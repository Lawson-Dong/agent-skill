"""Reduce vector matrices to 2D and export plots, coordinates and provenance."""
import argparse
import importlib.metadata
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.impute import SimpleImputer
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


def run(vectors, labels=None, texts=None, method='umap', output_format='html',
        output_dir='.', scale='none', missing='error', perplexity=30,
        n_neighbors=15, min_dist=0.1, feature_names=None):
    if method not in {'pca', 'tsne', 'umap'} or output_format not in {'html', 'png'}:
        raise ValueError('Invalid method or output format')
    if scale not in {'none', 'standard'} or missing not in {'error', 'median'}:
        raise ValueError('Invalid preprocessing option')
    sp = sparse.issparse(vectors)
    X = vectors.astype(float).tocsr(copy=True) if sp else np.array(vectors, dtype=float, copy=True)
    if X.ndim != 2 or X.shape[0] < 3 or X.shape[1] <= 2:
        raise ValueError('Require a matrix with >=3 samples and >2 features')
    n, d = X.shape
    for key, values in [('labels', labels), ('texts', texts)]:
        if values is not None and (np.asarray(values).ndim != 1 or len(values) != n):
            raise ValueError(f'{key} must have exactly one entry per row')
    if method == 'tsne' and n > 100000:
        raise ValueError('Use PCA or UMAP above 100,000 samples')
    data = X.data if sp else X
    invalid = int((~np.isfinite(data)).sum())
    if invalid:
        if missing == 'error' or sp:
            raise ValueError('NaN/Inf found; dense inputs allow explicit median imputation')
        X[~np.isfinite(X)] = np.nan
        if np.isnan(X).all(axis=0).any():
            raise ValueError('Cannot impute an entirely missing feature')
        X = SimpleImputer(strategy='median').fit_transform(X)
    if scale == 'standard':
        X = StandardScaler(with_mean=not sp).fit_transform(X)
    meta = dict(input_shape=[n, d], method=method, random_state=42, scale=scale,
                missing=missing, invalid_entries=invalid, sparse_input=sp,
                feature_names=feature_names, label_use='color only', pre_reduction=None)
    axis = ('SVD' if sp else 'PC') if method == 'pca' else method.upper()
    if method == 'pca':
        reducer = TruncatedSVD(n_components=2, random_state=42) if sp else PCA(n_components=2, random_state=42)
        Y = reducer.fit_transform(X)
        meta['effective_method'] = 'truncated_svd' if sp else 'pca'
        meta['explained_variance_ratio'] = reducer.explained_variance_ratio_.tolist()
    else:
        if sp or (method == 'tsne' and d > 100):
            k = min(50, d, n - 1)
            reducer = TruncatedSVD(n_components=k, random_state=42) if sp else PCA(n_components=k, random_state=42)
            X = reducer.fit_transform(X)
            meta['pre_reduction'] = dict(method='svd' if sp else 'pca', components=k)
        if method == 'tsne':
            if not np.isfinite(perplexity) or perplexity <= 0:
                raise ValueError('Require positive finite perplexity')
            p = min(float(perplexity), float(n - 1))
            Y = TSNE(n_components=2, perplexity=p, init='pca', learning_rate='auto', random_state=42).fit_transform(X)
            meta['parameters'] = dict(perplexity=p, init='pca', learning_rate='auto')
        else:
            if n_neighbors < 2 or not 0 <= min_dist <= 1:
                raise ValueError('Require neighbors >=2 and min_dist in [0,1]')
            import umap
            neighbors = min(int(n_neighbors), n - 1)
            init = 'random' if n == 3 else 'spectral'
            Y = umap.UMAP(n_components=2, n_neighbors=neighbors, min_dist=min_dist,
                          init=init, random_state=42, n_jobs=1).fit_transform(X)
            meta['parameters'] = dict(n_neighbors=neighbors, min_dist=min_dist, init=init)
    if Y.shape != (n, 2) or not np.isfinite(Y).all():
        raise ValueError('Invalid reduction output')
    frame = pd.DataFrame(dict(row_id=np.arange(n), x=Y[:, 0], y=Y[:, 1]))
    for key, values in [('label', labels), ('text', texts)]:
        if values is not None:
            frame[key] = pd.Series(list(values)).fillna('(missing)').astype(str)
    dest = Path(output_dir)
    dest.mkdir(parents=True, exist_ok=True)
    plot = dest / f'vector_visualization.{output_format}'
    title = f'{axis} 2D — {n:,} vectors, {d:,} features'
    if output_format == 'html':
        import plotly.express as px
        fig = px.scatter(frame, x='x', y='y', color='label' if labels is not None else None,
                         hover_data=[c for c in ['row_id', 'text'] if c in frame],
                         title=title, labels={'x': f'{axis}1', 'y': f'{axis}2'}, render_mode='webgl')
        fig.update_traces(marker=dict(size=5, opacity=0.7))
        fig.write_html(plot, include_plotlyjs=True, full_html=True)
    else:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 6))
        if labels is None:
            ax.scatter(frame.x, frame.y, s=8, alpha=0.7)
        else:
            for label in pd.unique(frame.label):
                group = frame[frame.label == label]
                ax.scatter(group.x, group.y, s=8, alpha=0.7, label=label)
            ax.legend(title='Label', bbox_to_anchor=(1.02, 1), loc='upper left')
        ax.set(title=title, xlabel=f'{axis}1', ylabel=f'{axis}2')
        fig.savefig(plot, dpi=160, bbox_inches='tight')
        plt.close(fig)
    versions = {}
    for package in ['numpy', 'pandas', 'scipy', 'scikit-learn', 'umap-learn', 'plotly', 'matplotlib']:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            pass
    meta['package_versions'] = versions
    frame.to_csv(dest / 'reduced_vectors.csv', index=False)
    (dest / 'reduction_metadata.json').write_text(json.dumps(meta, indent=2, allow_nan=False), encoding='utf-8')
    return dict(coordinates=frame, metadata=meta, plot_path=str(plot))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('vectors', type=Path)
    parser.add_argument('--label-column')
    parser.add_argument('--feature-columns', nargs='+')
    parser.add_argument('--method', choices=['pca', 'tsne', 'umap'], default='umap')
    parser.add_argument('--output-format', choices=['html', 'png'], default='html')
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--scale', choices=['none', 'standard'], default='none')
    parser.add_argument('--missing', choices=['error', 'median'], default='error')
    a = parser.parse_args()
    labels, columns = None, None
    if a.vectors.suffix.lower() == '.csv':
        table = pd.read_csv(a.vectors)
        candidates = [c for c in ['label', 'category'] if c in table]
        if not a.label_column and len(candidates) > 1:
            parser.error('Choose --label-column when both label and category exist')
        label = a.label_column or (candidates[0] if candidates else None)
        if label:
            labels = table[label].tolist()
        columns = a.feature_columns or [c for c in table.select_dtypes(include='number').columns if c != label]
        if label in columns:
            parser.error('Label column cannot be a feature')
        X = table[columns].to_numpy(dtype=float)
        print('Feature columns:', columns)
    elif a.vectors.suffix.lower() == '.npy':
        if a.label_column or a.feature_columns:
            parser.error('Column arguments only apply to CSV')
        X = np.load(a.vectors, allow_pickle=False)
    else:
        parser.error('Input must be CSV or NPY')
    result = run(X, labels=labels, feature_names=columns, method=a.method,
                 output_format=a.output_format, output_dir=a.output_dir,
                 scale=a.scale, missing=a.missing)
    print(json.dumps(dict(plot=result['plot_path'], metadata=result['metadata']), indent=2))


if __name__ == '__main__':
    main()

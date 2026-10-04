---
name: high-dimensional-vector-visualization-executer
description: Reduce high-dimensional vectors or embeddings to 2D with UMAP, PCA, or t-SNE; create interactive HTML or PNG scatter plots and export coordinate CSVs. Use for vector clouds, neural representations, embeddings, or numeric CSV/NPY matrices with optional categorical labels, including sparse matrices. Creating or installing this skill does not authorize running it on an existing project.
---

# High Dimensional Vector Visualization Executer

## Inputs

- Accept numeric lists, NumPy arrays, sparse matrices, or CSV/NPY paths as `vectors`, with shape `(n_samples, n_features)`, at least three samples and more than two features. Establish the sample axis; never silently flatten or transpose.
- Accept optional categorical `labels` and hover `texts`, each with one entry per sample. Use labels for coloring only, never supervised UMAP targets.
- Default `method` to `umap`; support `pca` and `tsne`.
- Default `output_format` to `html`; support `png`.
- Default `scale` to `none`; use `standard` explicitly for heterogeneous measurement units. Do not automatically standardize learned embeddings or neural vectors: this changes original geometry.
- Default missing-value handling to an error; support explicit median imputation. Never silently drop rows or replace infinity with zero.

## Workflow

1. Resolve the actual requested upload or file path. Use `/mnt/data` only when appropriate; do not assume all uploads reside there. Retrieve Library inputs when needed. Inspect CSV numeric columns and exclude IDs/metadata. Extract an explicit label column, or an unambiguous `label`/`category` column; ask if both exist. Never include labels as features. Load NPY with `allow_pickle=False`.
2. Check dependencies in the executing interpreter. Install only missing packages using that interpreter's `-m pip install` when permitted: `numpy pandas scipy scikit-learn matplotlib`, `umap-learn` for UMAP and `plotly` for HTML. Report installation blockers; never silently switch method or format.
3. Execute `scripts/visualize_vectors.py` relative to this skill directory. Use `run()` for in-memory inputs and CLI for files. Set seed 42. Use TruncatedSVD instead of PCA for sparse data without densifying the original matrix. Reduce sparse inputs to a manageable dense SVD representation before nonlinear methods.
4. For t-SNE above 100 features, apply PCA to `min(50, n_features, n_samples - 1)` components first. Keep perplexity strictly below sample count. Keep UMAP neighbors below sample count, and use random initialization for three samples. Reject t-SNE above 100,000 samples. Never silently sample; if sampling is requested, retain original row IDs and use seed 42.
5. Generate a scatter plot with categorical colors, legend, title, component axes and row IDs/optional texts on hover. Use self-contained Plotly HTML for interactivity and Matplotlib for PNG. Display PNG inline or use an available artifact renderer for HTML; a download link alone is not an inline plot.
6. Verify finite coordinates, original row count, label alignment and output creation. Save `reduced_vectors.csv`, `vector_visualization.html` or `.png`, and `reduction_metadata.json` in a task-specific directory. Record method, effective parameters, preprocessing, input shape and package versions. Persist final artifacts using the Library skill when available; return exact sandbox download links. Do not save skill files separately to Library.
7. Report method, preprocessing and links briefly. Explain that 2D geometry is approximate: t-SNE/UMAP cluster distances, sizes and density need not represent original-space geometry. Measure original-space quantities separately. For layer/model comparisons, independent fits can rotate, flip or rearrange; do not describe this as vector motion without a justified shared projection or alignment. Seed 42 does not guarantee identical results across package versions or environments.

## Execution

```bash
python <skill-directory>/scripts/visualize_vectors.py vectors.csv \
  --label-column label --method umap --output-format html --output-dir <output-directory>
python <skill-directory>/scripts/visualize_vectors.py vectors.npy \
  --method pca --output-format png --output-dir <output-directory>
```

For in-memory inputs, import the script via `importlib.util` and call `run(vectors, labels=labels, texts=texts, method="umap", output_format="html", output_dir=output_directory)`.

Use `--feature-columns` to explicitly select CSV features. Override `scale`, `missing`, `perplexity`, `n_neighbors`, or `min_dist` through `run()` when requested; record effective values. Defaults: UMAP neighbors 15/min_dist 0.1; t-SNE perplexity 30/PCA initialization/automatic learning rate. Report explained variance for PCA or sparse linear SVD.

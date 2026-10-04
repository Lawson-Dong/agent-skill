"""Generate three synthetic Gaussian groups and export their 2D projection."""
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/visualize_vectors.py'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--method', choices=['umap', 'pca', 'tsne'], default='umap')
    parser.add_argument('--output-format', choices=['html', 'png'], default='html')
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    dest = args.output_dir or ROOT / 'outputs/random-vectors' / args.method
    dest.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(42)
    centers = rng.normal(0, 2, (3, 64))
    vectors = np.repeat(centers, 100, axis=0) + rng.normal(0, 1, (300, 64))
    labels = np.repeat(['Group A', 'Group B', 'Group C'], 100)
    np.save(dest / 'random_vectors.npy', vectors)
    spec = importlib.util.spec_from_file_location('visualize_vectors', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.run(vectors, labels=labels, method=args.method,
                        output_format=args.output_format, output_dir=dest)
    result['metadata']['generation'] = {
        'seed': 42, 'samples_per_group': 100,
        'distribution': 'three Gaussian groups; centers N(0, 2^2), noise N(0, 1)'}
    (dest / 'reduction_metadata.json').write_text(
        json.dumps(result['metadata'], indent=2), encoding='utf-8')
    print(result['plot_path'])

if __name__ == '__main__':
    main()

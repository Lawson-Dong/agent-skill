"""Check exported artifacts, label preservation, sparse handling, and bad inputs."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import numpy as np
import pandas as pd
from scipy import sparse

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/visualize_vectors.py'
spec = importlib.util.spec_from_file_location('visualize_vectors', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class VisualizationTests(unittest.TestCase):
    def test_methods_and_exports(self):
        X = np.random.default_rng(42).normal(size=(36, 128))
        labels = ['A'] * 18 + ['B'] * 18
        for method, fmt in [('pca', 'png'), ('umap', 'html'), ('tsne', 'png')]:
            with self.subTest(method=method), tempfile.TemporaryDirectory() as directory:
                result = module.run(X, labels=labels, method=method, output_format=fmt, output_dir=directory)
                frame = pd.read_csv(Path(directory) / 'reduced_vectors.csv')
                self.assertEqual(frame.shape, (36, 4))
                self.assertEqual(frame.label.tolist(), labels)
                self.assertEqual(frame.row_id.tolist(), list(range(36)))
                self.assertTrue(np.isfinite(frame[['x', 'y']]).all().all())
                self.assertGreater(Path(result['plot_path']).stat().st_size, 100)
                meta = json.loads((Path(directory) / 'reduction_metadata.json').read_text())
                self.assertEqual(meta['input_shape'], [36, 128])
                self.assertEqual(meta['scale'], 'none')
                if method == 'tsne':
                    self.assertEqual(meta['pre_reduction']['components'], 35)

    def test_sparse_pca(self):
        with tempfile.TemporaryDirectory() as directory:
            result = module.run(sparse.eye(8), method='pca', output_format='png', output_dir=directory)
            self.assertEqual(result['metadata']['effective_method'], 'truncated_svd')

    def test_invalid_inputs(self):
        for X, labels in [(np.ones((2, 4)), None), (np.full((5, 4), np.nan), None),
                          (np.ones((5, 4)), ['A'])]:
            with self.subTest(shape=X.shape), tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    module.run(X, labels=labels, output_dir=directory)

if __name__ == '__main__':
    unittest.main()

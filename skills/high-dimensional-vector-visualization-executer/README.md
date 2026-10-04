# High Dimensional Vector Visualization Executer

Reduce high-dimensional vectors to 2D with UMAP, PCA, or t-SNE. The agent instructions are in [SKILL.md](SKILL.md). This folder contains all dependencies, scripts, metadata, examples, and tests for this skill.

## Setup

Use Python 3.11 or newer. From this skill directory:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

To use the skill in an agent that supports local skills, copy this complete `high-dimensional-vector-visualization-executer` directory into that agent's skill directory. ChatGPT Work users can import the skill through their supported skill workflow. Installation paths depend on the host; the Python script also runs independently.

## Run on your vectors

Input shape is `(n_samples, n_features)`, with at least three samples and more than two features. Labels are used only for coloring.

```bash
python scripts/visualize_vectors.py vectors.npy --method umap --output-format html --output-dir outputs/my-vectors
python scripts/visualize_vectors.py vectors.csv --label-column label --feature-columns f1 f2 f3 --method pca --output-format png --output-dir outputs/pca
```

For CSV inputs, explicitly select feature columns when IDs or numeric metadata are present. Scaling is off by default; use `--scale standard` only when intended. NaN/Inf values cause an error unless `--missing median` is explicitly selected for dense inputs.

Outputs: `vector_visualization.html` or `.png`, `reduced_vectors.csv`, and `reduction_metadata.json`.

## Reproduce the random-vector example

```bash
python examples/random_vectors.py --method umap
```

This generates 300 vectors with 64 features from three synthetic Gaussian groups, using seed 42. The groups are built into the data; they are not a discovery about neural representations. Open `outputs/random-vectors/umap/vector_visualization.html` for zooming and point details. Use `--method pca` or `--method tsne` to compare projections.

UMAP and t-SNE preserve aspects of local structure. Distances between clusters, cluster sizes, and density in 2D need not match the original space. Independent fits may rotate or rearrange; they do not establish vector motion across layers. Measure high-dimensional geometry separately.

## Validation

```bash
python -m unittest discover -s tests -v
python examples/random_vectors.py --method pca --output-format png
```

Licensed under the repository [MIT license](../../LICENSE).

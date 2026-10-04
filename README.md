# Agent Skills

Reusable agent skills by Lawson Dong. Each skill contains its instructions, executable resources, and agent metadata.

## Skills

| Skill | Purpose | Dedicated branch |
| --- | --- | --- |
| [High Dimensional Vector Visualization Executer](skills/high-dimensional-vector-visualization-executer/SKILL.md) | Reduce vector matrices to 2D with UMAP, PCA, or t-SNE; export interactive HTML or PNG, coordinates, and metadata. | [High-Dimensional-Vector-Visualization-Excuter](https://github.com/Lawson-Dong/agent-skill/tree/High-Dimensional-Vector-Visualization-Excuter) |

## Setup

Use Python 3.11 or newer. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

To use the skill in an agent that supports local skills, copy the complete `skills/high-dimensional-vector-visualization-executer` directory into that agent's skill directory. ChatGPT Work users can import the skill through their supported skill workflow. Installation paths depend on the host; the Python script also runs independently.

## Run on your vectors

Input shape is `(n_samples, n_features)`, with at least three samples and more than two features. Labels are used only for coloring.

```bash
python skills/high-dimensional-vector-visualization-executer/scripts/visualize_vectors.py vectors.npy --method umap --output-format html --output-dir outputs/my-vectors
python skills/high-dimensional-vector-visualization-executer/scripts/visualize_vectors.py vectors.csv --label-column label --feature-columns f1 f2 f3 --method pca --output-format png --output-dir outputs/pca
```

For CSV inputs, explicitly select feature columns when IDs or numeric metadata are present. Scaling is off by default; use `--scale standard` only when intended. NaN/Inf values cause an error unless `--missing median` is explicitly selected for dense inputs.

Outputs: `vector_visualization.html` or `.png`, `reduced_vectors.csv`, and `reduction_metadata.json`.

## Reproduce the random-vector example

```bash
python examples/random_vectors.py --method umap
```

This generates 300 vectors with 64 features from three synthetic Gaussian groups, using seed 42. The groups are built into the data; they are not a discovery about neural representations. Open `outputs/random-vectors/umap/vector_visualization.html` for zooming and point details. Use `--method pca` or `--method tsne` to compare projections.

UMAP and t-SNE preserve aspects of local structure. Distances between clusters, cluster sizes, and density in 2D need not match the original space. Independent fits may rotate or rearrange; they do not establish vector motion across layers. Measure high-dimensional geometry separately.

## Repository maintenance

`main` contains the published skill collection. Dedicated branches can develop individual skills; merge validated changes into `main` and keep both versions synchronized. The existing branch spelling `Excuter` is retained for link compatibility; the skill's canonical name is `high-dimensional-vector-visualization-executer`.

Before publishing, run:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs these checks on pushes and pull requests. Keep generated datasets and plots under `outputs/` (ignored by Git). Record package versions and parameters with each experiment rather than assuming seed 42 reproduces results across environments.

Licensed under [MIT](LICENSE).

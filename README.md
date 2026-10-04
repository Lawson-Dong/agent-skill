# Agent Skills

A collection of reusable agent skills by Lawson Dong. Published skills live together on `main`, each in a self-contained folder under `skills/`.

## Skill catalog

| Skill | Purpose | Instructions |
| --- | --- | --- |
| [High Dimensional Vector Visualization Executer](skills/high-dimensional-vector-visualization-executer/) | Reduce vectors or embeddings to 2D with UMAP, PCA, or t-SNE; export interactive HTML or PNG, coordinates, and metadata. | [SKILL.md](skills/high-dimensional-vector-visualization-executer/SKILL.md) |

## Use a skill

1. Open its folder and read its `README.md` for setup and examples.
2. Copy the complete skill folder into your agent's supported skill directory, or use the host's import workflow. Installation paths depend on the host.
3. Install only that skill's dependencies, if any. Scripts can also run independently.

For the vector visualization skill:

```bash
cd skills/high-dimensional-vector-visualization-executer
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python examples/random_vectors.py --method umap
```

## Repository layout

- `skills/<skill-name>/SKILL.md`: agent instructions and trigger metadata.
- `skills/<skill-name>/README.md`: human-facing setup and examples.
- Each skill owns its supporting resources, such as `scripts/`, `agents/`, `assets/`, `examples/`, `tests/`, and `requirements.txt`. Include only what it needs.
- `.github/workflows/validate.yml`: shared validation for the collection.
- `LICENSE`: MIT license for the repository.

## Add or maintain a skill

Use lowercase hyphenated folder names matching the `name` in `SKILL.md`. Add each skill as a new folder under `skills/` and add it to the catalog above. Keep dependencies and examples inside its own folder; use paths relative to that folder so it remains portable.

Publish validated changes on `main`. Branches may be temporary development branches, but are not separate skill catalogs and do not need to be kept synchronized. Link to skill folders on `main`.

GitHub Actions discovers all skill folders, checks their instruction metadata, and runs each skill's tests when present. Python skills with a `requirements.txt` have those dependencies installed in their own CI job. Run equivalent checks locally before publishing. Keep generated files under `outputs/` (ignored by Git).

Licensed under [MIT](LICENSE).

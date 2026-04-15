# Contributing

Thanks for your interest in improving the workshop materials! This repository is a teaching resource, so contributions that make the codebook clearer, the exercises smoother, or the setup easier are especially welcome.

## Ways to contribute

- **Fix typos or unclear wording** in the codebook, README, or exercise instructions
- **Report a setup problem** you ran into on your platform — open an issue with the OS, Python version, and full error message
- **Improve the sample data** — flag sentences that are misleading or suggest replacements that better illustrate an annotation challenge
- **Translate** parts of the codebook into another language (especially DE, NL, ES, DA, which the models support)
- **Suggest new exercises** that highlight an annotation edge case or a model limitation

## Workflow

1. Open an issue first for anything non-trivial so we can discuss the approach
2. Fork the repo and create a branch: `git checkout -b fix/typo-in-codebook`
3. Make your change; keep it focused — one concern per pull request
4. Run the smoke check locally if you touched data or scripts:
   ```bash
   python -m py_compile exercises/exercise_B_pipeline.py exercises/exercise_C_validate.py
   python -c "import pandas as pd; pd.read_csv('data/sample_manifestos.csv'); pd.read_csv('data/annotation_practice.csv')"
   ```
5. Open a pull request describing what changed and why

## Style

- Markdown: one sentence per line in long-form docs makes diffs readable
- Python: PEP 8, type hints where they aid clarity, no heavyweight dependencies beyond what's already in `requirements.txt`
- Keep examples runnable on a CPU in under a few minutes

## Questions

For workshop or research questions, reach out to the maintainers:

- Alona Dolinsky — a.dolinsky@bham.ac.uk
- Dylan Paltra — dylan.paltra@uni-oldenburg.de

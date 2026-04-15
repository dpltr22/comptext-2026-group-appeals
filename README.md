# From Concept to Computation: Identifying Group Appeals in Text

**COMPTEXT 2026 Workshop · University of Birmingham**
*Alona Dolinsky (a.dolinsky@bham.ac.uk) & Dylan Paltra (dylan.paltra@uni-oldenburg.de)*

This repository contains all materials for the COMPTEXT 2026 workshop on identifying social-group appeals in political text — from manual annotation through automated detection with the [`groupappeals`](https://pypi.org/project/groupappeals/) Python package.

---

## What you'll learn

- **Part 1 — Concept & Manual Annotation (~75 min):** why group appeals matter, how social groups and appeals are defined, how to build a reliable annotation codebook, and how to validate it.
- **Part 2 — Computation & Practice (~90 min):** an end-to-end NLP pipeline (group detection → stance → policy → category), hands-on use of the `groupappeals` package, and a guided exercise on sample data.

## Repository structure

```
.
├── README.md                  # this file
├── slides/                    # workshop slide deck (PDF / PPTX)
├── docs/
│   ├── codebook.md            # manual annotation codebook
│   ├── group_categories.md    # the 43 meaningful group categories
│   └── setup.md               # detailed installation & troubleshooting
├── data/
│   ├── sample_manifestos.csv  # small CSV for the hands-on exercise
│   └── annotation_practice.csv# 10 sentences for Exercise A
├── exercises/
│   ├── exercise_A_manual.md   # manual annotation worksheet
│   ├── exercise_B_pipeline.py # run the groupappeals pipeline
│   └── exercise_C_validate.py # explore & validate results
├── notebooks/
│   └── workshop_walkthrough.ipynb
├── requirements.txt
├── environment.yml            # conda alternative
├── LICENSE
└── .github/workflows/ci.yml
```

## Quick start

```bash
# 1. Clone
git clone https://github.com/<your-org>/comptext-2026-group-appeals.git
cd comptext-2026-group-appeals

# 2. Set up an environment (pick one)
python -m venv .venv && source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate                            # Windows

pip install -r requirements.txt

# 3. Verify
python -c "from groupappeals import run_full_pipeline; print('ok')"
```

A GPU is recommended for the stance/policy/classification steps; CPU works for the small sample data shipped here. See [`docs/setup.md`](docs/setup.md) if you run into trouble.

## Hands-on exercise (~45 min)

| Part | Time | What you do |
|------|------|-------------|
| A — Manual annotation | 10 min | Annotate 10 sentences using the codebook; compare with a neighbour |
| B — Run the pipeline | 20 min | Apply `groupappeals` to the sample (or your own) data |
| C — Explore & validate | 15 min | Compute distributions, spot-check 5–10 outputs, characterise errors |

Full instructions live in [`exercises/`](exercises/).

## Citing this work

If you use the package, codebook, or PSoGA database in your research, please cite:

- Dolinsky, A., Huber, R. A., & Horne, W. (2026). *Party Statements on Group Appeals (PSoGA) Database* [Data set]. Harvard Dataverse. <https://doi.org/10.7910/DVN/FVI3QW>
- Huber, R. A., & Dolinsky, A. (2023). On the definition and measurement of social-group appeals.

## License

Materials in this repository are released under the [MIT License](LICENSE). The `groupappeals` package and PSoGA database have their own licenses — please consult them separately.

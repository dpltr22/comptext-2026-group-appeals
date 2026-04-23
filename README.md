# From Concept to Computation: Identifying Group Appeals in Text

**COMPTEXT 2026 Workshop · University of Birmingham**
*Alona O. Dolinsky (a.o.dolinsky@bham.ac.uk) & Dylan Paltra (dylan.paltra@uni-oldenburg.de)*

This repository contains all materials for the COMPTEXT 2026 workshop on identifying social-group appeals in political text — from manual annotation through automated detection with the [`groupappeals`](https://pypi.org/project/groupappeals/) Python package.

---

## What you'll learn

- **Part 1 — Concept & Manual Annotation:** why group appeals matter, how social groups and appeals are defined, how to build a reliable annotation codebook, and how to validate it.
- **Part 2 — Computation & Practice:** an end-to-end NLP pipeline walkthrough (group detection → stance → policy → category), hands-on use of the `groupappeals` package, and a guided exercise on sample data.

## Hands-on exercise

| Part | What you do |
|------|--------------|
| A — Run the pipeline | Apply `groupappeals` to the sample (or your own) data |
| B — Manual annotation | Annotate 10 sentences using the codebook; compare with a neighbour |
| C — Explore & validate | Compute distributions, spot-check 5–10 outputs, characterise errors |

Full instructions live in [`exercises/`](exercises/).

## Citing this work

If you use the package, codebook, or PSoGA database in your research, please cite:

- Dolinsky, A.O, Huber, L.M., & Horne, W. (2026). *PSoGA: Sentence-level and manifesto-level social group appeals in party election manifestos across eight European democracies, 1970–2025* [Data set]. Harvard Dataverse. <https://doi.org/10.7910/DVN/FVI3QW>
- Huber, L.M., & Dolinsky, A.O. (2023). How parties shape their relationship with social groups:A roadmap to the study of group-based appeals. OSF. https://osf.io/preprints/osf/szaqw_v1

## License

Materials in this repository are released under the [MIT License](LICENSE). The `groupappeals` package and PSoGA database have their own licenses — please consult them separately.

"""
Exercise C — Explore & Validate Results (~15 min)
================================================

Goal: compute simple distributions, spot-check 5–10 rows by hand, and
characterise the kinds of errors the model makes.

Run from the repo root after Exercise B has produced sample_results.csv:

    python exercises/exercise_C_validate.py
"""

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_FILE = REPO_ROOT / "sample_results.csv"


def main() -> None:
    if not RESULTS_FILE.exists():
        raise SystemExit(
            f"Results not found at {RESULTS_FILE}.\n"
            "Run exercises/exercise_B_pipeline.py first."
        )

    df = pd.read_csv(RESULTS_FILE)

    # 1. How many sentences had a group detected?
    has_group = df["Exact.Group.Text"].notna()
    print(f"Sentences with a detected group: {has_group.sum()} / {len(df)}")

    # 2. Stance distribution
    print("\nStance distribution (rows with a group):")
    print(df.loc[has_group, "Stance_Clean"].value_counts())

    # 3. Policy distribution
    print("\nPolicy distribution (rows with a group):")
    print(df.loc[has_group, "Policy_Clean"].value_counts())

    # 4. Most common group categories
    if "Group1" in df.columns:
        print("\nTop 10 group categories:")
        print(df["Group1"].value_counts().head(10))

    # 5. Sample 10 rows for manual inspection
    print("\nRandom sample of 10 detections — inspect by eye:")
    cols = [
        "text", "Exact.Group.Text",
        "Stance_Clean", "Policy_Clean", "Group1",
    ]
    sample_n = min(10, has_group.sum())
    if sample_n > 0:
        print(df[has_group][cols].sample(sample_n, random_state=42).to_string(index=False))

    # ------------------------------------------------------------------
    # Discussion prompts
    # ------------------------------------------------------------------
    print("""

Discussion prompts
------------------
- Do the detected group spans match what you would have annotated?
- Where does the model under- or over-detect groups?
- Are stance labels plausible? (in manifestos, expect a positive majority)
- Which sentences would you re-check on a larger run?
""")


if __name__ == "__main__":
    main()

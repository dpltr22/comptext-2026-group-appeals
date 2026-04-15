"""
Exercise B — Run the groupappeals pipeline (~20 min)
====================================================

Goal: apply the full pipeline to a small CSV and inspect the output. Compare
the model's group detections with your manual annotations from Exercise A.

Run from the repo root:

    python exercises/exercise_B_pipeline.py

Switch to your own data by changing INPUT_FILE.
"""

from pathlib import Path

from groupappeals import run_full_pipeline

# ---------------------------------------------------------------------------
# Configuration — edit these to point at your own data
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = REPO_ROOT / "data" / "sample_manifestos.csv"
OUTPUT_FILE = REPO_ROOT / "sample_results.csv"


def main() -> None:
    print(f"Reading: {INPUT_FILE}")
    print(f"Writing: {OUTPUT_FILE}\n")

    result_df = run_full_pipeline(
        input_file=str(INPUT_FILE),
        output_file=str(OUTPUT_FILE),
        text_column="text",
        # Build a composite ID like 'Labour_2019_1' for full traceability
        create_composite_id=["party", "year", "sentence_id"],
        clean_labels=True,
        split_groups=True,
        batch_size=8,           # bump to 32+ on a GPU
    )

    print(f"\nDone. {len(result_df)} rows written.")
    print("\nFirst few rows of the output:")
    cols = [
        "text_id", "text", "Exact.Group.Text",
        "Stance_Clean", "Policy_Clean", "Group1",
    ]
    print(result_df[cols].head(10).to_string(index=False))


if __name__ == "__main__":
    main()

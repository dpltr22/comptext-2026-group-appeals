# Setup & Troubleshooting

## Requirements

- **Python 3.8+** (3.10 or 3.11 recommended)
- **PyTorch** with a backend appropriate for your machine (CUDA on NVIDIA GPUs, MPS on Apple Silicon, or CPU)
- ~3 GB free disk space for cached model weights on first run

## Option 1 — `pip` + `venv`

```bash
python -m venv .venv
source .venv/bin/activate            # Linux / macOS
# .venv\Scripts\activate             # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

## Option 2 — `conda` / `mamba`

```bash
conda env create -f environment.yml
conda activate groupappeals-workshop
```

## Verify the install

```bash
python -c "from groupappeals import run_full_pipeline; print('groupappeals ready')"
```

The first call to a model will download weights from HuggingFace (~500 MB per model). Subsequent runs load from cache.

## Hardware notes

| Backend | Detection | Recommended `batch_size` |
|---------|-----------|--------------------------|
| CUDA (NVIDIA GPU) | Auto | 32–64 |
| MPS (Apple Silicon) | Auto | 16–32 |
| CPU | Auto fallback | 4–8; use the small sample CSV |

Group **detection** is fast even on CPU. Stance, policy, and category classification are noticeably slower without a GPU — the sample dataset is sized to finish in a few minutes on a modern laptop.

## Common issues

**`OSError: Can't load tokenizer ...`** — your machine couldn't reach HuggingFace. Check your network or pre-download with `huggingface-cli download <model>`.

**`CUDA out of memory`** — lower `batch_size` (e.g. 8) or pass `device='cpu'`.

**Slow first run** — expected. Models are being downloaded and cached. Re-running uses the cache.

**Windows + long paths** — enable long paths in Windows or move the cache directory closer to root: set `HF_HOME=C:\hf`.

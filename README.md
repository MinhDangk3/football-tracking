Project run instructions

This repository analyzes football videos using a YOLO-based detector and additional modules.

Quick start (PowerShell on Windows):

1. Create a virtual environment and activate it

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Upgrade pip and install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Note about torch: If you have a CUDA-capable GPU, install a matching torch+cuda wheel from https://pytorch.org/get-started/locally. Example CPU-only:

```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

3. Run the main script

```powershell
python main.py
```

Files of interest:

- `main.py` — entry point
- `yolo_inf.py` — small YOLO inference example
- `models/best.pt` — model weights used by the tracker

Troubleshooting:

- If you see errors importing `supervision`, install it from https://pypi.org/project/supervision/ or `pip install supervision`.
- If video doesn't read, confirm `input_video/08fd33_4.mp4` exists.
- If you prefer, run `yolo_inf.py` standalone to test model inference.

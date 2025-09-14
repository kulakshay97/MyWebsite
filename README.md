# Personal Website Generator

This repository contains a small Python static site generator using Jinja2.
Run `python generate.py` to produce a static website in the `docs/` folder,
ready to be served by GitHub Pages (select branch `main` and folder `/docs`).

Steps:
1. Create virtualenv and install requirements:
   ```
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Edit `data.yaml` with your info.
3. Run `python generate.py`
4. Preview with `python -m http.server --directory docs 8000` and open http://localhost:8000

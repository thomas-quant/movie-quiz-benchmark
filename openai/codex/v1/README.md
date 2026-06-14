# Movie Types Quiz

A small Flask quiz app with one page per question and session-backed context.

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/flask --app app run --debug
```

Open `http://127.0.0.1:5000`.

## Test

```bash
.venv/bin/python -m pytest -q
```

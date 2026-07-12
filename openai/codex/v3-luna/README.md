# Reel Types

A 30-question, multi-page Flask quiz about movie genres and film types.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```

Then open http://127.0.0.1:5000.

Quiz progress is stored in the Flask session, so the current question, score, and previous answer remain available as the user moves between pages.

# Reel Types Quiz

A Flask quiz about movie types and genres. It presents one question per page, keeps answers and score in the Flask session, shows feedback from the previous page, and includes 30 questions.

## Run locally

Create and activate a virtual environment, then install the dependency:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

Set `FLASK_SECRET_KEY` to a strong random value before deploying the app.

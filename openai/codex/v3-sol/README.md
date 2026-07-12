# Reel Knowledge

A 30-question, multi-page Flask quiz about movie genres. Answers and progress are kept between pages using Flask's signed session cookie.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```

Open `http://127.0.0.1:5000`.

For production, set a strong `SECRET_KEY` environment variable before starting the app.

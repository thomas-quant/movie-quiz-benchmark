# Movie Types Quiz

A multi-page Flask quiz on movie genres and types — 32 questions, one per page,
with progress, score, and per-question feedback carried across pages via the
Flask session cookie.

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```

Then open http://127.0.0.1:5000

Set `QUIZ_SECRET_KEY` in the environment for anything beyond local development.

## How it works

- `questions.py` — the 32-question bank (text, choices, correct index).
- `app.py` — routes:
  - `/` start page (offers resume if a quiz is in progress)
  - `/start` resets the session and begins at question 1
  - `/question/<n>` shows one question per page; POST records the answer and
    redirects to the next page (post/redirect/get). Skipping ahead redirects
    back to the first unanswered question.
  - `/results` final score plus a full review of every answer.
- State (`answers`, `score`, `last_feedback`) lives in the signed session
  cookie, so each new page knows what happened on the previous one.

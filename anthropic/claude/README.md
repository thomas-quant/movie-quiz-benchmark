# 🎬 Movie Types Quiz

A multi-page Flask quiz on the **types/genres of movies**. Each question lives on
its own page, and your answers are remembered in the session as you move forward,
back, or refresh — so context is never lost between pages.

- **32 questions**, one per page
- Multiple choice (4 options each)
- Forward / back navigation with answers preserved
- Progress bar + scored results page with a per-question review

## Run it

```bash
cd claude
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

> Optional: set a stable `FLASK_SECRET_KEY` env var so sessions survive restarts.
> Without it a random key is generated each launch.

## How the multi-page state works

State is stored in Flask's signed `session` cookie under `answers`, a map of
`{question_number: chosen_option_index}`. Routes:

| Route          | Purpose                                            |
| -------------- | -------------------------------------------------- |
| `/`            | Landing page (offers Start / Resume)               |
| `/start`       | Clears progress, redirects to question 1           |
| `/quiz/<n>`    | GET shows question *n*; POST saves the answer       |
| `/results`     | Scores all answers and shows a review              |

## Files

```
app.py            # Flask routes + scoring
questions.py      # The question bank (edit/add questions here)
templates/        # base, start, question, results (Jinja2)
static/style.css  # Styling
```

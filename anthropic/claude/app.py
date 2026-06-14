"""A multi-page Flask quiz about types of movies.

Each question lives on its own page (/quiz/<n>). Progress is kept in the
server-side-signed session cookie, so answers from earlier pages survive as
the user moves forward, backward, or refreshes — context is never lost.
"""

import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from questions import QUESTIONS

app = Flask(__name__)
# In production, set FLASK_SECRET_KEY in the environment. The random fallback
# keeps things working out of the box (sessions just reset on restart).
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(32))

TOTAL = len(QUESTIONS)


def _answers():
    """Return the per-question answer map from the session ({index: choice})."""
    return session.get("answers", {})


@app.route("/")
def index():
    """Landing page — explains the quiz and links to the first question."""
    answered = len(_answers())
    return render_template("start.html", total=TOTAL, answered=answered)


@app.route("/start")
def start():
    """Reset all progress and jump to the first question."""
    session["answers"] = {}
    session.modified = True
    return redirect(url_for("quiz", n=1))


@app.route("/quiz/<int:n>", methods=["GET", "POST"])
def quiz(n):
    """Show question ``n`` (1-based) and record the submitted answer."""
    if n < 1 or n > TOTAL:
        return redirect(url_for("quiz", n=1))

    answers = _answers()

    if request.method == "POST":
        # Persist the selected option (if any) before navigating.
        choice = request.form.get("choice")
        if choice is not None and choice.isdigit():
            answers[str(n)] = int(choice)
            session["answers"] = answers
            session.modified = True

        direction = request.form.get("direction", "next")
        if direction == "prev":
            return redirect(url_for("quiz", n=max(1, n - 1)))
        if n >= TOTAL:
            return redirect(url_for("results"))
        return redirect(url_for("quiz", n=n + 1))

    question = QUESTIONS[n - 1]
    return render_template(
        "question.html",
        question=question,
        n=n,
        total=TOTAL,
        selected=answers.get(str(n)),
        answered=len(answers),
        is_last=(n == TOTAL),
    )


@app.route("/results")
def results():
    """Score every recorded answer and present a breakdown."""
    answers = _answers()
    review = []
    score = 0
    for i, q in enumerate(QUESTIONS, start=1):
        chosen = answers.get(str(i))
        correct = q["answer"]
        is_correct = chosen == correct
        if is_correct:
            score += 1
        review.append(
            {
                "n": i,
                "q": q["q"],
                "options": q["options"],
                "chosen": chosen,
                "correct": correct,
                "is_correct": is_correct,
                "answered": chosen is not None,
                "explain": q["explain"],
            }
        )

    pct = round(100 * score / TOTAL) if TOTAL else 0
    if pct >= 90:
        verdict = "Cinephile! You know your genres cold."
    elif pct >= 70:
        verdict = "Solid — you'd win most movie-night debates."
    elif pct >= 50:
        verdict = "Not bad. A few more matinees and you'll be set."
    else:
        verdict = "Time for a film festival binge!"

    return render_template(
        "results.html",
        review=review,
        score=score,
        total=TOTAL,
        pct=pct,
        verdict=verdict,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

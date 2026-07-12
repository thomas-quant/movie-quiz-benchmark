import os

from flask import Flask, redirect, render_template, request, session, url_for

from questions import QUESTIONS

app = Flask(__name__)
# Signs the session cookie so quiz state survives across pages.
app.secret_key = os.environ.get("QUIZ_SECRET_KEY", "dev-only-change-me")

TOTAL = len(QUESTIONS)


def answers():
    """Answers recorded so far, as {question_index: chosen_choice_index}.

    Session keys are stored as strings because the cookie is JSON-serialized.
    """
    return {int(k): v for k, v in session.get("answers", {}).items()}


def first_unanswered():
    done = answers()
    for i in range(TOTAL):
        if i not in done:
            return i
    return TOTAL  # everything answered


@app.route("/")
def index():
    in_progress = len(answers())
    return render_template(
        "index.html",
        total=TOTAL,
        in_progress=in_progress if 0 < in_progress < TOTAL else 0,
        resume_at=first_unanswered() + 1,
    )


@app.route("/start")
def start():
    session.clear()
    session["answers"] = {}
    session["score"] = 0
    return redirect(url_for("question", number=1))


@app.route("/question/<int:number>", methods=["GET", "POST"])
def question(number):
    if "answers" not in session:
        return redirect(url_for("index"))
    if not 1 <= number <= TOTAL:
        return redirect(url_for("index"))

    idx = number - 1
    done = answers()

    # Don't allow skipping ahead of the first unanswered question,
    # and send finished quizzes to the results page.
    expected = first_unanswered()
    if expected >= TOTAL:
        return redirect(url_for("results"))
    if idx != expected:
        return redirect(url_for("question", number=expected + 1))

    q = QUESTIONS[idx]

    if request.method == "POST":
        try:
            choice = int(request.form["choice"])
        except (KeyError, ValueError):
            return render_template(
                "question.html",
                q=q,
                number=number,
                total=TOTAL,
                score=session.get("score", 0),
                feedback=None,
                error="Please select an answer before continuing.",
            )
        if not 0 <= choice < len(q["choices"]):
            return redirect(url_for("question", number=number))

        correct = choice == q["answer"]
        done[idx] = choice
        session["answers"] = {str(k): v for k, v in done.items()}
        if correct:
            session["score"] = session.get("score", 0) + 1
        # Carried to the next page so the user sees how they did last question.
        session["last_feedback"] = {
            "number": number,
            "correct": correct,
            "chosen": q["choices"][choice],
            "right_answer": q["choices"][q["answer"]],
        }
        if number == TOTAL:
            return redirect(url_for("results"))
        return redirect(url_for("question", number=number + 1))

    feedback = session.pop("last_feedback", None)
    return render_template(
        "question.html",
        q=q,
        number=number,
        total=TOTAL,
        score=session.get("score", 0),
        feedback=feedback,
        error=None,
    )


@app.route("/results")
def results():
    done = answers()
    if len(done) < TOTAL:
        return redirect(url_for("question", number=first_unanswered() + 1))

    review = []
    for i, q in enumerate(QUESTIONS):
        chosen = done[i]
        review.append(
            {
                "number": i + 1,
                "text": q["text"],
                "chosen": q["choices"][chosen],
                "right_answer": q["choices"][q["answer"]],
                "correct": chosen == q["answer"],
            }
        )
    score = session.get("score", 0)
    return render_template(
        "results.html",
        score=score,
        total=TOTAL,
        percent=round(score * 100 / TOTAL),
        review=review,
    )


if __name__ == "__main__":
    app.run(debug=True)

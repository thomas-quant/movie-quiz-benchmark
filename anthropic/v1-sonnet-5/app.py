from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-in-production"

# Each question tests knowledge of movie genres / types.
# options: list of 4 strings. answer: index (0-3) of the correct option.
QUESTIONS = [
    {"question": "Which genre is defined by high-speed chases, explosions, and stunts?",
     "options": ["Action", "Documentary", "Musical", "Drama"], "answer": 0},
    {"question": "A film designed primarily to make the audience laugh belongs to which genre?",
     "options": ["Tragedy", "Comedy", "Western", "Noir"], "answer": 1},
    {"question": "Which genre focuses on serious, realistic stories and emotional character development?",
     "options": ["Slapstick", "Slasher", "Drama", "Heist"], "answer": 2},
    {"question": "Films intended to frighten or unsettle the audience, often featuring monsters or the supernatural, are what genre?",
     "options": ["Horror", "Romance", "Sports", "Biography"], "answer": 0},
    {"question": "Which genre is set in imagined futures, outer space, or involves advanced technology?",
     "options": ["Fantasy", "Western", "Science Fiction", "War"], "answer": 2},
    {"question": "Stories involving magic, mythical creatures, and imaginary worlds define which genre?",
     "options": ["Fantasy", "Crime", "Mystery", "Found Footage"], "answer": 0},
    {"question": "Which genre keeps audiences in suspense with tension, danger, and plot twists?",
     "options": ["Thriller", "Musical", "Silent Film", "Coming-of-age"], "answer": 0},
    {"question": "A story centered on a romantic relationship as its main plot is which genre?",
     "options": ["Romance", "Noir", "Disaster", "Adventure"], "answer": 0},
    {"question": "Which genre uses real footage and interviews to portray factual, non-fiction subjects?",
     "options": ["Mockumentary", "Documentary", "Biopic", "Anthology"], "answer": 1},
    {"question": "Movies made using drawings, CGI, or stop-motion instead of live actors are called what?",
     "options": ["Animation", "Silent Film", "Noir", "Found Footage"], "answer": 0},
    {"question": "A film where characters break into song and dance to advance the story is which genre?",
     "options": ["Western", "Musical", "War", "Crime"], "answer": 1},
    {"question": "Which genre is typically set in the American frontier with cowboys and outlaws?",
     "options": ["Western", "Adventure", "Sports", "Heist"], "answer": 0},
    {"question": "Films depicting combat and its impact on soldiers or civilians belong to which genre?",
     "options": ["War", "Romance", "Musical", "Sports"], "answer": 0},
    {"question": "A story built around solving a puzzling crime or unexplained event is which genre?",
     "options": ["Mystery", "Comedy", "Fantasy", "Musical"], "answer": 0},
    {"question": "Films centered on criminals, gangs, or illegal activity are classified as which genre?",
     "options": ["Crime", "Sports", "Fantasy", "Musical"], "answer": 0},
    {"question": "Which genre follows a hero on a journey, often to exotic or dangerous locations?",
     "options": ["Adventure", "Drama", "Noir", "Mockumentary"], "answer": 0},
    {"question": "A dramatized retelling of a real person's life story is called what?",
     "options": ["Biopic (Biography)", "Documentary", "Anthology", "Found Footage"], "answer": 0},
    {"question": "Films focused on athletes, teams, or competitions are which genre?",
     "options": ["Sports", "War", "Western", "Noir"], "answer": 0},
    {"question": "Which genre features characters with extraordinary powers fighting villains, often based on comics?",
     "options": ["Superhero", "Western", "Drama", "Mystery"], "answer": 0},
    {"question": "A stylish, cynical crime genre popular in the 1940s-50s, often shot in shadowy black-and-white, is called what?",
     "options": ["Film Noir", "Slasher", "Screwball", "Peplum"], "answer": 0},
    {"question": "Which subgenre of horror centers on a killer stalking and murdering a sequence of victims?",
     "options": ["Slasher", "Mockumentary", "Rom-com", "Heist"], "answer": 0},
    {"question": "A film presented as if it were amateur or documentary recordings discovered later is what style?",
     "options": ["Found Footage", "Silent Film", "Anthology", "Biopic"], "answer": 0},
    {"question": "A fictional documentary-style comedy that satirizes its subject is called what?",
     "options": ["Mockumentary", "Noir", "Peplum", "War Film"], "answer": 0},
    {"question": "Which genre blends romance and comedy, often following two people falling in love?",
     "options": ["Romantic Comedy (Rom-Com)", "Tragedy", "Slasher", "War"], "answer": 0},
    {"question": "A comedy with a cynical, morbid, or taboo edge is known as which type?",
     "options": ["Dark Comedy", "Musical", "Western", "Sports"], "answer": 0},
    {"question": "Which genre delves into a character's mental state, often blurring reality and perception?",
     "options": ["Psychological Thriller", "Adventure", "Musical", "Sports"], "answer": 0},
    {"question": "A film about a team planning and executing an elaborate robbery is which genre?",
     "options": ["Heist", "Fantasy", "Musical", "Biography"], "answer": 0},
    {"question": "Which genre depicts catastrophic events like earthquakes, floods, or asteroid impacts threatening large numbers of people?",
     "options": ["Disaster", "Romance", "Mystery", "Western"], "answer": 0},
    {"question": "A story following a young protagonist's growth from adolescence to adulthood is which genre?",
     "options": ["Coming-of-Age", "Noir", "Heist", "War"], "answer": 0},
    {"question": "Movies made before synchronized sound technology, relying on title cards and music, are called what?",
     "options": ["Silent Films", "Found Footage", "Mockumentary", "Anthology"], "answer": 0},
    {"question": "A film made up of several short, loosely connected stories is known as what?",
     "options": ["Anthology", "Biopic", "Slasher", "Peplum"], "answer": 0},
    {"question": "Which genre combines science fiction elements with horror to create fear through futuristic or alien threats?",
     "options": ["Sci-Fi Horror", "Musical", "Western", "Sports"], "answer": 0},
]

TOTAL_QUESTIONS = len(QUESTIONS)


@app.route("/")
def start():
    session.clear()
    return render_template("start.html", total=TOTAL_QUESTIONS)


@app.route("/begin", methods=["POST"])
def begin():
    session.clear()
    session["index"] = 1
    session["score"] = 0
    session["history"] = []
    return redirect(url_for("question", n=1))


@app.route("/question/<int:n>", methods=["GET"])
def question(n):
    if "index" not in session:
        return redirect(url_for("start"))

    current = session["index"]

    if n > TOTAL_QUESTIONS:
        return redirect(url_for("results"))

    # Don't allow jumping ahead of or behind the current question.
    if n != current:
        return redirect(url_for("question", n=current))

    q = QUESTIONS[n - 1]
    history = session.get("history", [])
    last_result = history[-1] if history else None

    return render_template(
        "question.html",
        q=q,
        n=n,
        total=TOTAL_QUESTIONS,
        score=session.get("score", 0),
        last_result=last_result,
    )


@app.route("/question/<int:n>", methods=["POST"])
def answer(n):
    if "index" not in session or n != session["index"]:
        return redirect(url_for("start"))

    q = QUESTIONS[n - 1]
    selected = request.form.get("option")
    is_correct = selected is not None and int(selected) == q["answer"]

    if is_correct:
        session["score"] = session.get("score", 0) + 1

    history = session.get("history", [])
    history.append({
        "question": q["question"],
        "options": q["options"],
        "chosen": int(selected) if selected is not None else None,
        "correct_index": q["answer"],
        "is_correct": is_correct,
    })
    session["history"] = history
    session["index"] = n + 1

    if n + 1 > TOTAL_QUESTIONS:
        return redirect(url_for("results"))
    return redirect(url_for("question", n=n + 1))


@app.route("/results")
def results():
    if "history" not in session or len(session.get("history", [])) < TOTAL_QUESTIONS:
        return redirect(url_for("start"))

    return render_template(
        "results.html",
        score=session.get("score", 0),
        total=TOTAL_QUESTIONS,
        history=session.get("history", []),
    )


if __name__ == "__main__":
    app.run(debug=True)

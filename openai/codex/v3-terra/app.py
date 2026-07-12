import os
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "change-this-for-production")


QUESTIONS = [
    {
        "question": "Which movie type is chiefly designed to make its audience laugh?",
        "options": ["Comedy", "Western", "Horror", "Documentary"],
        "answer": "Comedy",
        "fact": "Comedies use humour, timing, and comic situations as their main storytelling tools.",
    },
    {
        "question": "A film built around suspense, danger, and attempts to frighten the audience is usually a…",
        "options": ["Romance", "Musical", "Horror", "Biopic"],
        "answer": "Horror",
        "fact": "Horror films create fear through threats, atmosphere, and often the unknown.",
    },
    {
        "question": "Which genre usually features a central love story and emotional relationships?",
        "options": ["War", "Romance", "Sports", "Crime"],
        "answer": "Romance",
        "fact": "Romance films focus on the development and challenges of romantic relationships.",
    },
    {
        "question": "A movie set in a speculative future with advanced technology is most likely…",
        "options": ["Science fiction", "Historical drama", "Western", "Courtroom drama"],
        "answer": "Science fiction",
        "fact": "Science fiction explores imagined science, technology, space, or future societies.",
    },
    {
        "question": "What genre commonly includes cowboys, frontier towns, and life in the American West?",
        "options": ["Noir", "Western", "Fantasy", "Adventure"],
        "answer": "Western",
        "fact": "Westerns traditionally explore frontier life, conflict, and rugged landscapes.",
    },
    {
        "question": "A movie following a character through a dangerous journey in an unfamiliar place is often an…",
        "options": ["Adventure", "Animated film", "Satire", "Melodrama"],
        "answer": "Adventure",
        "fact": "Adventure films centre on quests, exploration, and high-stakes journeys.",
    },
    {
        "question": "Which type of movie tells its story primarily through drawn, stop-motion, or computer-generated imagery?",
        "options": ["Live concert film", "Animated film", "Mockumentary", "Thriller"],
        "answer": "Animated film",
        "fact": "Animation is a filmmaking medium, and animated films can also belong to other genres.",
    },
    {
        "question": "A non-fiction movie that investigates real people, events, or ideas is a…",
        "options": ["Documentary", "Fantasy", "Slasher", "Period drama"],
        "answer": "Documentary",
        "fact": "Documentaries aim to present or examine real-world subjects.",
    },
    {
        "question": "What genre usually involves a protagonist investigating a crime or solving a puzzle?",
        "options": ["Mystery", "Musical", "Coming-of-age", "Disaster"],
        "answer": "Mystery",
        "fact": "Mysteries revolve around hidden information that the viewer is encouraged to uncover.",
    },
    {
        "question": "A high-energy film focused on chases, fights, and physical stunts belongs most often to which genre?",
        "options": ["Action", "Romance", "Drama", "Documentary"],
        "answer": "Action",
        "fact": "Action films prioritise kinetic set pieces and physical conflict.",
    },
    {
        "question": "Which genre is commonly set in an invented world with magic, mythical beings, or supernatural rules?",
        "options": ["Fantasy", "Legal drama", "Biopic", "Sports"],
        "answer": "Fantasy",
        "fact": "Fantasy creates worlds or events beyond the limits of ordinary reality.",
    },
    {
        "question": "A movie in which songs and dance numbers are an important part of the storytelling is a…",
        "options": ["Musical", "Heist film", "Thriller", "Western"],
        "answer": "Musical",
        "fact": "Musicals use performance to express character, plot, or emotion.",
    },
    {
        "question": "Which genre often explores serious characters and emotionally weighty conflicts?",
        "options": ["Drama", "Parody", "Monster movie", "Road movie"],
        "answer": "Drama",
        "fact": "Dramas focus on character development and meaningful human conflict.",
    },
    {
        "question": "A film about a real person's life is known as a…",
        "options": ["Biopic", "Creature feature", "Whodunit", "Buddy comedy"],
        "answer": "Biopic",
        "fact": "Biopics dramatise the life of a real individual, sometimes with artistic licence.",
    },
    {
        "question": "Which movie type creates tension around an imminent threat, twist, or uncertain outcome?",
        "options": ["Thriller", "Musical", "Family film", "Western"],
        "answer": "Thriller",
        "fact": "Thrillers are designed to keep viewers anxious and eager to know what happens next.",
    },
    {
        "question": "A film that centres on criminal activity, police, or the justice system is often a…",
        "options": ["Crime film", "Fantasy", "Rom-com", "Nature film"],
        "answer": "Crime film",
        "fact": "Crime films can follow criminals, investigators, victims, or all three.",
    },
    {
        "question": "What genre uses exaggerated humour to imitate or poke fun at other works or conventions?",
        "options": ["Parody", "Epic", "War film", "Mystery"],
        "answer": "Parody",
        "fact": "Parody depends on the audience recognising the style or work being imitated.",
    },
    {
        "question": "A movie about soldiers and conflict during wartime belongs to the…",
        "options": ["War film", "Screwball comedy", "Fantasy", "Documentary"],
        "answer": "War film",
        "fact": "War films may depict combat, its consequences, or the lives shaped by war.",
    },
    {
        "question": "A film about characters competing in athletics is most accurately called a…",
        "options": ["Sports film", "Noir", "Musical", "Disaster film"],
        "answer": "Sports film",
        "fact": "Sports films often pair competition with an underdog, team, or personal-growth story.",
    },
    {
        "question": "Which genre mixes romantic storylines with comic situations?",
        "options": ["Romantic comedy", "Psychological horror", "Space opera", "Crime drama"],
        "answer": "Romantic comedy",
        "fact": "Romantic comedies balance relationship stakes with humour.",
    },
    {
        "question": "A film styled around shadowy visuals, moral ambiguity, and crime is frequently called…",
        "options": ["Film noir", "Animation", "A musical", "A western"],
        "answer": "Film noir",
        "fact": "Classic film noir is known for cynical characters, dramatic lighting, and crime-driven plots.",
    },
    {
        "question": "Which type of film recreates a past era as a major part of its setting and story?",
        "options": ["Period drama", "Mockumentary", "Superhero film", "Slapstick comedy"],
        "answer": "Period drama",
        "fact": "Period dramas use costumes, settings, and social details to evoke a specific historical time.",
    },
    {
        "question": "A movie in which heroes with extraordinary powers fight threats is a…",
        "options": ["Superhero film", "Nature documentary", "Whodunit", "Road movie"],
        "answer": "Superhero film",
        "fact": "Superhero films usually draw on comic-book traditions and larger-than-life powers.",
    },
    {
        "question": "What genre puts a group of characters in danger from a major catastrophe, such as an earthquake or flood?",
        "options": ["Disaster film", "Romance", "Biopic", "Satire"],
        "answer": "Disaster film",
        "fact": "Disaster films build drama around survival during large-scale calamity.",
    },
    {
        "question": "A movie that follows travellers as they move from place to place is often called a…",
        "options": ["Road movie", "Courtroom drama", "Ghost story", "Historical epic"],
        "answer": "Road movie",
        "fact": "Road movies use a journey to change the characters and reveal their relationships.",
    },
    {
        "question": "Which genre uses humour to expose or criticise social, political, or cultural problems?",
        "options": ["Satire", "Action", "Fantasy", "Adventure"],
        "answer": "Satire",
        "fact": "Satire can be playful or sharp, but it uses wit to comment on real issues.",
    },
    {
        "question": "A film in which characters plan and carry out a major theft is a…",
        "options": ["Heist film", "Coming-of-age film", "Musical", "War film"],
        "answer": "Heist film",
        "fact": "Heist films often emphasise planning, teamwork, obstacles, and reversals.",
    },
    {
        "question": "Which type of movie follows a young person's transition toward adulthood?",
        "options": ["Coming-of-age film", "Creature feature", "Noir", "Disaster film"],
        "answer": "Coming-of-age film",
        "fact": "Coming-of-age stories focus on identity, maturity, and formative experiences.",
    },
    {
        "question": "A movie that presents fictional events in the style of a documentary is a…",
        "options": ["Mockumentary", "Biopic", "Western", "Melodrama"],
        "answer": "Mockumentary",
        "fact": "Mockumentaries borrow documentary conventions to make fiction feel real, often for comedy.",
    },
    {
        "question": "A mystery structured around identifying which character committed a crime is commonly a…",
        "options": ["Whodunit", "Musical", "Sports film", "Romance"],
        "answer": "Whodunit",
        "fact": "Whodunits invite the audience to weigh clues and suspects alongside the investigator.",
    },
]


def reset_quiz():
    session["question_index"] = 0
    session["answers"] = []
    session["score"] = 0
    session.pop("last_response", None)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        reset_quiz()
        return redirect(url_for("question", number=1))
    return render_template("home.html", total_questions=len(QUESTIONS))


@app.route("/question/<int:number>", methods=["GET", "POST"])
def question(number):
    # Let a visitor safely begin from a bookmarked first question, but do not
    # allow direct URLs to skip earlier questions.
    if "question_index" not in session:
        if number != 1:
            return redirect(url_for("home"))
        reset_quiz()

    expected_number = session.get("question_index", 0) + 1
    if number != expected_number:
        return redirect(url_for("question", number=expected_number)) if expected_number <= len(QUESTIONS) else redirect(url_for("results"))

    current = QUESTIONS[number - 1]
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice not in current["options"]:
            return render_template(
                "question.html",
                question=current,
                number=number,
                total_questions=len(QUESTIONS),
                last_response=session.get("last_response"),
                error="Please choose an answer before continuing.",
            )

        correct = choice == current["answer"]
        # Keep the signed cookie session small; the static question catalogue is
        # used again on the results page to show the question and correct answer.
        session["answers"].append({
            "number": number,
            "choice": choice,
            "correct": correct,
        })
        session["score"] = session.get("score", 0) + int(correct)
        session["question_index"] = number
        session["last_response"] = {
            "number": number,
            "choice": choice,
            "correct": correct,
            "answer": current["answer"],
            "fact": current["fact"],
        }
        session.modified = True

        if number == len(QUESTIONS):
            return redirect(url_for("results"))
        return redirect(url_for("question", number=number + 1))

    return render_template(
        "question.html",
        question=current,
        number=number,
        total_questions=len(QUESTIONS),
        last_response=session.get("last_response"),
    )


@app.route("/results")
def results():
    if session.get("question_index", 0) < len(QUESTIONS):
        return redirect(url_for("question", number=session.get("question_index", 0) + 1))
    return render_template(
        "results.html",
        answers=session.get("answers", []),
        questions=QUESTIONS,
        score=session.get("score", 0),
        total_questions=len(QUESTIONS),
    )


@app.post("/restart")
def restart():
    reset_quiz()
    return redirect(url_for("question", number=1))


if __name__ == "__main__":
    app.run(debug=True)

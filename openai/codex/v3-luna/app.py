import os
from datetime import datetime, timezone

from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")


QUESTIONS = [
    {
        "prompt": "Which movie type is built around heroes, villains, and extraordinary powers?",
        "category": "Genre basics",
        "choices": ["Superhero", "Documentary", "Romance", "Western"],
        "answer": "Superhero",
        "explanation": "Superhero films center on characters with unusual abilities, costumes, or heroic missions.",
    },
    {
        "prompt": "A film about cowboys, frontier towns, and life in the American West is usually a…",
        "category": "Genre basics",
        "choices": ["Western", "Musical", "Sports film", "Thriller"],
        "answer": "Western",
        "explanation": "Westerns use frontier settings and often explore law, survival, justice, and changing communities.",
    },
    {
        "prompt": "Which movie type is designed primarily to make the audience laugh?",
        "category": "Genre basics",
        "choices": ["Comedy", "Horror", "War film", "Mystery"],
        "answer": "Comedy",
        "explanation": "Comedy uses humor, comic situations, and playful characters as its main source of entertainment.",
    },
    {
        "prompt": "Stories focused on a relationship developing between two people are typically what type?",
        "category": "Genre basics",
        "choices": ["Romance", "Action", "Disaster", "Biopic"],
        "answer": "Romance",
        "explanation": "Romance films make the emotional relationship between their central characters the main story.",
    },
    {
        "prompt": "Which movie type aims to frighten, unsettle, or disturb its audience?",
        "category": "Genre basics",
        "choices": ["Horror", "Coming-of-age", "Musical", "Historical epic"],
        "answer": "Horror",
        "explanation": "Horror is built around fear and suspense, often using monsters, the supernatural, or psychological threats.",
    },
    {
        "prompt": "A film where characters break into song and dance as part of the story is a…",
        "category": "Genre basics",
        "choices": ["Musical", "Noir", "War film", "Mockumentary"],
        "answer": "Musical",
        "explanation": "Musicals weave songs, choreography, and often spoken scenes into one cinematic narrative.",
    },
    {
        "prompt": "Which type of film follows a real person’s life, usually with actors portraying key events?",
        "category": "Genre basics",
        "choices": ["Biopic", "Fantasy", "Slasher", "Heist film"],
        "answer": "Biopic",
        "explanation": "A biopic dramatizes the life of a real person, though filmmakers may condense or reshape events.",
    },
    {
        "prompt": "A movie centered on solving a crime or discovering who committed it is a…",
        "category": "Genre basics",
        "choices": ["Mystery", "Rom-com", "Sports film", "Epic"],
        "answer": "Mystery",
        "explanation": "Mysteries invite viewers to follow clues and uncover hidden information alongside the characters.",
    },
    {
        "prompt": "Which movie type usually follows a protagonist trying to complete a dangerous physical mission?",
        "category": "Genre basics",
        "choices": ["Action", "Documentary", "Romance", "Slice of life"],
        "answer": "Action",
        "explanation": "Action films emphasize movement, stunts, fights, chases, and high-stakes physical challenges.",
    },
    {
        "prompt": "A film set during a major real-world conflict and focused on soldiers or civilians is a…",
        "category": "Genre basics",
        "choices": ["War film", "Fantasy", "Comedy", "Road movie"],
        "answer": "War film",
        "explanation": "War films dramatize the experiences and consequences of armed conflict, on or away from the battlefield.",
    },
    {
        "prompt": "Which type of movie is set in an invented world with magic, mythical creatures, or impossible rules?",
        "category": "Worlds & stories",
        "choices": ["Fantasy", "Noir", "Biopic", "Courtroom drama"],
        "answer": "Fantasy",
        "explanation": "Fantasy films build stories around imaginative worlds and elements that do not follow ordinary reality.",
    },
    {
        "prompt": "A story involving advanced technology, space travel, or imagined futures belongs to…",
        "category": "Worlds & stories",
        "choices": ["Science fiction", "Western", "Romance", "Musical"],
        "answer": "Science fiction",
        "explanation": "Science fiction explores speculative science, technology, societies, and futures—or alternate presents.",
    },
    {
        "prompt": "Which type of movie follows a character’s transition from childhood toward adulthood?",
        "category": "Worlds & stories",
        "choices": ["Coming-of-age", "Disaster film", "Heist film", "Superhero"],
        "answer": "Coming-of-age",
        "explanation": "Coming-of-age stories focus on growing up, forming an identity, and gaining independence.",
    },
    {
        "prompt": "A group planning and carrying out a robbery is the classic setup for a…",
        "category": "Worlds & stories",
        "choices": ["Heist film", "Period romance", "Sports film", "Horror comedy"],
        "answer": "Heist film",
        "explanation": "Heist films turn a carefully planned theft into a story about teamwork, deception, and risk.",
    },
    {
        "prompt": "Which movie type often uses morally complicated characters, shadows, and a cynical city atmosphere?",
        "category": "Worlds & stories",
        "choices": ["Film noir", "Musical", "Fantasy", "Documentary"],
        "answer": "Film noir",
        "explanation": "Film noir is known for fatalism, moral ambiguity, crime, and a distinctive low-key visual style.",
    },
    {
        "prompt": "A film about a team or individual competing in a sporting event is a…",
        "category": "Worlds & stories",
        "choices": ["Sports film", "Mystery", "Western", "Kaiju film"],
        "answer": "Sports film",
        "explanation": "Sports films use competition to explore ambition, discipline, teamwork, failure, and redemption.",
    },
    {
        "prompt": "Which type of movie uses real footage, interviews, or observation to explore a subject?",
        "category": "Worlds & stories",
        "choices": ["Documentary", "Slasher", "Rom-com", "Action"],
        "answer": "Documentary",
        "explanation": "Documentaries present nonfiction stories using real people, events, evidence, and filmmaking choices.",
    },
    {
        "prompt": "A movie built around a large-scale catastrophe such as an earthquake or tidal wave is a…",
        "category": "Worlds & stories",
        "choices": ["Disaster film", "Biopic", "Noir", "Coming-of-age"],
        "answer": "Disaster film",
        "explanation": "Disaster films put characters in the path of a large-scale crisis and focus on survival and response.",
    },
    {
        "prompt": "Which movie type deliberately imitates a documentary while presenting fictional events?",
        "category": "Formats & hybrids",
        "choices": ["Mockumentary", "Historical epic", "Thriller", "Fantasy"],
        "answer": "Mockumentary",
        "explanation": "A mockumentary uses documentary conventions—such as interviews or handheld footage—for comedy or satire.",
    },
    {
        "prompt": "A funny film focused on a couple falling in love is commonly called a…",
        "category": "Formats & hybrids",
        "choices": ["Rom-com", "War film", "Psychological horror", "Road movie"],
        "answer": "Rom-com",
        "explanation": "Rom-com is short for romantic comedy: a blend of relationship-focused storytelling and humor.",
    },
    {
        "prompt": "Which hybrid genre mixes frightening situations with jokes and comic timing?",
        "category": "Formats & hybrids",
        "choices": ["Horror comedy", "Historical drama", "Sports film", "Space opera"],
        "answer": "Horror comedy",
        "explanation": "Horror comedies intentionally let fear and humor play off each other, sometimes switching tone rapidly.",
    },
    {
        "prompt": "A movie that follows a journey from one place to another, with the travel shaping the story, is a…",
        "category": "Formats & hybrids",
        "choices": ["Road movie", "Heist film", "Biopic", "Slasher"],
        "answer": "Road movie",
        "explanation": "Road movies use travel as a structure for encounters, personal change, and a shifting sense of home.",
    },
    {
        "prompt": "Which type of film usually keeps tension high through danger, uncertainty, and anticipation?",
        "category": "Formats & hybrids",
        "choices": ["Thriller", "Musical", "Documentary", "Western"],
        "answer": "Thriller",
        "explanation": "Thrillers are designed to create suspense and keep viewers wondering what will happen next.",
    },
    {
        "prompt": "A film that recreates a past era with period costumes, settings, and customs is often a…",
        "category": "Formats & hybrids",
        "choices": ["Historical drama", "Superhero film", "Mockumentary", "Rom-com"],
        "answer": "Historical drama",
        "explanation": "Historical dramas use the past as their setting, combining researched details with dramatic storytelling.",
    },
    {
        "prompt": "Which type of horror film is especially associated with a masked or relentless killer stalking victims?",
        "category": "Formats & hybrids",
        "choices": ["Slasher", "Fantasy", "War film", "Courtroom drama"],
        "answer": "Slasher",
        "explanation": "Slashers typically feature a killer, a group of potential victims, and escalating pursuit or attacks.",
    },
    {
        "prompt": "A story about giant creatures attacking cities is often described as a…",
        "category": "Formats & hybrids",
        "choices": ["Kaiju film", "Film noir", "Biopic", "Coming-of-age film"],
        "answer": "Kaiju film",
        "explanation": "Kaiju is a Japanese term for giant monster; the genre often pairs spectacle with fears about nature or technology.",
    },
    {
        "prompt": "Which type of movie often presents a huge, sweeping adventure across many locations and years?",
        "category": "Formats & hybrids",
        "choices": ["Epic", "Mockumentary", "Slasher", "Slice-of-life"],
        "answer": "Epic",
        "explanation": "Epics use broad scale, memorable settings, and major stakes to tell expansive stories.",
    },
    {
        "prompt": "A quiet film focused on ordinary routines and small, realistic moments is a…",
        "category": "Formats & hybrids",
        "choices": ["Slice-of-life film", "Action film", "Disaster film", "Space opera"],
        "answer": "Slice-of-life film",
        "explanation": "Slice-of-life films find meaning in everyday experiences rather than extraordinary plot events.",
    },
    {
        "prompt": "Which movie type is centered on legal arguments, evidence, and a case in court?",
        "category": "Formats & hybrids",
        "choices": ["Courtroom drama", "Fantasy", "Road movie", "Musical"],
        "answer": "Courtroom drama",
        "explanation": "Courtroom dramas build their conflict around trials, lawyers, testimony, and competing versions of the truth.",
    },
    {
        "prompt": "A film combining starships, planets, adventure, and a grand conflict is often called a…",
        "category": "Formats & hybrids",
        "choices": ["Space opera", "Western", "Rom-com", "Documentary"],
        "answer": "Space opera",
        "explanation": "Space opera is a large-scale science-fiction adventure with sweeping characters, worlds, and conflicts.",
    },
]


def new_quiz_state():
    return {
        "current": 0,
        "score": 0,
        "answers": [],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "last_result": None,
    }


@app.context_processor
def inject_quiz_meta():
    return {"total_questions": len(QUESTIONS)}


@app.get("/")
def home():
    active = "quiz" in session
    return render_template("home.html", active=active)


@app.post("/start")
def start():
    session["quiz"] = new_quiz_state()
    session.modified = True
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz_state = session.get("quiz")
    if not quiz_state:
        return redirect(url_for("home"))

    current = quiz_state.get("current", 0)
    if current >= len(QUESTIONS):
        return redirect(url_for("results"))

    question = QUESTIONS[current]
    if request.method == "POST":
        selected = request.form.get("answer", "")
        if selected not in question["choices"]:
            flash("Choose an answer before continuing.", "error")
            return render_template("quiz.html", question=question, number=current + 1, state=quiz_state)

        is_correct = selected == question["answer"]
        result = {"selected": selected, "is_correct": is_correct}
        # Keep the signed cookie small: the full review is rebuilt from QUESTIONS below.
        quiz_state["answers"].append(question["choices"].index(selected))
        quiz_state["score"] += int(is_correct)
        quiz_state["current"] = current + 1
        quiz_state["last_result"] = result
        session["quiz"] = quiz_state
        session.modified = True

        if quiz_state["current"] >= len(QUESTIONS):
            return redirect(url_for("results"))
        return redirect(url_for("quiz"))

    return render_template("quiz.html", question=question, number=current + 1, state=quiz_state)


@app.get("/results")
def results():
    quiz_state = session.get("quiz")
    if not quiz_state:
        return redirect(url_for("home"))
    if quiz_state.get("current", 0) < len(QUESTIONS):
        return redirect(url_for("quiz"))

    score = quiz_state["score"]
    percentage = round(score / len(QUESTIONS) * 100)
    if percentage >= 90:
        verdict = "Genre virtuoso"
        verdict_copy = "You can spot a movie type from a single frame of its trailer."
    elif percentage >= 70:
        verdict = "Sharp-eyed cinephile"
        verdict_copy = "Your genre instincts are strong, with only a few plot twists along the way."
    elif percentage >= 50:
        verdict = "Rising film fan"
        verdict_copy = "You have a solid foundation—there are plenty of great genres left to discover."
    else:
        verdict = "Curious newcomer"
        verdict_copy = "Every wrong answer is a new movie night waiting to happen."

    answers = []
    category_scores = {}
    for number, answer_index in enumerate(quiz_state["answers"], start=1):
        question = QUESTIONS[number - 1]
        selected = question["choices"][answer_index]
        answer = {
            "number": number,
            "prompt": question["prompt"],
            "selected": selected,
            "correct": question["answer"],
            "is_correct": selected == question["answer"],
            "category": question["category"],
            "explanation": question["explanation"],
        }
        answers.append(answer)
        category = question["category"]
        category_scores.setdefault(category, {"score": 0, "total": 0})
        category_scores[category]["total"] += 1
        category_scores[category]["score"] += int(answer["is_correct"])

    return render_template(
        "results.html",
        state=quiz_state,
        score=score,
        percentage=percentage,
        verdict=verdict,
        verdict_copy=verdict_copy,
        category_scores=category_scores,
        answers=answers,
    )


@app.post("/restart")
def restart():
    session.pop("quiz", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

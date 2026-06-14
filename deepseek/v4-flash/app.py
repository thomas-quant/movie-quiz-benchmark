from flask import Flask, session, request, redirect, url_for, render_template
import random

app = Flask(__name__)
app.secret_key = "movie_quiz_secret_key_2024"

QUESTIONS = [
    {
        "question": "Which genre typically features cowboys, saloons, and duels at high noon?",
        "options": ["Western", "Action", "Adventure", "Historical"],
        "answer": "Western",
    },
    {
        "question": "What genre is designed specifically to frighten, shock, or disgust its audience?",
        "options": ["Thriller", "Horror", "Mystery", "Psychological Drama"],
        "answer": "Horror",
    },
    {
        "question": "Which genre relies on humor, jokes, and amusing situations as its primary draw?",
        "options": ["Satire", "Farce", "Comedy", "Slapstick"],
        "answer": "Comedy",
    },
    {
        "question": "A serious, character-driven genre focused on realistic emotional conflict is called?",
        "options": ["Melodrama", "Drama", "Tragedy", "Realism"],
        "answer": "Drama",
    },
    {
        "question": "Which genre explores futuristic technology, space exploration, or speculative science?",
        "options": ["Fantasy", "Science Fiction", "Futurism", "Tech Noir"],
        "answer": "Science Fiction",
    },
    {
        "question": "What genre centers on love, emotional attachment, and romantic relationships?",
        "options": ["Romance", "Drama", "Erotica", "Soap Opera"],
        "answer": "Romance",
    },
    {
        "question": "Which genre uses suspense, tension, and excitement as its core emotional drivers?",
        "options": ["Horror", "Action", "Thriller", "Mystery"],
        "answer": "Thriller",
    },
    {
        "question": "A genre defined by explosive stunts, fight scenes, and high-energy set pieces is?",
        "options": ["Adventure", "Action", "Martial Arts", "Blockbuster"],
        "answer": "Action",
    },
    {
        "question": "Which non-fiction genre aims to capture real events, people, and places?",
        "options": ["Biopic", "Documentary", "Newsreel", "Reality"],
        "answer": "Documentary",
    },
    {
        "question": "What genre involves magic, mythical creatures, or supernatural elements?",
        "options": ["Science Fiction", "Superhero", "Fantasy", "Folklore"],
        "answer": "Fantasy",
    },
    {
        "question": "A genre where characters break into song and dance as part of the storytelling is?",
        "options": ["Opera", "Musical", "Concert Film", "Variety"],
        "answer": "Musical",
    },
    {
        "question": "Which genre encompasses films made frame-by-frame rather than live-action recording?",
        "options": ["VFX", "Animation", "Motion Capture", "CGI"],
        "answer": "Animation",
    },
    {
        "question": "A genre centered on solving a crime, puzzle, or unexplained event is?",
        "options": ["Thriller", "Mystery", "Detective", "Noir"],
        "answer": "Mystery",
    },
    {
        "question": "Which genre involves heroic journeys, exploration, and high-stakes discovery?",
        "options": ["Action", "Epic", "Adventure", "Quest"],
        "answer": "Adventure",
    },
    {
        "question": "A style characterized by cynical protagonists, shadowy visuals, and moral ambiguity is?",
        "options": ["Neo-noir", "Film Noir", "German Expressionism", "Gothic"],
        "answer": "Film Noir",
    },
    {
        "question": "Which genre features costumed vigilantes with extraordinary powers or advanced tech?",
        "options": ["Action", "Superhero", "Fantasy", "Martial Arts"],
        "answer": "Superhero",
    },
    {
        "question": "A horror subgenre where a masked killer systematically hunts victims is?",
        "options": ["Slasher", "Psychological Horror", "Found Footage", "Gothic Horror"],
        "answer": "Slasher",
    },
    {
        "question": "Which hybrid genre blends romantic plots with comedic tone and structure?",
        "options": ["Romantic Drama", "Rom-Com", "Comedy of Manners", "Screwball"],
        "answer": "Rom-Com",
    },
    {
        "question": "A film that dramatizes the real-life story of a historical figure is a?",
        "options": ["Documentary", "Biopic", "Historical Drama", "Docudrama"],
        "answer": "Biopic",
    },
    {
        "question": "Which genre is set in a specific period of the past with period-accurate detail?",
        "options": ["Historical", "Period Piece", "Epic", "Heritage Film"],
        "answer": "Historical",
    },
    {
        "question": "A genre focusing on armed conflict, military strategy, and the realities of war is?",
        "options": ["Action", "War", "Historical", "Patriotic"],
        "answer": "War",
    },
    {
        "question": "Which genre revolves around organized crime, heists, or law enforcement?",
        "options": ["Mystery", "Crime", "Thriller", "Gangster"],
        "answer": "Crime",
    },
    {
        "question": "A genre centered on large-scale catastrophes like earthquakes or asteroid impacts is?",
        "options": ["Action", "Disaster", "Survival", "Apocalyptic"],
        "answer": "Disaster",
    },
    {
        "question": "Which genre showcases choreographed hand-to-hand combat and fighting styles?",
        "options": ["Action", "Martial Arts", "Wuxia", "Kung Fu"],
        "answer": "Martial Arts",
    },
    {
        "question": "A thriller subgenre that delves into the unstable minds of its characters is?",
        "options": ["Psychological Thriller", "Mindbender", "Psychodrama", "Dark Mystery"],
        "answer": "Psychological Thriller",
    },
    {
        "question": "Which genre finds humor in grim, taboo, or morbid subject matter?",
        "options": ["Black Comedy", "Dark Comedy", "Satire", "Cringe Comedy"],
        "answer": "Dark Comedy",
    },
    {
        "question": "A genre tracking a protagonist's journey from youth into adulthood is?",
        "options": ["Coming of Age", "Teen Drama", " Bildungsroman", "Youth Film"],
        "answer": "Coming of Age",
    },
    {
        "question": "Which genre presents fictional events in the style of a non-fiction documentary?",
        "options": ["Reality TV", "Docudrama", "Mockumentary", "Found Footage"],
        "answer": "Mockumentary",
    },
    {
        "question": "A revival of classic noir tropes with modern sensibilities and color cinematography is?",
        "options": ["Neo-noir", "Post-noir", "Tech Noir", "Modern Noir"],
        "answer": "Neo-noir",
    },
    {
        "question": "Which genre uses exaggerated, absurd situations for comedic or satirical effect?",
        "options": ["Slapstick", "Farce", "Parody", "Absurdism"],
        "answer": "Farce",
    },
    {
        "question": "A genre with sweeping scope, often covering decades or vast historical events is?",
        "options": ["Historical", "Epic", "Saga", "Blockbuster"],
        "answer": "Epic",
    },
    {
        "question": "Which genre uses humor, irony, and exaggeration to criticize politics or society?",
        "options": ["Parody", "Satire", "Dark Comedy", "Editorial"],
        "answer": "Satire",
    },
    {
        "question": "A film with no spoken dialogue where meaning is conveyed entirely through visuals is?",
        "options": ["Visual Essay", "Mime Film", "Silent Film", "Avant-Garde"],
        "answer": "Silent Film",
    },
    {
        "question": "Which genre focuses on court cases, lawyers, and the justice system?",
        "options": ["Crime", "Legal Drama", "Courtroom Drama", "Procedural"],
        "answer": "Courtroom Drama",
    },
]

TOTAL_QUESTIONS = len(QUESTIONS)


def get_question_order():
    if "order" not in session:
        order = list(range(TOTAL_QUESTIONS))
        random.shuffle(order)
        session["order"] = order
    return session["order"]


@app.route("/")
def index():
    session.clear()
    return render_template("index.html", total=TOTAL_QUESTIONS)


@app.route("/quiz/<int:qid>", methods=["GET", "POST"])
def question(qid):
    order = get_question_order()
    if qid < 0 or qid >= TOTAL_QUESTIONS:
        return redirect(url_for("result"))

    question_index = order[qid]
    q = QUESTIONS[question_index]

    if request.method == "POST":
        selected = request.form.get("answer")
        session.setdefault("answers", {})[str(qid)] = selected
        session.modified = True
        next_qid = qid + 1
        if next_qid >= TOTAL_QUESTIONS:
            return redirect(url_for("result"))
        return redirect(url_for("question", qid=next_qid))

    return render_template(
        "question.html",
        qid=qid,
        question=q["question"],
        options=q["options"],
        total=TOTAL_QUESTIONS,
        progress=qid + 1,
    )


@app.route("/result")
def result():
    order = get_question_order()
    answers = session.get("answers", {})
    score = 0
    results = []
    for i in range(TOTAL_QUESTIONS):
        q = QUESTIONS[order[i]]
        selected = answers.get(str(i))
        correct = selected == q["answer"]
        if correct:
            score += 1
        results.append(
            {
                "question": q["question"],
                "options": q["options"],
                "correct": q["answer"],
                "selected": selected,
                "is_correct": correct,
            }
        )
    return render_template(
        "result.html",
        results=results,
        score=score,
        total=TOTAL_QUESTIONS,
        percentage=round(score / TOTAL_QUESTIONS * 100),
    )


if __name__ == "__main__":
    app.run(debug=True)

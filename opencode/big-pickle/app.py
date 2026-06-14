from flask import Flask, session, request, render_template, redirect, url_for
import os
import uuid

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", uuid.uuid4().hex)

QUESTIONS = [
    {
        "q": "Which movie genre is defined by its primary goal of making the audience laugh?",
        "options": ["Comedy", "Drama", "Thriller", "Musical"],
        "answer": "Comedy",
    },
    {
        "q": "Films that use futuristic technology, space travel, or advanced science as key plot elements belong to which genre?",
        "options": ["Fantasy", "Science Fiction", "Adventure", "Action"],
        "answer": "Science Fiction",
    },
    {
        "q": "What genre focuses on emotional character development and realistic conflicts?",
        "options": ["Comedy", "Action", "Drama", "Horror"],
        "answer": "Drama",
    },
    {
        "q": "Which genre aims to evoke fear, dread, or terror in its audience?",
        "options": ["Thriller", "Horror", "Mystery", "Suspense"],
        "answer": "Horror",
    },
    {
        "q": "A movie where characters sing and dance as part of the storytelling belongs to which genre?",
        "options": ["Opera", "Musical", "Rom-Com", "Dance"],
        "answer": "Musical",
    },
    {
        "q": "Which genre centers around a romantic relationship between two or more characters?",
        "options": ["Drama", "Romance", "Comedy", "Slice of Life"],
        "answer": "Romance",
    },
    {
        "q": "Films drawn by hand or created with computer graphics rather than live-action belong to which genre?",
        "options": ["Animated", "Visual Effects", "CGI", "Fantasy"],
        "answer": "Animated",
    },
    {
        "q": "Which genre is set in the American frontier and often features cowboys and gunfights?",
        "options": ["Western", "Adventure", "Historical", "Action"],
        "answer": "Western",
    },
    {
        "q": "A non-fiction film that documents reality for educational or historical purposes is called what?",
        "options": ["Biopic", "Documentary", "Docudrama", "Newsreel"],
        "answer": "Documentary",
    },
    {
        "q": "Which genre involves the resolution of a crime, often featuring detectives or amateur sleuths?",
        "options": ["Thriller", "Crime", "Mystery", "Suspense"],
        "answer": "Mystery",
    },
    {
        "q": "Which genre is characterized by suspense, tension, and excitement, often with a protagonist in danger?",
        "options": ["Horror", "Action", "Thriller", "Adventure"],
        "answer": "Thriller",
    },
    {
        "q": "Films set in a specific historical period that recreate the era's look and feel belong to which genre?",
        "options": ["Period Piece", "Documentary", "Drama", "Epic"],
        "answer": "Period Piece",
    },
    {
        "q": "Which genre features worlds with magic, mythical creatures, and supernatural elements?",
        "options": ["Science Fiction", "Fantasy", "Supernatural", "Mythology"],
        "answer": "Fantasy",
    },
    {
        "q": "A film centered on a battle between nations, often depicting combat or its aftermath, is which genre?",
        "options": ["Action", "War", "Historical", "Epic"],
        "answer": "War",
    },
    {
        "q": "Which genre focuses on a protagonist's journey into unknown territory, often with survival elements?",
        "options": ["Action", "Adventure", "Thriller", "Exploration"],
        "answer": "Adventure",
    },
    {
        "q": "Films that explore psychological states with surreal or non-linear narratives are what genre?",
        "options": ["Psychological", "Art House", "Experimental", "Thriller"],
        "answer": "Psychological",
    },
    {
        "q": "A film that tells a story through visuals with little to no dialogue, popular in the early 20th century, is called?",
        "options": ["Mime", "Silent", "Visual", "Experimental"],
        "answer": "Silent",
    },
    {
        "q": "Which genre involves a protagonist maturing from youth to adulthood, dealing with identity struggles?",
        "options": ["Drama", "Coming-of-Age", "Slice of Life", "Teen"],
        "answer": "Coming-of-Age",
    },
    {
        "q": "Films that focus on the planning and execution of a theft or robbery belong to which genre?",
        "options": ["Crime", "Heist", "Action", "Thriller"],
        "answer": "Heist",
    },
    {
        "q": "Which genre combines comedy and romance into a single narrative?",
        "options": ["Romantic Comedy", "Comedy-Drama", "Romance", "Satire"],
        "answer": "Romantic Comedy",
    },
    {
        "q": "A subgenre where a mysterious death is investigated, leading to a final revelation of the culprit, is called what?",
        "options": ["Mystery", "Crime Drama", "Whodunit", "Detective"],
        "answer": "Whodunit",
    },
    {
        "q": "Which genre features courtroom proceedings as the central plot device?",
        "options": ["Legal Drama", "Crime", "Drama", "Mystery"],
        "answer": "Legal Drama",
    },
    {
        "q": "Films that exaggerate characters and situations for satirical or outrageous comedic effect are what genre?",
        "options": ["Parody", "Satire", "Comedy", "Farce"],
        "answer": "Parody",
    },
    {
        "q": "Which genre centers around the lives of gangsters and organized crime?",
        "options": ["Crime Drama", "Thriller", "Gangster", "Action"],
        "answer": "Gangster",
    },
    {
        "q": "Films where the main character discovers and explores a hidden or parallel world belong to which subgenre?",
        "options": ["Portal Fantasy", "Parallel Realms", "Fantasy", "Alternate History"],
        "answer": "Portal Fantasy",
    },
    {
        "q": "Which genre is known for its stylized black-and-white aesthetic and morally ambiguous characters?",
        "options": ["German Expressionism", "Film Noir", "Neo-Noir", "Gothic"],
        "answer": "Film Noir",
    },
    {
        "q": "A genre that blends advanced technology with dystopian, high-tech settings is called what?",
        "options": ["Cyberpunk", "Science Fiction", "Dystopian", "Tech Noir"],
        "answer": "Cyberpunk",
    },
    {
        "q": "Which genre focuses on the exploits of secret agents and international espionage?",
        "options": ["Spy", "Thriller", "Action", "Political"],
        "answer": "Spy",
    },
    {
        "q": "Films that follow characters during a long journey, often with comedic or dramatic undertones, are called what?",
        "options": ["Travelogue", "Road Movie", "Adventure", "Journey"],
        "answer": "Road Movie",
    },
    {
        "q": "Which genre is defined by fast-paced editing, high-energy soundtrack, and stylized violence?",
        "options": ["Action", "MTV-style", "Hyperkinetic", "Adrenaline"],
        "answer": "Action",
    },
    {
        "q": "A biographical film that dramatizes the life of a real person is called what?",
        "options": ["Documentary", "Biopic", "Historical Drama", "Docudrama"],
        "answer": "Biopic",
    },
    {
        "q": "Which genre combines elements of science fiction and horror, often involving mutation or body modification?",
        "options": ["Body Horror", "Sci-Fi Horror", "Biopunk", "Gross-Out"],
        "answer": "Body Horror",
    },
]


@app.route("/")
def index():
    session.clear()
    return render_template("index.html", total=len(QUESTIONS))


@app.route("/quiz/<int:qid>", methods=["GET", "POST"])
def quiz(qid):
    if qid < 0 or qid >= len(QUESTIONS):
        return redirect(url_for("result"))

    if "answers" not in session:
        session["answers"] = {}

    if request.method == "POST":
        chosen = request.form.get("option")
        if chosen:
            answers = dict(session["answers"])
            answers[str(qid)] = chosen
            session["answers"] = answers
            session.modified = True
            return redirect(url_for("quiz", qid=qid + 1))

    qdata = QUESTIONS[qid]
    prev_answer = session["answers"].get(str(qid - 1)) if qid > 0 else None

    return render_template(
        "quiz.html",
        question=qdata["q"],
        options=qdata["options"],
        qid=qid,
        total=len(QUESTIONS),
        progress=(qid / len(QUESTIONS)) * 100,
        prev_answer=prev_answer,
    )


@app.route("/result")
def result():
    answers = session.get("answers", {})
    if not answers:
        return redirect(url_for("index"))

    score = 0
    results = []
    for i, q in enumerate(QUESTIONS):
        chosen = answers.get(str(i))
        correct = chosen == q["answer"]
        if correct:
            score += 1
        results.append(
            {
                "question": q["q"],
                "chosen": chosen,
                "correct": q["answer"],
                "is_correct": correct,
            }
        )

    return render_template(
        "result.html",
        score=score,
        total=len(QUESTIONS),
        results=results,
        pct=round((score / len(QUESTIONS)) * 100),
    )


if __name__ == "__main__":
    app.run(debug=True, port=3000)

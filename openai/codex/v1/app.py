import os

from flask import Flask, redirect, render_template, request, session, url_for


QUESTIONS = [
    {
        "category": "Action",
        "prompt": "Which movie type is built around chases, fights, stunts, and high physical danger?",
        "options": ["Action", "Romantic comedy", "Biographical drama", "Musical"],
        "answer": "Action",
        "explanation": "Action films use physical conflict and momentum as the main attraction.",
    },
    {
        "category": "Comedy",
        "prompt": "Which type of movie is primarily designed to make the audience laugh?",
        "options": ["Comedy", "Noir", "War film", "Documentary"],
        "answer": "Comedy",
        "explanation": "Comedies organize scenes, characters, and timing around humor.",
    },
    {
        "category": "Drama",
        "prompt": "Which movie type focuses on serious character conflict and emotional stakes?",
        "options": ["Drama", "Slapstick", "Sports film", "Monster movie"],
        "answer": "Drama",
        "explanation": "Dramas emphasize character choices, relationships, and consequences.",
    },
    {
        "category": "Horror",
        "prompt": "Which movie type tries to frighten, unsettle, or shock the audience?",
        "options": ["Horror", "Buddy comedy", "Historical epic", "Dance film"],
        "answer": "Horror",
        "explanation": "Horror films create fear through threat, suspense, atmosphere, or violence.",
    },
    {
        "category": "Science fiction",
        "prompt": "Which movie type often explores futuristic technology, space travel, or alternate scientific possibilities?",
        "options": ["Science fiction", "Western", "Courtroom drama", "Road movie"],
        "answer": "Science fiction",
        "explanation": "Science fiction asks 'what if' questions about science, technology, and society.",
    },
    {
        "category": "Fantasy",
        "prompt": "Which movie type usually features magic, invented worlds, mythical beings, or supernatural quests?",
        "options": ["Fantasy", "Political thriller", "Mockumentary", "Gangster film"],
        "answer": "Fantasy",
        "explanation": "Fantasy films rely on magical or mythical elements that do not need scientific grounding.",
    },
    {
        "category": "Mystery",
        "prompt": "Which movie type centers on solving a puzzle, crime, disappearance, or hidden truth?",
        "options": ["Mystery", "Musical", "Disaster film", "Teen comedy"],
        "answer": "Mystery",
        "explanation": "Mysteries withhold information and invite the audience to solve the case.",
    },
    {
        "category": "Thriller",
        "prompt": "Which movie type is driven by suspense, danger, tension, and urgent uncertainty?",
        "options": ["Thriller", "Slice-of-life drama", "Parody", "Concert film"],
        "answer": "Thriller",
        "explanation": "Thrillers keep pressure high by making outcomes feel immediate and risky.",
    },
    {
        "category": "Romance",
        "prompt": "Which movie type places a love relationship at the center of the story?",
        "options": ["Romance", "Heist film", "Creature feature", "Legal drama"],
        "answer": "Romance",
        "explanation": "Romance films focus on attraction, intimacy, obstacles, and emotional commitment.",
    },
    {
        "category": "Romantic comedy",
        "prompt": "Which movie type blends a central love story with comic misunderstandings and lighthearted tone?",
        "options": ["Romantic comedy", "Military drama", "Cyberpunk", "Survival thriller"],
        "answer": "Romantic comedy",
        "explanation": "Romantic comedies balance relationship tension with humor and warmth.",
    },
    {
        "category": "Animated film",
        "prompt": "Which movie type is defined by images created frame by frame rather than live-action photography?",
        "options": ["Animated film", "Noir", "Spy thriller", "Docudrama"],
        "answer": "Animated film",
        "explanation": "Animation can be hand-drawn, computer-generated, stop-motion, or mixed media.",
    },
    {
        "category": "Documentary",
        "prompt": "Which movie type presents real people, events, places, or issues in a nonfiction format?",
        "options": ["Documentary", "Fantasy adventure", "Slasher", "Screwball comedy"],
        "answer": "Documentary",
        "explanation": "Documentaries build their argument or story from nonfiction material.",
    },
    {
        "category": "Musical",
        "prompt": "Which movie type uses songs and musical performance to advance story or express character emotion?",
        "options": ["Musical", "Hard-boiled detective film", "Zombie film", "Procedural"],
        "answer": "Musical",
        "explanation": "Musicals make performance part of the storytelling structure.",
    },
    {
        "category": "Western",
        "prompt": "Which movie type is often set on the American frontier with outlaws, sheriffs, ranches, and frontier justice?",
        "options": ["Western", "Space opera", "Family comedy", "Political satire"],
        "answer": "Western",
        "explanation": "Westerns use frontier settings and conflicts around law, survival, and territory.",
    },
    {
        "category": "War film",
        "prompt": "Which movie type focuses on armed conflict, soldiers, combat, military life, or the effects of war?",
        "options": ["War film", "Romantic fantasy", "Heist comedy", "Coming-of-age comedy"],
        "answer": "War film",
        "explanation": "War films examine battle, strategy, sacrifice, trauma, and moral pressure.",
    },
    {
        "category": "Crime film",
        "prompt": "Which movie type revolves around criminals, lawbreaking, investigations, or the justice system?",
        "options": ["Crime film", "Dance film", "Fairy tale", "Epic fantasy"],
        "answer": "Crime film",
        "explanation": "Crime films study criminal acts and their consequences from many angles.",
    },
    {
        "category": "Gangster film",
        "prompt": "Which movie type is a crime subgenre centered on organized crime groups and underworld power?",
        "options": ["Gangster film", "Road movie", "Historical romance", "Creature feature"],
        "answer": "Gangster film",
        "explanation": "Gangster films focus on organized criminal networks, loyalty, ambition, and violence.",
    },
    {
        "category": "Film noir",
        "prompt": "Which movie type is known for cynical mood, shadowy visuals, moral ambiguity, and doomed characters?",
        "options": ["Film noir", "Teen musical", "Sports comedy", "Disaster film"],
        "answer": "Film noir",
        "explanation": "Noir uses fatalism, corruption, and stylized darkness to shape its world.",
    },
    {
        "category": "Superhero film",
        "prompt": "Which movie type follows characters with extraordinary powers or heroic identities saving others from large threats?",
        "options": ["Superhero film", "Legal thriller", "Mockumentary", "Travel documentary"],
        "answer": "Superhero film",
        "explanation": "Superhero films center on masked or powered heroes and their responsibilities.",
    },
    {
        "category": "Adventure",
        "prompt": "Which movie type emphasizes journeys, quests, exploration, danger, and discovery?",
        "options": ["Adventure", "Courtroom drama", "Satire", "Found-footage horror"],
        "answer": "Adventure",
        "explanation": "Adventure films send characters into unfamiliar or risky places with clear goals.",
    },
    {
        "category": "Coming-of-age",
        "prompt": "Which movie type follows a young person growing, maturing, or crossing into a new stage of life?",
        "options": ["Coming-of-age", "Spy film", "Medical drama", "Martial arts film"],
        "answer": "Coming-of-age",
        "explanation": "Coming-of-age stories focus on identity, maturity, and formative choices.",
    },
    {
        "category": "Biographical film",
        "prompt": "Which movie type dramatizes the life or major experiences of a real person?",
        "options": ["Biographical film", "Buddy cop film", "Zombie comedy", "Legal satire"],
        "answer": "Biographical film",
        "explanation": "Biographical films, often called biopics, adapt real lives into dramatic stories.",
    },
    {
        "category": "Historical film",
        "prompt": "Which movie type is set in a real past era and uses historical events or periods as major context?",
        "options": ["Historical film", "Techno-thriller", "Creature comedy", "Teen romance"],
        "answer": "Historical film",
        "explanation": "Historical films recreate or interpret events and social worlds from the past.",
    },
    {
        "category": "Sports film",
        "prompt": "Which movie type centers on athletes, teams, competition, training, and the pressure to win?",
        "options": ["Sports film", "Noir mystery", "Fantasy quest", "Spy comedy"],
        "answer": "Sports film",
        "explanation": "Sports films use competition as a structure for character growth and conflict.",
    },
    {
        "category": "Family film",
        "prompt": "Which movie type is made to appeal broadly to children and adults watching together?",
        "options": ["Family film", "Psychological horror", "Political thriller", "Neo-noir"],
        "answer": "Family film",
        "explanation": "Family films aim for accessible stories, broad emotional appeal, and age-inclusive tone.",
    },
    {
        "category": "Spy film",
        "prompt": "Which movie type features espionage, secret missions, intelligence agencies, and hidden identities?",
        "options": ["Spy film", "Slapstick comedy", "Courtroom drama", "Folk horror"],
        "answer": "Spy film",
        "explanation": "Spy films build tension from surveillance, deception, missions, and national stakes.",
    },
    {
        "category": "Heist film",
        "prompt": "Which movie type focuses on planning, executing, or escaping from a major theft?",
        "options": ["Heist film", "Historical epic", "Body horror", "Road romance"],
        "answer": "Heist film",
        "explanation": "Heist films organize the story around a theft and the team or plan behind it.",
    },
    {
        "category": "Disaster film",
        "prompt": "Which movie type revolves around large-scale catastrophes like earthquakes, floods, fires, or crashes?",
        "options": ["Disaster film", "Screwball comedy", "Police procedural", "Fantasy musical"],
        "answer": "Disaster film",
        "explanation": "Disaster films focus on survival and human response to extreme events.",
    },
    {
        "category": "Martial arts film",
        "prompt": "Which movie type highlights hand-to-hand combat, disciplined fighting styles, and choreographed fight scenes?",
        "options": ["Martial arts film", "Legal drama", "Space opera", "Travelogue"],
        "answer": "Martial arts film",
        "explanation": "Martial arts films make fighting style, training, and physical skill central.",
    },
    {
        "category": "Road movie",
        "prompt": "Which movie type follows characters traveling from place to place, usually changing through the journey?",
        "options": ["Road movie", "Monster movie", "Courtroom thriller", "Concert film"],
        "answer": "Road movie",
        "explanation": "Road movies use travel as the engine for encounters, conflict, and transformation.",
    },
]


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-movie-quiz-key"),
    )

    if test_config:
        app.config.update(test_config)

    @app.get("/")
    def index():
        return render_template("index.html", question_count=len(QUESTIONS))

    @app.post("/start")
    def start():
        session.clear()
        session["current_index"] = 0
        session["score"] = 0
        session["answers"] = []
        session["last_feedback"] = None
        return redirect(url_for("quiz_question", number=1))

    @app.route("/quiz/<int:number>", methods=["GET", "POST"])
    def quiz_question(number):
        if not _quiz_started():
            return redirect(url_for("index"))

        current_index = session["current_index"]
        if current_index >= len(QUESTIONS):
            return redirect(url_for("result"))

        expected_number = current_index + 1
        if number != expected_number:
            return redirect(url_for("quiz_question", number=expected_number))

        question = QUESTIONS[current_index]

        if request.method == "POST":
            selected_answer = request.form.get("answer", "")
            if selected_answer not in question["options"]:
                return (
                    render_template(
                        "question.html",
                        error="Choose one of the listed answers.",
                        feedback=session.get("last_feedback"),
                        number=number,
                        question=question,
                        question_count=len(QUESTIONS),
                    ),
                    400,
                )

            is_correct = selected_answer == question["answer"]
            answers = list(session.get("answers", []))
            answers.append(
                {
                    "question": question["prompt"],
                    "selected": selected_answer,
                    "correct_answer": question["answer"],
                    "is_correct": is_correct,
                }
            )

            session["answers"] = answers
            session["score"] = session.get("score", 0) + int(is_correct)
            session["current_index"] = current_index + 1
            session["last_feedback"] = {
                "question": question["prompt"],
                "selected": selected_answer,
                "correct_answer": question["answer"],
                "is_correct": is_correct,
                "explanation": question["explanation"],
            }

            if session["current_index"] >= len(QUESTIONS):
                return redirect(url_for("result"))
            return redirect(url_for("quiz_question", number=number + 1))

        return render_template(
            "question.html",
            error=None,
            feedback=session.get("last_feedback"),
            number=number,
            question=question,
            question_count=len(QUESTIONS),
        )

    @app.get("/result")
    def result():
        if not _quiz_started():
            return redirect(url_for("index"))

        if session["current_index"] < len(QUESTIONS):
            return redirect(url_for("quiz_question", number=session["current_index"] + 1))

        return render_template(
            "result.html",
            answers=session.get("answers", []),
            question_count=len(QUESTIONS),
            score=session.get("score", 0),
        )

    return app


def _quiz_started():
    return {"current_index", "score", "answers", "last_feedback"}.issubset(session.keys())


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

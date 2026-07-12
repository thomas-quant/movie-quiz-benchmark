import os

from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)


QUESTIONS = [
    {
        "prompt": "A detective follows a trail of clues through rain-soaked streets, never sure whom to trust.",
        "answer": "Mystery",
        "options": ["Mystery", "Musical", "Western", "Fantasy"],
        "fact": "Mysteries are driven by questions, clues, and the eventual reveal.",
    },
    {
        "prompt": "Two rival bakers keep meeting at competitions—and slowly realize they are falling in love.",
        "answer": "Romance",
        "options": ["War", "Romance", "Horror", "Crime"],
        "fact": "Romance films make an evolving love story their emotional center.",
    },
    {
        "prompt": "A crew races through a collapsing city, leaping between vehicles to stop a stolen weapon.",
        "answer": "Action",
        "options": ["Drama", "Documentary", "Action", "Animation"],
        "fact": "Action movies emphasize physical feats, chases, fights, and spectacle.",
    },
    {
        "prompt": "A family moves into an old farmhouse where whispers echo from rooms that do not exist.",
        "answer": "Horror",
        "options": ["Comedy", "Horror", "Sports", "Biography"],
        "fact": "Horror aims to create fear, dread, shock, or unease.",
    },
    {
        "prompt": "An awkward substitute teacher accidentally becomes the leader of a tiny town's parade.",
        "answer": "Comedy",
        "options": ["Thriller", "Comedy", "History", "Science Fiction"],
        "fact": "Comedy builds its storytelling around humor and comic situations.",
    },
    {
        "prompt": "A pilot wakes after 200 years to find that humans now live among cities in the clouds.",
        "answer": "Science Fiction",
        "options": ["Science Fiction", "Western", "Romance", "Crime"],
        "fact": "Science fiction imagines worlds shaped by speculative science or technology.",
    },
    {
        "prompt": "A shy child discovers a hidden kingdom where rivers talk and mountains can move.",
        "answer": "Fantasy",
        "options": ["Mystery", "Fantasy", "Documentary", "War"],
        "fact": "Fantasy invites magic, myth, and impossible worlds into its stories.",
    },
    {
        "prompt": "A struggling musician must choose between a career-defining tour and caring for his father.",
        "answer": "Drama",
        "options": ["Action", "Animation", "Drama", "Adventure"],
        "fact": "Drama focuses on emotional conflict, relationships, and difficult choices.",
    },
    {
        "prompt": "A journalist's investigation into a senator becomes a breathless race against an unseen pursuer.",
        "answer": "Thriller",
        "options": ["Musical", "Thriller", "Family", "Biography"],
        "fact": "Thrillers sustain tension through danger, urgency, and uncertainty.",
    },
    {
        "prompt": "A cartographer crosses an uncharted jungle to find a city missing from every map.",
        "answer": "Adventure",
        "options": ["Adventure", "Horror", "Comedy", "Sports"],
        "fact": "Adventure films send characters into risky journeys and unfamiliar places.",
    },
    {
        "prompt": "A small-town sheriff faces an outlaw at high noon on a dusty frontier main street.",
        "answer": "Western",
        "options": ["Crime", "Western", "History", "Romance"],
        "fact": "Westerns are rooted in frontier settings, conflicts, and mythology.",
    },
    {
        "prompt": "Neighbors burst into choreographed song while trying to save their beloved local theater.",
        "answer": "Musical",
        "options": ["Mystery", "Musical", "War", "Action"],
        "fact": "Musicals use songs and dance as essential parts of the narrative.",
    },
    {
        "prompt": "Filmmakers spend three years following a wolf pack through a changing wilderness.",
        "answer": "Documentary",
        "options": ["Fantasy", "Documentary", "Thriller", "Animation"],
        "fact": "Documentaries use real subjects and evidence to explore the world.",
    },
    {
        "prompt": "A hand-drawn fox leaves the forest and builds an unlikely friendship in the city.",
        "answer": "Animation",
        "options": ["Biography", "Drama", "Animation", "Crime"],
        "fact": "Animation creates movement frame by frame rather than primarily filming live action.",
    },
    {
        "prompt": "A codebreaker works in secret to help turn the tide of a global conflict.",
        "answer": "War",
        "options": ["War", "Comedy", "Family", "Western"],
        "fact": "War films explore armed conflict and its human consequences.",
    },
    {
        "prompt": "An ambitious thief rises through an underground empire while detectives close in.",
        "answer": "Crime",
        "options": ["Science Fiction", "Musical", "Crime", "Adventure"],
        "fact": "Crime films center on lawbreaking, criminal worlds, or their investigation.",
    },
    {
        "prompt": "The true story of a painter is traced from an isolated childhood to worldwide recognition.",
        "answer": "Biography",
        "options": ["Biography", "Horror", "Mystery", "Fantasy"],
        "fact": "Biographical films dramatize the life of a real person.",
    },
    {
        "prompt": "An underdog runner trains for one final chance to qualify for the national team.",
        "answer": "Sports",
        "options": ["History", "Sports", "Thriller", "Romance"],
        "fact": "Sports films build their stories around athletes, teams, and competition.",
    },
    {
        "prompt": "Siblings and their talking dog set out to reunite their parents before the holidays.",
        "answer": "Family",
        "options": ["Action", "Family", "Crime", "War"],
        "fact": "Family films are designed for broad age groups and often emphasize connection.",
    },
    {
        "prompt": "The rise and fall of an ancient city is reconstructed around newly discovered letters.",
        "answer": "History",
        "options": ["History", "Comedy", "Animation", "Science Fiction"],
        "fact": "Historical films dramatize people, places, and events from the past.",
    },
    {
        "prompt": "A private investigator searches for a vanished singer as every witness changes their story.",
        "answer": "Mystery",
        "options": ["Adventure", "Mystery", "Sports", "Musical"],
        "fact": "A central puzzle—and the search for its answer—signals a mystery.",
    },
    {
        "prompt": "Former childhood friends fake a relationship for a wedding, then find the feelings becoming real.",
        "answer": "Romance",
        "options": ["Romance", "War", "Documentary", "Horror"],
        "fact": "When love and emotional intimacy drive the plot, romance is the clearest fit.",
    },
    {
        "prompt": "A retired spy fights across three countries to rescue a kidnapped diplomat.",
        "answer": "Action",
        "options": ["Drama", "Action", "Biography", "Family"],
        "fact": "High-energy confrontations and physical danger are hallmarks of action.",
    },
    {
        "prompt": "Campers realize the figure in their photographs is getting closer in every picture.",
        "answer": "Horror",
        "options": ["Western", "History", "Horror", "Comedy"],
        "fact": "A supernatural threat designed to frighten the audience belongs to horror.",
    },
    {
        "prompt": "Two hopeless roommates enter a talent contest despite having absolutely no talent.",
        "answer": "Comedy",
        "options": ["Thriller", "Comedy", "Crime", "Fantasy"],
        "fact": "Absurd situations and escalating mishaps are classic comedy engines.",
    },
    {
        "prompt": "Scientists discover a signal from beneath the ice that may not have come from Earth.",
        "answer": "Science Fiction",
        "options": ["Musical", "Romance", "Science Fiction", "Sports"],
        "fact": "Extraterrestrial signals and scientific discovery are science-fiction territory.",
    },
    {
        "prompt": "A blacksmith must return a stolen crown before an immortal sorcerer wakes.",
        "answer": "Fantasy",
        "options": ["Fantasy", "Documentary", "Biography", "Crime"],
        "fact": "Sorcery, magical artifacts, and mythic quests point to fantasy.",
    },
    {
        "prompt": "Three sisters return home after years apart to decide what to do with their childhood house.",
        "answer": "Drama",
        "options": ["Animation", "Adventure", "Drama", "Action"],
        "fact": "Grounded relationships and unresolved emotion are central to drama.",
    },
    {
        "prompt": "A commuter receives anonymous instructions—and learns that ignoring them puts the whole train at risk.",
        "answer": "Thriller",
        "options": ["Family", "Thriller", "History", "Western"],
        "fact": "A ticking clock, hidden adversary, and mounting danger define a thriller.",
    },
    {
        "prompt": "A marine biologist sails into forbidden waters in search of a creature thought extinct.",
        "answer": "Adventure",
        "options": ["Adventure", "Mystery", "Comedy", "War"],
        "fact": "Exploration, danger, and discovery make this an adventure.",
    },
]


@app.context_processor
def inject_quiz_size():
    return {"total_questions": len(QUESTIONS)}


@app.get("/")
def home():
    completed = len(session.get("answers", []))
    return render_template("index.html", completed=completed)


@app.post("/quiz/start")
def start_quiz():
    session["answers"] = []
    return redirect(url_for("question", number=1))


@app.route("/quiz/<int:number>", methods=["GET", "POST"])
def question(number):
    if number < 1 or number > len(QUESTIONS):
        return redirect(url_for("home"))

    answers = session.get("answers", [])

    if request.method == "POST":
        selected = request.form.get("answer")
        current = QUESTIONS[number - 1]

        if selected not in current["options"]:
            return render_template(
                "question.html",
                question=current,
                number=number,
                previous=_previous_answer(answers, number),
                selected=None,
                error="Choose one answer to continue.",
            ), 400

        result = {
            "number": number,
            "selected": selected,
            "correct": selected == current["answer"],
            "answer": current["answer"],
            "fact": current["fact"],
        }

        # Replace an answer when revisiting a page; otherwise append it.
        answers = [answer for answer in answers if answer["number"] != number]
        answers.append(result)
        answers.sort(key=lambda answer: answer["number"])
        session["answers"] = answers

        if number == len(QUESTIONS):
            return redirect(url_for("results"))
        return redirect(url_for("question", number=number + 1))

    # Keep the sequence coherent instead of allowing unanswered pages to be skipped.
    first_unanswered = next(
        (index for index in range(1, len(QUESTIONS) + 1)
         if not any(answer["number"] == index for answer in answers)),
        len(QUESTIONS) + 1,
    )
    if number > first_unanswered:
        return redirect(url_for("question", number=first_unanswered))

    saved = next((item for item in answers if item["number"] == number), None)
    return render_template(
        "question.html",
        question=QUESTIONS[number - 1],
        number=number,
        previous=_previous_answer(answers, number),
        selected=saved["selected"] if saved else None,
        error=None,
    )


def _previous_answer(answers, number):
    if number <= 1:
        return None
    return next((item for item in answers if item["number"] == number - 1), None)


@app.get("/results")
def results():
    answers = session.get("answers", [])
    if len(answers) < len(QUESTIONS):
        next_number = len(answers) + 1
        return redirect(url_for("question", number=next_number))

    score = sum(answer["correct"] for answer in answers)
    percentage = round(score / len(QUESTIONS) * 100)

    if percentage >= 90:
        rank = "Genre Auteur"
        message = "You read movie DNA like a seasoned director."
    elif percentage >= 70:
        rank = "Festival Favorite"
        message = "Your watchlist has clearly taken you places."
    elif percentage >= 50:
        rank = "Rising Critic"
        message = "A strong cut—with room for a sequel."
    else:
        rank = "Curious Moviegoer"
        message = "Every great film journey starts with an opening scene."

    return render_template(
        "results.html",
        answers=answers,
        score=score,
        percentage=percentage,
        rank=rank,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)

import os

from flask import Flask, redirect, render_template_string, request, session, url_for


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-movie-quiz-secret")


QUESTIONS = [
    {
        "prompt": "Which movie type is built around characters breaking into songs and choreographed dance numbers?",
        "options": ["Musical", "Noir", "Western", "Docudrama"],
        "answer": 0,
        "note": "Musicals use songs and dance as a main storytelling device.",
    },
    {
        "prompt": "A whodunit about clues, suspects, and a final reveal belongs most directly to which type?",
        "options": ["Mystery", "Disaster", "Road movie", "Sports drama"],
        "answer": 0,
        "note": "Mysteries center on solving a crime, puzzle, or hidden truth.",
    },
    {
        "prompt": "Stories about space travel, advanced technology, aliens, or speculative futures are usually classified as what?",
        "options": ["Science fiction", "Romantic comedy", "Biopic", "Slasher"],
        "answer": 0,
        "note": "Science fiction explores imagined science, technology, and future possibilities.",
    },
    {
        "prompt": "Which movie type is primarily designed to frighten, disturb, or unsettle the audience?",
        "options": ["Horror", "Period drama", "Family", "Heist"],
        "answer": 0,
        "note": "Horror is built around fear, dread, shock, or the supernatural.",
    },
    {
        "prompt": "Fast fights, chases, stunts, explosions, and physical danger usually point to which type?",
        "options": ["Action", "Mockumentary", "Satire", "Coming-of-age"],
        "answer": 0,
        "note": "Action movies emphasize movement, risk, combat, and spectacle.",
    },
    {
        "prompt": "Which movie type focuses on jokes, comic timing, awkward situations, and making the audience laugh?",
        "options": ["Comedy", "War", "Noir", "Monster movie"],
        "answer": 0,
        "note": "Comedy is organized around humor and comic conflict.",
    },
    {
        "prompt": "A story set around frontier towns, outlaws, sheriffs, ranches, and the Old West is usually what type?",
        "options": ["Western", "Fantasy", "Legal thriller", "Animation"],
        "answer": 0,
        "note": "Westerns are tied to frontier settings and the mythology of the American West.",
    },
    {
        "prompt": "Which type is set in a past era and pays close attention to costumes, manners, and historical setting?",
        "options": ["Period drama", "Cyberpunk", "Buddy comedy", "Creature feature"],
        "answer": 0,
        "note": "Period dramas recreate earlier time periods through setting, behavior, and design.",
    },
    {
        "prompt": "When the central question is whether two people will form or keep a loving relationship, the type is usually what?",
        "options": ["Romance", "War", "Noir", "Martial arts"],
        "answer": 0,
        "note": "Romance movies put the emotional relationship at the center of the plot.",
    },
    {
        "prompt": "A tense story driven by suspense, danger, twists, and pressure is most often called what?",
        "options": ["Thriller", "Musical", "Family", "Sports drama"],
        "answer": 0,
        "note": "Thrillers rely on tension, uncertainty, pursuit, and high stakes.",
    },
    {
        "prompt": "Which type uses drawn, stop-motion, computer-generated, or otherwise animated images as its main form?",
        "options": ["Animation", "Crime", "Western", "Docudrama"],
        "answer": 0,
        "note": "Animation describes the form of image-making, not only the audience age.",
    },
    {
        "prompt": "A nonfiction film using real people, interviews, archive material, or observed events is what type?",
        "options": ["Documentary", "Superhero", "Romantic comedy", "Fantasy"],
        "answer": 0,
        "note": "Documentaries present nonfiction subjects, even when they use a strong point of view.",
    },
    {
        "prompt": "A dramatic film based on the life of a real person is usually called what?",
        "options": ["Biopic", "Disaster", "Slasher", "Buddy comedy"],
        "answer": 0,
        "note": "Biopic is short for biographical picture.",
    },
    {
        "prompt": "Movies centered on criminals, detectives, gangs, investigations, or the justice system fit which type?",
        "options": ["Crime", "Musical", "Road movie", "Fantasy"],
        "answer": 0,
        "note": "Crime movies focus on criminal acts and their consequences.",
    },
    {
        "prompt": "A quest, expedition, treasure hunt, or dangerous journey to unfamiliar places is most often what type?",
        "options": ["Adventure", "Noir", "Mockumentary", "Legal thriller"],
        "answer": 0,
        "note": "Adventure movies are driven by exploration, quests, and external obstacles.",
    },
    {
        "prompt": "Which type usually features masked heroes, comic-book powers, secret identities, and villains?",
        "options": ["Superhero", "Period drama", "Sports drama", "Satire"],
        "answer": 0,
        "note": "Superhero movies center on heroic figures with extraordinary abilities or identities.",
    },
    {
        "prompt": "Highly stylized hand-to-hand combat, training, honor codes, and fight choreography point to what type?",
        "options": ["Martial arts", "Romance", "Disaster", "Documentary"],
        "answer": 0,
        "note": "Martial arts movies make combat styles and fight craft central to the appeal.",
    },
    {
        "prompt": "Magic, invented worlds, mythical creatures, curses, and enchanted objects belong most directly to which type?",
        "options": ["Fantasy", "Heist", "Noir", "Legal thriller"],
        "answer": 0,
        "note": "Fantasy uses magic or impossible worlds as core story material.",
    },
    {
        "prompt": "A light romance built around comic misunderstandings and relationship obstacles is what type?",
        "options": ["Romantic comedy", "War", "Monster movie", "Science fiction"],
        "answer": 0,
        "note": "Romantic comedies combine a love story with comic structure and tone.",
    },
    {
        "prompt": "Which type uses humor, exaggeration, or irony to criticize society, politics, media, or human behavior?",
        "options": ["Satire", "Action", "Family", "Sports drama"],
        "answer": 0,
        "note": "Satire makes a critical point through comedy or exaggeration.",
    },
    {
        "prompt": "Stories about soldiers, battles, combat missions, military life, and the cost of conflict are usually what type?",
        "options": ["War", "Musical", "Coming-of-age", "Mockumentary"],
        "answer": 0,
        "note": "War movies focus on armed conflict and its effects.",
    },
    {
        "prompt": "A film about athletes, teams, competition, training, and a big match or season is most likely what type?",
        "options": ["Sports drama", "Noir", "Horror", "Period drama"],
        "answer": 0,
        "note": "Sports dramas use competition and performance as the story engine.",
    },
    {
        "prompt": "Which type follows a young person growing emotionally, socially, or morally into a new stage of life?",
        "options": ["Coming-of-age", "Heist", "Disaster", "Western"],
        "answer": 0,
        "note": "Coming-of-age movies focus on maturity, identity, and transition.",
    },
    {
        "prompt": "A movie aimed at broad household viewing, often with children and adults both in mind, is usually labeled what?",
        "options": ["Family", "Slasher", "Legal thriller", "Noir"],
        "answer": 0,
        "note": "Family movies are designed for a wide age range and shared viewing.",
    },
    {
        "prompt": "Which type makes a trip by car, bus, train, or highway the structure of the story?",
        "options": ["Road movie", "Fantasy", "Martial arts", "Monster movie"],
        "answer": 0,
        "note": "Road movies use travel as the plot framework and a source of change.",
    },
    {
        "prompt": "Shadowy lighting, moral ambiguity, private eyes, fatal choices, and urban crime point to what type?",
        "options": ["Noir", "Musical", "Family", "Adventure"],
        "answer": 0,
        "note": "Noir is known for dark style, crime, cynicism, and compromised characters.",
    },
    {
        "prompt": "A plot about planning, assembling a crew, and executing a robbery is most directly what type?",
        "options": ["Heist", "Biopic", "Animation", "War"],
        "answer": 0,
        "note": "Heist movies are built around the preparation and execution of a theft.",
    },
    {
        "prompt": "Which type follows people trying to survive earthquakes, fires, sinking ships, asteroids, or other catastrophes?",
        "options": ["Disaster", "Romance", "Mockumentary", "Superhero"],
        "answer": 0,
        "note": "Disaster movies place large-scale catastrophe at the center.",
    },
    {
        "prompt": "A film where a creature, beast, or giant animal terrorizes characters is usually what type?",
        "options": ["Monster movie", "Period drama", "Sports drama", "Legal thriller"],
        "answer": 0,
        "note": "Monster movies build conflict around a threatening creature.",
    },
    {
        "prompt": "Which horror subtype features a killer stalking and attacking a series of victims?",
        "options": ["Slasher", "Documentary", "Western", "Romantic comedy"],
        "answer": 0,
        "note": "Slashers usually involve a persistent killer and a pattern of attacks.",
    },
]


ANSWER_POSITIONS = [0, 2, 1, 3, 2, 0, 3, 1, 2, 0, 3, 1, 0, 2, 3, 1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0]


def spread_answer_positions():
    for question, position in zip(QUESTIONS, ANSWER_POSITIONS):
        correct_option = question["options"][0]
        distractors = question["options"][1:]
        question["options"] = distractors[:position] + [correct_option] + distractors[position:]
        question["answer"] = position


spread_answer_positions()


BASE_STYLES = """
<style>
    :root {
        color-scheme: light;
        --ink: #17202a;
        --muted: #5c6672;
        --line: #d9dee5;
        --paper: #fbfbf8;
        --panel: #ffffff;
        --accent: #c83d34;
        --accent-strong: #9d2d27;
        --gold: #d79b28;
        --green: #257a53;
        --red: #b43b35;
    }

    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        min-height: 100vh;
        color: var(--ink);
        background:
            linear-gradient(135deg, rgba(200, 61, 52, 0.08), transparent 32%),
            linear-gradient(315deg, rgba(37, 122, 83, 0.10), transparent 34%),
            var(--paper);
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        letter-spacing: 0;
    }

    a {
        color: inherit;
    }

    .shell {
        width: min(1040px, calc(100vw - 32px));
        margin: 0 auto;
        padding: 28px 0 40px;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        padding: 12px 0 24px;
    }

    .brand {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        font-weight: 800;
        font-size: clamp(1.05rem, 2vw, 1.25rem);
    }

    .brand-mark {
        width: 38px;
        height: 38px;
        border-radius: 8px;
        display: grid;
        place-items: center;
        color: white;
        background: linear-gradient(135deg, var(--accent), #222832);
        box-shadow: 0 10px 24px rgba(23, 32, 42, 0.15);
        position: relative;
        overflow: hidden;
    }

    .brand-mark::before,
    .brand-mark::after {
        content: "";
        position: absolute;
        width: 5px;
        height: 100%;
        top: 0;
        background: repeating-linear-gradient(to bottom, rgba(255,255,255,0.72) 0 4px, transparent 4px 8px);
    }

    .brand-mark::before {
        left: 6px;
    }

    .brand-mark::after {
        right: 6px;
    }

    .meta-pill {
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 8px 12px;
        color: var(--muted);
        background: rgba(255, 255, 255, 0.65);
        font-size: 0.93rem;
        white-space: nowrap;
    }

    .layout {
        display: grid;
        grid-template-columns: minmax(0, 1.12fr) minmax(280px, 0.88fr);
        gap: 24px;
        align-items: stretch;
    }

    .panel {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid rgba(217, 222, 229, 0.95);
        border-radius: 8px;
        box-shadow: 0 24px 70px rgba(23, 32, 42, 0.11);
    }

    .quiz-card {
        padding: clamp(22px, 4vw, 34px);
    }

    .cinema-panel {
        min-height: 420px;
        padding: 18px;
        display: grid;
        align-content: stretch;
        background:
            linear-gradient(rgba(23, 32, 42, 0.54), rgba(23, 32, 42, 0.48)),
            url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1200&q=80");
        background-position: center;
        background-size: cover;
        overflow: hidden;
    }

    .screen-board {
        align-self: end;
        display: grid;
        gap: 12px;
        color: white;
        text-shadow: 0 1px 16px rgba(0, 0, 0, 0.5);
    }

    .score-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 12px;
    }

    .score-cell {
        border: 1px solid rgba(255, 255, 255, 0.45);
        border-radius: 8px;
        padding: 14px;
        background: rgba(23, 32, 42, 0.42);
        backdrop-filter: blur(4px);
    }

    .score-cell strong {
        display: block;
        font-size: clamp(1.45rem, 4vw, 2.1rem);
        line-height: 1;
    }

    .score-cell span {
        display: block;
        margin-top: 6px;
        color: rgba(255, 255, 255, 0.82);
        font-size: 0.85rem;
    }

    .eyebrow {
        margin: 0 0 12px;
        color: var(--accent-strong);
        font-size: 0.82rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    h1 {
        margin: 0;
        font-size: clamp(2rem, 5vw, 4.6rem);
        line-height: 0.97;
        max-width: 11ch;
    }

    h2 {
        margin: 0;
        font-size: clamp(1.55rem, 3vw, 2.25rem);
        line-height: 1.08;
    }

    .lead {
        margin: 16px 0 0;
        color: var(--muted);
        font-size: clamp(1rem, 2vw, 1.14rem);
        line-height: 1.55;
        max-width: 62ch;
    }

    .progress {
        display: grid;
        gap: 8px;
        margin: 22px 0 0;
    }

    .progress-label {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        color: var(--muted);
        font-size: 0.92rem;
    }

    .progress-track {
        width: 100%;
        height: 10px;
        overflow: hidden;
        border-radius: 999px;
        background: #e6e9ee;
    }

    .progress-fill {
        height: 100%;
        width: var(--progress);
        border-radius: inherit;
        background: linear-gradient(90deg, var(--accent), var(--gold));
    }

    .feedback {
        margin: 0 0 22px;
        border: 1px solid var(--line);
        border-left: 5px solid var(--green);
        border-radius: 8px;
        padding: 14px 16px;
        background: #f7fbf8;
    }

    .feedback.missed {
        border-left-color: var(--red);
        background: #fff8f7;
    }

    .feedback-title {
        margin: 0 0 7px;
        font-weight: 800;
    }

    .feedback p {
        margin: 0;
        color: var(--muted);
        line-height: 1.45;
    }

    form {
        margin-top: 24px;
    }

    .options {
        display: grid;
        gap: 12px;
        margin: 0;
        padding: 0;
        border: 0;
    }

    .option {
        display: grid;
        grid-template-columns: 24px 1fr;
        gap: 12px;
        align-items: start;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 15px 16px;
        background: white;
        cursor: pointer;
        transition: border-color 140ms ease, box-shadow 140ms ease, transform 140ms ease;
    }

    .option:hover,
    .option:focus-within {
        border-color: var(--accent);
        box-shadow: 0 12px 30px rgba(200, 61, 52, 0.12);
        transform: translateY(-1px);
    }

    .option input {
        margin-top: 2px;
        accent-color: var(--accent);
    }

    .option span {
        line-height: 1.35;
        font-weight: 650;
    }

    .actions {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-top: 24px;
        flex-wrap: wrap;
    }

    .button {
        appearance: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 44px;
        border: 0;
        border-radius: 8px;
        padding: 11px 18px;
        background: var(--accent);
        color: white;
        font: inherit;
        font-weight: 800;
        text-decoration: none;
        cursor: pointer;
        box-shadow: 0 14px 30px rgba(200, 61, 52, 0.18);
    }

    .button:hover,
    .button:focus {
        background: var(--accent-strong);
    }

    .button.secondary {
        border: 1px solid var(--line);
        background: white;
        color: var(--ink);
        box-shadow: none;
    }

    .error {
        margin: 16px 0 0;
        color: var(--red);
        font-weight: 750;
    }

    .review {
        margin-top: 26px;
        display: grid;
        gap: 12px;
    }

    .review-row {
        display: grid;
        gap: 8px;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 14px;
        background: white;
    }

    .review-head {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        font-weight: 800;
    }

    .review-status {
        color: var(--green);
        white-space: nowrap;
    }

    .review-status.missed {
        color: var(--red);
    }

    .review-row p {
        margin: 0;
        color: var(--muted);
        line-height: 1.45;
    }

    @media (max-width: 780px) {
        .shell {
            width: min(100% - 24px, 640px);
            padding-top: 14px;
        }

        .topbar {
            align-items: flex-start;
            padding-bottom: 14px;
        }

        .layout {
            grid-template-columns: 1fr;
        }

        .cinema-panel {
            min-height: 260px;
            order: -1;
        }

        h1 {
            max-width: 100%;
        }
    }
</style>
"""


HOME_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Movie Type Quiz</title>
    """ + BASE_STYLES + """
</head>
<body>
    <div class="shell">
        <header class="topbar">
            <div class="brand"><span class="brand-mark" aria-hidden="true"></span>Movie Type Quiz</div>
            <div class="meta-pill">{{ total }} questions</div>
        </header>
        <main class="layout">
            <section class="panel quiz-card">
                <p class="eyebrow">Genre check</p>
                <h1>Movie Type Quiz</h1>
                <p class="lead">Match each clue to the movie type it describes.</p>
                <form action="{{ url_for('start') }}" method="post">
                    <div class="actions">
                        <button class="button" type="submit">Start quiz</button>
                        {% if in_progress %}
                            <a class="button secondary" href="{{ url_for('question', number=current + 1) }}">Resume</a>
                        {% endif %}
                    </div>
                </form>
            </section>
            <aside class="panel cinema-panel" aria-label="Cinema seats">
                <div class="screen-board">
                    <div class="score-grid">
                        <div class="score-cell">
                            <strong>{{ total }}</strong>
                            <span>questions</span>
                        </div>
                        <div class="score-cell">
                            <strong>{{ answered }}</strong>
                            <span>answered</span>
                        </div>
                    </div>
                </div>
            </aside>
        </main>
    </div>
</body>
</html>
"""


QUESTION_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Question {{ number }} - Movie Type Quiz</title>
    """ + BASE_STYLES + """
</head>
<body>
    <div class="shell">
        <header class="topbar">
            <div class="brand"><span class="brand-mark" aria-hidden="true"></span>Movie Type Quiz</div>
            <div class="meta-pill">Score {{ score }} / {{ answered }}</div>
        </header>
        <main class="layout">
            <section class="panel quiz-card">
                {% if last_feedback %}
                    <div class="feedback{% if not last_feedback.is_correct %} missed{% endif %}">
                        <p class="feedback-title">
                            Previous page:
                            {% if last_feedback.is_correct %}Correct{% else %}Missed{% endif %}
                        </p>
                        <p>
                            You chose {{ last_feedback.selected }}.
                            {% if not last_feedback.is_correct %}
                                Correct answer: {{ last_feedback.correct }}.
                            {% endif %}
                            {{ last_feedback.note }}
                        </p>
                    </div>
                {% endif %}

                <p class="eyebrow">Question {{ number }} of {{ total }}</p>
                <h2>{{ question.prompt }}</h2>

                <form method="post">
                    <fieldset class="options">
                        <legend class="eyebrow">Choose one</legend>
                        {% for option in question.options %}
                            <label class="option">
                                <input type="radio" name="choice" value="{{ loop.index0 }}" required>
                                <span>{{ option }}</span>
                            </label>
                        {% endfor %}
                    </fieldset>
                    {% if error %}
                        <p class="error">{{ error }}</p>
                    {% endif %}
                    <div class="actions">
                        <button class="button" type="submit">
                            {% if number == total %}Finish quiz{% else %}Next question{% endif %}
                        </button>
                        <a class="button secondary" href="{{ url_for('home') }}">Exit</a>
                    </div>
                </form>
            </section>
            <aside class="panel cinema-panel" aria-label="Quiz progress">
                <div class="screen-board">
                    <div class="score-grid">
                        <div class="score-cell">
                            <strong>{{ score }}</strong>
                            <span>score</span>
                        </div>
                        <div class="score-cell">
                            <strong>{{ total - answered }}</strong>
                            <span>left</span>
                        </div>
                    </div>
                    <div class="progress">
                        <div class="progress-label">
                            <span>Progress</span>
                            <span>{{ answered }} / {{ total }}</span>
                        </div>
                        <div class="progress-track" aria-hidden="true">
                            <div class="progress-fill" style="--progress: {{ progress }}%;"></div>
                        </div>
                    </div>
                </div>
            </aside>
        </main>
    </div>
</body>
</html>
"""


RESULT_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Results - Movie Type Quiz</title>
    """ + BASE_STYLES + """
</head>
<body>
    <div class="shell">
        <header class="topbar">
            <div class="brand"><span class="brand-mark" aria-hidden="true"></span>Movie Type Quiz</div>
            <div class="meta-pill">Final score {{ score }} / {{ total }}</div>
        </header>
        <main class="layout">
            <section class="panel quiz-card">
                <p class="eyebrow">Results</p>
                <h1>{{ score }} / {{ total }}</h1>
                <p class="lead">{{ result_message }}</p>
                <form action="{{ url_for('start') }}" method="post">
                    <div class="actions">
                        <button class="button" type="submit">Retake quiz</button>
                        <a class="button secondary" href="{{ url_for('home') }}">Home</a>
                    </div>
                </form>

                <div class="review">
                    {% for row in rows %}
                        <article class="review-row">
                            <div class="review-head">
                                <span>{{ row.number }}. {{ row.prompt }}</span>
                                <span class="review-status{% if not row.is_correct %} missed{% endif %}">
                                    {% if row.is_correct %}Correct{% else %}Missed{% endif %}
                                </span>
                            </div>
                            <p>You chose {{ row.selected }}. Correct answer: {{ row.correct }}.</p>
                        </article>
                    {% endfor %}
                </div>
            </section>
            <aside class="panel cinema-panel" aria-label="Final score">
                <div class="screen-board">
                    <div class="score-grid">
                        <div class="score-cell">
                            <strong>{{ score }}</strong>
                            <span>correct</span>
                        </div>
                        <div class="score-cell">
                            <strong>{{ total - score }}</strong>
                            <span>missed</span>
                        </div>
                    </div>
                </div>
            </aside>
        </main>
    </div>
</body>
</html>
"""


def normalize_state():
    answers = session.get("answers", [])
    if not isinstance(answers, list):
        answers = []
    answers = [answer for answer in answers if isinstance(answer, int)]
    answers = answers[: len(QUESTIONS)]
    session["answers"] = answers
    session["current"] = len(answers)
    session.modified = True
    return answers


def score_for(answers):
    return sum(
        1
        for index, selected in enumerate(answers)
        if 0 <= selected < len(QUESTIONS[index]["options"])
        and selected == QUESTIONS[index]["answer"]
    )


def feedback_for(index, selected):
    question = QUESTIONS[index]
    correct_index = question["answer"]
    return {
        "is_correct": selected == correct_index,
        "selected": question["options"][selected],
        "correct": question["options"][correct_index],
        "note": question["note"],
    }


@app.get("/")
def home():
    answers = normalize_state()
    current = len(answers)
    return render_template_string(
        HOME_TEMPLATE,
        total=len(QUESTIONS),
        answered=current,
        current=current,
        in_progress=0 < current < len(QUESTIONS),
    )


@app.post("/start")
def start():
    session.clear()
    session["answers"] = []
    session["current"] = 0
    return redirect(url_for("question", number=1))


@app.route("/question/<int:number>", methods=["GET", "POST"])
def question(number):
    answers = normalize_state()
    current = len(answers)

    if current >= len(QUESTIONS):
        return redirect(url_for("results"))

    expected_number = current + 1
    if number != expected_number:
        return redirect(url_for("question", number=expected_number))

    question_data = QUESTIONS[current]

    if request.method == "POST":
        raw_choice = request.form.get("choice", "")
        try:
            selected = int(raw_choice)
        except ValueError:
            selected = -1

        if selected < 0 or selected >= len(question_data["options"]):
            return render_question(
                number=number,
                question_data=question_data,
                answers=answers,
                error="Choose one answer.",
            )

        answers.append(selected)
        session["answers"] = answers
        session["current"] = len(answers)
        session.modified = True

        if len(answers) == len(QUESTIONS):
            return redirect(url_for("results"))
        return redirect(url_for("question", number=len(answers) + 1))

    return render_question(number=number, question_data=question_data, answers=answers)


def render_question(number, question_data, answers, error=None):
    last_feedback = None
    if answers:
        last_feedback = feedback_for(len(answers) - 1, answers[-1])

    answered = len(answers)
    progress = round((answered / len(QUESTIONS)) * 100, 2)

    return render_template_string(
        QUESTION_TEMPLATE,
        total=len(QUESTIONS),
        number=number,
        question=question_data,
        answered=answered,
        score=score_for(answers),
        progress=progress,
        last_feedback=last_feedback,
        error=error,
    )


@app.get("/results")
def results():
    answers = normalize_state()
    if len(answers) < len(QUESTIONS):
        return redirect(url_for("question", number=len(answers) + 1))

    rows = []
    for index, selected in enumerate(answers):
        question_data = QUESTIONS[index]
        correct_index = question_data["answer"]
        rows.append(
            {
                "number": index + 1,
                "prompt": question_data["prompt"],
                "selected": question_data["options"][selected],
                "correct": question_data["options"][correct_index],
                "is_correct": selected == correct_index,
            }
        )

    score = score_for(answers)
    percent = score / len(QUESTIONS)
    if percent == 1:
        result_message = "Perfect score."
    elif percent >= 0.8:
        result_message = "Strong genre instincts."
    elif percent >= 0.6:
        result_message = "Solid score with room to sharpen a few categories."
    else:
        result_message = "Review the missed genres and try again."

    return render_template_string(
        RESULT_TEMPLATE,
        total=len(QUESTIONS),
        score=score,
        rows=rows,
        result_message=result_message,
    )


if __name__ == "__main__":
    app.run(debug=True)

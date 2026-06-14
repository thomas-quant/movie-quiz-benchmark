from flask import Flask, render_template_string, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "movie-quiz-secret-key-change-me"

QUESTIONS = [
    {
        "id": 1,
        "question": "What kind of mood are you usually in when you pick a movie?",
        "options": [
            ("A", "I want to laugh out loud", "comedy"),
            ("B", "I want to feel my heart race", "thriller"),
            ("C", "I want to be moved to tears", "drama"),
            ("D", "I want to escape into another world", "fantasy"),
        ],
    },
    {
        "id": 2,
        "question": "Pick a setting for a perfect evening film.",
        "options": [
            ("A", "A bustling city with witty characters", "comedy"),
            ("B", "A dark, rain-soaked alley", "thriller"),
            ("C", "A small town with deep family ties", "drama"),
            ("D", "A galaxy far, far away", "scifi"),
        ],
    },
    {
        "id": 3,
        "question": "Which best describes your ideal film pacing?",
        "options": [
            ("A", "Quick jokes, snappy edits", "comedy"),
            ("B", "Slow burn that explodes", "thriller"),
            ("C", "Patient and emotionally rich", "drama"),
            ("D", "Relentless action set-pieces", "action"),
        ],
    },
    {
        "id": 4,
        "question": "What do you most want from a film's main character?",
        "options": [
            ("A", "A lovable underdog", "comedy"),
            ("B", "A morally grey antihero", "thriller"),
            ("C", "Someone with a profound inner struggle", "drama"),
            ("D", "A chosen one with a destiny", "fantasy"),
        ],
    },
    {
        "id": 5,
        "question": "Choose a favorite director-style storytelling:",
        "options": [
            ("A", "Edgar Wright's rapid-fire humor", "comedy"),
            ("B", "David Fincher's meticulous dread", "thriller"),
            ("C", "Greta Gerwig's tender realism", "drama"),
            ("D", "Christopher Nolan's mind-bending plots", "scifi"),
        ],
    },
    {
        "id": 6,
        "question": "Which soundtrack appeals most?",
        "options": [
            ("A", "Quirky indie pop", "comedy"),
            ("B", "Pulsing electronic tension", "thriller"),
            ("C", "Sweeping orchestral score", "drama"),
            ("D", "Epic choir and brass", "fantasy"),
        ],
    },
    {
        "id": 7,
        "question": "Pick a perfect movie-watching snack:",
        "options": [
            ("A", "Sweet popcorn with friends", "comedy"),
            ("B", "Coffee at midnight, alone", "thriller"),
            ("C", "Tea and a quiet room", "drama"),
            ("D", "Anything goes — I'm there for the ride", "action"),
        ],
    },
    {
        "id": 8,
        "question": "What ending do you prefer?",
        "options": [
            ("A", "Happy, feel-good wrap-up", "comedy"),
            ("B", "Twist that recontextualizes everything", "thriller"),
            ("C", "Bittersweet but meaningful", "drama"),
            ("D", "World saved, sequel teased", "scifi"),
        ],
    },
    {
        "id": 9,
        "question": "How do you feel about jump scares?",
        "options": [
            ("A", "Love them if they're in a comedy", "comedy"),
            ("B", "More of a slow dread person, honestly", "thriller"),
            ("C", "They're fine in service of the story", "horror"),
            ("D", "Bring them on — I want the adrenaline", "horror"),
        ],
    },
    {
        "id": 10,
        "question": "Choose a film poster vibe:",
        "options": [
            ("A", "Bright colors, big smiles", "comedy"),
            ("B", "Black background, single striking face", "thriller"),
            ("C", "Two people, silhouette, golden hour", "romance"),
            ("D", "Massive explosion, lone hero in front", "action"),
        ],
    },
    {
        "id": 11,
        "question": "What era of film do you gravitate toward?",
        "options": [
            ("A", "Modern 2010s+ indie hits", "comedy"),
            ("B", "70s New Hollywood grit", "drama"),
            ("C", "Golden Age classics", "romance"),
            ("D", "Whatever's brand new this week", "action"),
        ],
    },
    {
        "id": 12,
        "question": "Pick a favorite sub-genre to mash into anything:",
        "options": [
            ("A", "Buddy comedy", "comedy"),
            ("B", "Heist gone wrong", "thriller"),
            ("C", "Coming of age", "drama"),
            ("D", "Time loop", "scifi"),
        ],
    },
    {
        "id": 13,
        "question": "How important are practical effects to you?",
        "options": [
            ("A", "I just want a good time", "comedy"),
            ("B", "Real stunts make action sing", "action"),
            ("C", "In-camera magic beats CGI", "fantasy"),
            ("D", "Whatever serves the story", "drama"),
        ],
    },
    {
        "id": 14,
        "question": "Pick a streaming night format:",
        "options": [
            ("A", "90-minute crowd-pleaser", "comedy"),
            ("B", "Slow-burn limited series", "drama"),
            ("C", "Trilogy marathon", "fantasy"),
            ("D", "Standalone one-and-done", "thriller"),
        ],
    },
    {
        "id": 15,
        "question": "Which trait matters most in a lead performance?",
        "options": [
            ("A", "Comedic timing", "comedy"),
            ("B", "Charisma and presence", "action"),
            ("C", "Vulnerability", "drama"),
            ("D", "Menace", "thriller"),
        ],
    },
    {
        "id": 16,
        "question": "Pick a setting you'd love to explore:",
        "options": [
            ("A", "A road trip across America", "comedy"),
            ("B", "A noir detective's office", "thriller"),
            ("C", "A magical school", "fantasy"),
            ("D", "A space station", "scifi"),
        ],
    },
    {
        "id": 17,
        "question": "What's your tolerance for ambiguity?",
        "options": [
            ("A", "I want it all spelled out, happily", "comedy"),
            ("B", "I love a good ambiguous ending", "drama"),
            ("C", "I'm fine with it if it's earned", "thriller"),
            ("D", "Give me answers OR a wild ride", "scifi"),
        ],
    },
    {
        "id": 18,
        "question": "Favorite kind of villain?",
        "options": [
            ("A", "A bumbling foil", "comedy"),
            ("B", "A mirror of the hero", "drama"),
            ("C", "An existential threat", "scifi"),
            ("D", "A pure evil force of nature", "horror"),
        ],
    },
    {
        "id": 19,
        "question": "Pick a perfect film length:",
        "options": [
            ("A", "Under 100 minutes", "comedy"),
            ("B", "2 hours, tightly paced", "action"),
            ("C", "Over 2.5 hours, deep dive", "drama"),
            ("D", "Whatever it takes to tell the story", "fantasy"),
        ],
    },
    {
        "id": 20,
        "question": "Which theme resonates most?",
        "options": [
            ("A", "Friendship and found family", "comedy"),
            ("B", "Justice and revenge", "thriller"),
            ("C", "Love in all its forms", "romance"),
            ("D", "Survival against the odds", "action"),
        ],
    },
    {
        "id": 21,
        "question": "How do you feel about musicals?",
        "options": [
            ("A", "I love them, give me big numbers", "musical"),
            ("B", "Only the really clever ones", "comedy"),
            ("C", "Sometimes, in the right mood", "drama"),
            ("D", "Not really my thing", "thriller"),
        ],
    },
    {
        "id": 22,
        "question": "Pick a perfect opening scene:",
        "options": [
            ("A", "An awkward job interview", "comedy"),
            ("B", "A voiceover setting up a mystery", "thriller"),
            ("C", "A first kiss", "romance"),
            ("D", "A hero being thrown into chaos", "action"),
        ],
    },
    {
        "id": 23,
        "question": "Best way to watch a film?",
        "options": [
            ("A", "Big theater, opening weekend", "action"),
            ("B", "Cozy couch, lights off, focused", "thriller"),
            ("C", "Background noise while cooking", "comedy"),
            ("D", "On a plane — no distractions", "drama"),
        ],
    },
    {
        "id": 24,
        "question": "Pick a documentary topic you'd actually watch:",
        "options": [
            ("A", "Behind the scenes of a comedy legend", "comedy"),
            ("B", "A true crime deep dive", "thriller"),
            ("C", "A nature epic", "scifi"),
            ("D", "An artist portrait", "drama"),
        ],
    },
    {
        "id": 25,
        "question": "Which film trope do you secretly love?",
        "options": [
            ("A", "The training montage", "action"),
            ("B", "The final speech that wins everyone over", "drama"),
            ("C", "The meet-cute", "romance"),
            ("D", "The heist plan walkthrough", "thriller"),
        ],
    },
    {
        "id": 26,
        "question": "Best kind of twist?",
        "options": [
            ("A", "The villain was the sidekick all along", "thriller"),
            ("B", "It was all a dream — actually no", "comedy"),
            ("C", "The protagonist was the villain", "drama"),
            ("D", "Time travel did the thing", "scifi"),
        ],
    },
    {
        "id": 27,
        "question": "Which element of fantasy appeals most?",
        "options": [
            ("A", "A richly built magic system", "fantasy"),
            ("B", "Epic world-ending stakes", "fantasy"),
            ("C", "Quirky mythical creatures", "comedy"),
            ("D", "Low-stakes magical realism", "drama"),
        ],
    },
    {
        "id": 28,
        "question": "Pick a perfect post-film feeling:",
        "options": [
            ("A", "Giggly and quoting lines to friends", "comedy"),
            ("B", "Staring at the wall, processing", "drama"),
            ("C", "Pumped to start something new", "action"),
            ("D", "Looking up the entire filmography", "thriller"),
        ],
    },
    {
        "id": 29,
        "question": "Romance subplot — how do you feel?",
        "options": [
            ("A", "Love it when it's central", "romance"),
            ("B", "Only if it doesn't derail the plot", "action"),
            ("C", "Skip it, I'm here for the mission", "thriller"),
            ("D", "Make it awkward and funny", "comedy"),
        ],
    },
    {
        "id": 30,
        "question": "Final question: what matters most in a film to you?",
        "options": [
            ("A", "It made me laugh", "comedy"),
            ("B", "It made me think", "drama"),
            ("C", "It thrilled me", "thriller"),
            ("D", "It transported me", "fantasy"),
        ],
    },
]

RESULT_COPY = {
    "comedy": {
        "title": "The Comedy Lover",
        "tagline": "You came for the laughs and stayed for the heart.",
        "summary": "You gravitate toward films that find the humor in being human. You love sharp dialogue, awkward situations, and characters who stumble into warmth. Think Edgar Wright, Greta Gerwig, or Taika Waititi — storytellers who believe the best jokes have something true inside them.",
        "films": ["The Grand Budapest Hotel", "Superbad", "Booksmart", "The Big Lebowski", "Jojo Rabbit"],
    },
    "drama": {
        "title": "The Drama Devotee",
        "tagline": "You want to feel something real, and stay for the catharsis.",
        "summary": "You're drawn to stories that treat emotions as the main event. You appreciate patient pacing, layered performances, and the kind of quiet scene that hits harder than any explosion. The best dramas leave you changed by the credits.",
        "films": ["Moonlight", "Marriage Story", "The Shawshank Redemption", "Lady Bird", "Manchester by the Sea"],
    },
    "thriller": {
        "title": "The Thrill Seeker",
        "tagline": "You live for the tension between what is and what could be.",
        "summary": "You love a film that keeps you guessing, second-guessing, and leaning forward. Twists, unreliable narrators, and slow-burn dread are your catnip. You don't mind being uncomfortable — you came for the chill down the spine.",
        "films": ["Parasite", "Gone Girl", "Se7en", "Zodiac", "The Prestige"],
    },
    "fantasy": {
        "title": "The Fantasy Wanderer",
        "tagline": "You want to be carried to a world that couldn't exist without stories.",
        "summary": "You crave myth, magic, and impossible journeys. Whether it's a hidden kingdom, a chosen one, or a quiet spell tucked into a kitchen sink, you want films that treat wonder as a serious craft. Reality is fine — magic is better.",
        "films": ["The Lord of the Rings", "Pan's Labyrinth", "Spirited Away", "The Princess Bride", "Everything Everywhere All at Once"],
    },
    "scifi": {
        "title": "The Sci-Fi Visionary",
        "tagline": "You watch films for tomorrow's questions, today.",
        "summary": "Big ideas, weird worlds, and the occasional paradox are your love language. You're fascinated by how technology bends humanity — for better, worse, or stranger. You want a film that leaves you arguing about implications at 2 AM.",
        "films": ["Arrival", "Blade Runner 2049", "Ex Machina", "Dune", "Interstellar"],
    },
    "action": {
        "title": "The Action Junkie",
        "tagline": "You came for the stunts, you stayed for the spectacle.",
        "summary": "You want momentum, muscle, and choreography that earns its applause. Car chases, fist fights, last-minute saves — you want a film that knows exactly what it is and never apologizes. Practical stunts and clean framing are your love letter.",
        "films": ["Mad Max: Fury Road", "John Wick", "Mission: Impossible — Fallout", "The Raid", "Top Gun: Maverick"],
    },
    "romance": {
        "title": "The Romance Romantic",
        "tagline": "You believe in the meet-cute, the fight, and the coming back.",
        "summary": "You want love stories that earn their happy ending — or earn their heartbreak. You pay attention to glances, montages, and the small details of how people fall for each other. The best romances feel like remembering your own.",
        "films": ["Before Sunrise", "La La Land", "In the Mood for Love", "Eternal Sunshine of the Spotless Mind", "Past Lives"],
    },
    "horror": {
        "title": "The Horror Connoisseur",
        "tagline": "You don't flinch. You lean closer.",
        "summary": "You treat dread like a craft. Whether it's supernatural, psychological, or just plain weird, you want a film that knows when to hold a silence and when to break it. Jump scares are fine — real horror is the thing you feel the next morning.",
        "films": ["Hereditary", "The Witch", "Get Out", "The Shining", "Midsommar"],
    },
    "musical": {
        "title": "The Musical Maven",
        "tagline": "When the singing starts, you're already on your feet.",
        "summary": "You love a film where emotion becomes song, and a single number can carry the whole story. You appreciate choreography, melody, and the kind of theatricality that would feel ridiculous if it weren't so right. Cut to the chorus.",
        "films": ["Chicago", "Moulin Rouge!", "The Greatest Showman", "La La Land", "West Side Story (2021)"],
    },
}


def get_or_init_answers():
    answers = session.get("answers")
    if answers is None:
        answers = []
        session["answers"] = answers
    return answers


@app.route("/", methods=["GET"])
def home():
    session.clear()
    return redirect(url_for("question", q=1))


@app.route("/question/<int:q>", methods=["GET", "POST"])
def question(q):
    if q < 1 or q > len(QUESTIONS):
        return redirect(url_for("home"))

    answers = get_or_init_answers()

    if request.method == "POST":
        chosen = request.form.get("choice")
        valid_categories = {cat for _, _, cat in QUESTIONS[q - 1]["options"]}
        if chosen not in valid_categories:
            return render_template_string(
                QUESTION_TEMPLATE,
                q_data=QUESTIONS[q - 1],
                q_num=q,
                total=len(QUESTIONS),
                last_answer=answers[-1] if answers else None,
                error="Please pick one of the options before moving on.",
            )
        while len(answers) < q:
            answers.append(None)
        answers[q - 1] = chosen
        session["answers"] = answers
        if q >= len(QUESTIONS):
            return redirect(url_for("result"))
        return redirect(url_for("question", q=q + 1))

    last_answer = answers[-1] if answers and len(answers) >= q - 1 else None
    if last_answer is None and answers and q - 1 < len(answers):
        last_answer = answers[q - 2] if q - 2 >= 0 else None

    return render_template_string(
        QUESTION_TEMPLATE,
        q_data=QUESTIONS[q - 1],
        q_num=q,
        total=len(QUESTIONS),
        last_answer=answers[-1] if answers else None,
        error=None,
    )


@app.route("/result", methods=["GET"])
def result():
    answers = get_or_init_answers()
    if len(answers) < len(QUESTIONS) or any(a is None for a in answers):
        return redirect(url_for("question", q=len(answers) + 1))

    tally = {}
    for cat in answers:
        tally[cat] = tally.get(cat, 0) + 1
    top_cat = max(tally, key=tally.get)
    profile = RESULT_COPY[top_cat]

    history = []
    for idx, ans in enumerate(answers, start=1):
        history.append((idx, QUESTIONS[idx - 1]["question"], ans))

    return render_template_string(
        RESULT_TEMPLATE,
        profile=profile,
        tally=sorted(tally.items(), key=lambda kv: kv[1], reverse=True),
        top=top_cat,
        history=history,
        total=len(QUESTIONS),
    )


QUESTION_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Movie Type Quiz — Question {{ q_num }}</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: radial-gradient(circle at top, #1f1c3a 0%, #0a0a14 70%);
      color: #f5f5fa;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .card {
      width: 100%;
      max-width: 640px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 32px;
      backdrop-filter: blur(10px);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
    }
    .progress {
      font-size: 13px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #9d9bb5;
      margin-bottom: 8px;
    }
    .bar {
      height: 4px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      overflow: hidden;
      margin-bottom: 28px;
    }
    .bar > span {
      display: block;
      height: 100%;
      background: linear-gradient(90deg, #ff7e5f, #feb47b);
      width: {{ (q_num / total * 100) | round(1) }}%;
    }
    h1 {
      font-size: 26px;
      line-height: 1.3;
      margin: 0 0 12px;
    }
    .context {
      font-size: 14px;
      color: #b9b6d3;
      background: rgba(255, 255, 255, 0.04);
      border-left: 3px solid #ff7e5f;
      padding: 10px 14px;
      border-radius: 6px;
      margin-bottom: 20px;
    }
    .context strong { color: #ffd0bd; }
    .options { display: grid; gap: 12px; margin-top: 8px; }
    label.opt {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      padding: 14px 16px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.15s ease;
      background: rgba(255, 255, 255, 0.02);
    }
    label.opt:hover {
      border-color: #ff7e5f;
      background: rgba(255, 126, 95, 0.08);
      transform: translateY(-1px);
    }
    label.opt input { margin-top: 4px; accent-color: #ff7e5f; }
    label.opt .letter {
      flex: 0 0 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      display: grid;
      place-items: center;
      font-weight: 600;
      font-size: 13px;
    }
    label.opt .text { flex: 1; line-height: 1.4; }
    button {
      margin-top: 24px;
      width: 100%;
      padding: 14px;
      background: linear-gradient(90deg, #ff7e5f, #feb47b);
      color: #0a0a14;
      border: none;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 600;
      letter-spacing: 0.04em;
      cursor: pointer;
      transition: transform 0.1s ease, box-shadow 0.15s ease;
    }
    button:hover { transform: translateY(-1px); box-shadow: 0 10px 24px rgba(255, 126, 95, 0.25); }
    .error {
      color: #ff9b8a;
      font-size: 14px;
      margin-top: 12px;
    }
  </style>
</head>
<body>
  <form class="card" method="post" action="{{ url_for('question', q=q_num) }}">
    <div class="progress">Question {{ q_num }} of {{ total }}</div>
    <div class="bar"><span></span></div>

    {% if last_answer and q_num > 1 %}
      <div class="context">
        Last page, you leaned <strong>{{ last_answer }}</strong>. We'll keep that in mind.
      </div>
    {% endif %}

    <h1>{{ q_data.question }}</h1>

    <div class="options">
      {% for letter, text, cat in q_data.options %}
        <label class="opt">
          <input type="radio" name="choice" value="{{ cat }}" required />
          <span class="letter">{{ letter }}</span>
          <span class="text">{{ text }}</span>
        </label>
      {% endfor %}
    </div>

    {% if error %}
      <div class="error">{{ error }}</div>
    {% endif %}

    <button type="submit">
      {% if q_num == total %}See My Result{% else %}Next Question →{% endif %}
    </button>
  </form>
</body>
</html>
"""

RESULT_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Your Movie Type — Results</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: radial-gradient(circle at top, #1f1c3a 0%, #0a0a14 70%);
      color: #f5f5fa;
      padding: 32px 24px;
    }
    .wrap { max-width: 720px; margin: 0 auto; }
    .card {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 36px;
      backdrop-filter: blur(10px);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
    }
    .eyebrow {
      font-size: 12px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #ffb39a;
    }
    h1 { font-size: 36px; margin: 6px 0 4px; }
    .tagline { color: #b9b6d3; font-style: italic; margin-bottom: 22px; }
    .summary { line-height: 1.6; color: #e6e3f5; }
    h2 { margin-top: 32px; font-size: 18px; letter-spacing: 0.06em; text-transform: uppercase; color: #ffb39a; }
    .films { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
    .film {
      background: rgba(255, 126, 95, 0.12);
      border: 1px solid rgba(255, 126, 95, 0.35);
      padding: 6px 12px;
      border-radius: 999px;
      font-size: 13px;
    }
    .tally { display: grid; gap: 6px; margin-top: 12px; }
    .tally .row {
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      padding: 6px 10px;
      background: rgba(255, 255, 255, 0.04);
      border-radius: 8px;
    }
    .tally .row.top { border: 1px solid #ff7e5f; }
    details { margin-top: 28px; }
    summary { cursor: pointer; color: #ffb39a; font-size: 14px; }
    ol.history { margin-top: 10px; padding-left: 20px; line-height: 1.5; font-size: 14px; color: #cfcde0; }
    a.again {
      display: inline-block;
      margin-top: 28px;
      padding: 12px 22px;
      background: linear-gradient(90deg, #ff7e5f, #feb47b);
      color: #0a0a14;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <div class="eyebrow">You are</div>
      <h1>{{ profile.title }}</h1>
      <div class="tagline">"{{ profile.tagline }}"</div>
      <p class="summary">{{ profile.summary }}</p>

      <h2>Films for you</h2>
      <div class="films">
        {% for f in profile.films %}<span class="film">{{ f }}</span>{% endfor %}
      </div>

      <h2>Your genre breakdown</h2>
      <div class="tally">
        {% for cat, count in tally %}
          <div class="row {% if cat == top %}top{% endif %}">
            <span>{{ cat }}{% if cat == top %} (top match){% endif %}</span>
            <span>{{ count }} / {{ total }}</span>
          </div>
        {% endfor %}
      </div>

      <details>
        <summary>See how you answered ({{ total }} questions)</summary>
        <ol class="history">
          {% for idx, q_text, ans in history %}
            <li><strong>{{ ans }}</strong> — {{ q_text }}</li>
          {% endfor %}
        </ol>
      </details>

      <a class="again" href="{{ url_for('home') }}">Take it again</a>
    </div>
  </div>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)

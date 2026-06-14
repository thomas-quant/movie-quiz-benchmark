from flask import Flask, session, redirect, url_for, request, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

QUESTIONS = [
    {
        "question": "Which genre is known as the 'King of Bollywood' in Indian cinema?",
        "options": ["Action", "Romance", "Comedy", "Drama"],
        "answer": "Romance",
        "context": "Bollywood is synonymous with romantic musicals."
    },
    {
        "question": "The 1977 film 'Star Wars' is most closely associated with which genre?",
        "options": ["Western", "Science Fiction", "Horror", "Musical"],
        "answer": "Science Fiction",
        "context": "Star Wars revolutionized sci-fi cinema with its space opera format."
    },
    {
        "question": "Which genre features stories where the protagonist is typically placed in a dangerous or unsettling environment?",
        "options": ["Romance", "Comedy", "Thriller", "Documentary"],
        "answer": "Thriller",
        "context": "Thrillers keep audiences on edge with suspense and tension."
    },
    {
        "question": "Film Noir is characterized by which visual style?",
        "options": ["Bright, saturated colors", "High contrast black and white", "Sepia tones", "Neon lighting"],
        "answer": "High contrast black and white",
        "context": "Film Noir emerged in the 1940s with its distinctive chiaroscuro lighting."
    },
    {
        "question": "Which genre does NOT typically use found footage as a storytelling technique?",
        "options": ["Horror", "Documentary", "Romance", "Sci-Fi"],
        "answer": "Romance",
        "context": "Found footage is a technique mainly in horror and mockumentary films."
    },
    {
        "question": "Martial arts films originated primarily from which country?",
        "options": ["Japan", "Hong Kong", "India", "South Korea"],
        "answer": "Hong Kong",
        "context": "Hong Kong cinema popularized martial arts films globally in the 1960s-80s."
    },
    {
        "question": "Which genre is often called 'the oldest genre of film'?",
        "options": ["Silent", "Documentary", "Action", "Animation"],
        "answer": "Documentary",
        "context": "Documentaries date back to the earliest days of cinema in the 1890s."
    },
    {
        "question": "A 'whodunit' is a sub-genre of which main genre?",
        "options": ["Comedy", "Mystery", "Horror", "Western"],
        "answer": "Mystery",
        "context": "Whodunits focus on solving a crime, typically a murder."
    },
    {
        "question": "Which genre is known for its use of 'jump scares'?",
        "options": ["Romance", "Horror", "Musical", "Animation"],
        "answer": "Horror",
        "context": "Jump scares are sudden audio-visual shocks designed to startle audiences."
    },
    {
        "question": "The French New Wave movement is considered a sub-genre of which main category?",
        "options": ["Action", "Art House", "Comedy", "Thriller"],
        "answer": "Art House",
        "context": "French New Wave films broke traditional filmmaking conventions in the late 1950s."
    },
    {
        "question": "Which genre typically features a 'chosen one' narrative?",
        "options": ["Documentary", "Fantasy", "Romance", "Western"],
        "answer": "Fantasy",
        "context": "The 'chosen one' trope is a staple of fantasy storytelling."
    },
    {
        "question": "The 'screwball comedy' peaked in popularity during which decade?",
        "options": ["1920s", "1930s-1940s", "1960s", "1980s"],
        "answer": "1930s-1940s",
        "context": "Screwball comedies featured fast-paced dialogue and battle-of-the-sexes themes."
    },
    {
        "question": "Which genre does the film 'The Blair Witch Project' belong to?",
        "options": ["Documentary", "Found Footage Horror", "Drama", "Comedy"],
        "answer": "Found Footage Horror",
        "context": "The Blair Witch Project popularized the found footage horror sub-genre."
    },
    {
        "question": "Spaghetti Westerns were primarily produced in which country?",
        "options": ["USA", "Italy", "Mexico", "Spain"],
        "answer": "Italy",
        "context": "Italian directors like Sergio Leone created the Spaghetti Western sub-genre."
    },
    {
        "question": "Which genre is characterized by improvised dialogue and naturalistic acting?",
        "options": ["Musical", "Indie Drama", "Action", "Animation"],
        "answer": "Indie Drama",
        "context": "Indie dramas often favor authenticity over scripted performances."
    },
    {
        "question": "The 'J-horror' sub-genre originated from which country?",
        "options": ["Japan", "China", "Thailand", "South Korea"],
        "answer": "Japan",
        "context": "J-horror (Japanese horror) became globally influential in the late 1990s."
    },
    {
        "question": "Which genre does NOT typically feature a love interest subplot?",
        "options": ["Action", "Comedy", "Documentary", "Drama"],
        "answer": "Documentary",
        "context": "Documentaries aim for factual storytelling, not romantic subplots."
    },
    {
        "question": "The 'kaiju' genre originated from which country?",
        "options": ["USA", "Japan", "China", "South Korea"],
        "answer": "Japan",
        "context": "Kaiju means 'strange beast' — Godzilla is the most famous example."
    },
    {
        "question": "Which genre is most associated with the term 'mise-en-scène'?",
        "options": ["Action", "Art House", "Comedy", "Animation"],
        "answer": "Art House",
        "context": "Art house cinema emphasizes visual composition and directorial vision."
    },
    {
        "question": "The 'revenge film' sub-genre is prominent in which main genre?",
        "options": ["Romance", "Action/Thriller", "Comedy", "Musical"],
        "answer": "Action/Thriller",
        "context": "Revenge narratives like Kill Bill blend action with thriller elements."
    },
    {
        "question": "Which genre typically uses a 'narrator' device to tell the story?",
        "options": ["Documentary", "Action", "Horror", "Musical"],
        "answer": "Documentary",
        "context": "Documentaries frequently use narration to guide the viewer."
    },
    {
        "question": "The 'slasher' sub-genre peaked during which decade?",
        "options": ["1960s", "1970s-1980s", "1990s", "2000s"],
        "answer": "1970s-1980s",
        "context": "Friday the 13th, Halloween, and Nightmare on Elm Street defined this era."
    },
    {
        "question": "Which genre does the film 'Napoleon Dynamite' primarily belong to?",
        "options": ["Action", "Indie Comedy", "Drama", "Romance"],
        "answer": "Indie Comedy",
        "context": "Napoleon Dynamite is a cult classic indie comedy from 2004."
    },
    {
        "question": "Which genre is known for its use of 'long takes' and minimal editing?",
        "options": ["Action", "Art House", "Comedy", "Musical"],
        "answer": "Art House",
        "context": "Art house directors often use extended takes for immersive storytelling."
    },
    {
        "question": "The 'giallo' genre is a blend of which two main genres?",
        "options": ["Comedy + Drama", "Horror + Mystery", "Action + Sci-Fi", "Romance + Musical"],
        "answer": "Horror + Mystery",
        "context": "Giallo is an Italian genre mixing horror thrills with mystery plotting."
    },
    {
        "question": "Which genre typically features non-linear storytelling?",
        "options": ["Musical", "Indie Drama", "Animation", "Western"],
        "answer": "Indie Drama",
        "context": "Films like Pulp Fiction and Memento popularized non-linear narratives."
    },
    {
        "question": "The 'mockumentary' is a parody of which genre?",
        "options": ["Horror", "Documentary", "Action", "Sci-Fi"],
        "answer": "Documentary",
        "context": "Mockumentaries like The Office imitate documentary filmmaking style."
    },
    {
        "question": "Which genre is known for its 'chase scenes' as a defining element?",
        "options": ["Romance", "Action", "Musical", "Documentary"],
        "answer": "Action",
        "context": "Chase sequences are a hallmark of action cinema."
    },
    {
        "question": "Which genre does the film 'Blade Runner' primarily belong to?",
        "options": ["Fantasy", "Cyberpunk/Sci-Fi", "Horror", "Western"],
        "answer": "Cyberpunk/Sci-Fi",
        "context": "Blade Runner is a defining cyberpunk film set in a dystopian future."
    },
    {
        "question": "Which genre is most associated with the 'unreliable narrator' technique?",
        "options": ["Action", "Psychological Thriller", "Comedy", "Musical"],
        "answer": "Psychological Thriller",
        "context": "Films like Fight Club and Shutter Island use unreliable narrators."
    },
    {
        "question": "The 'exploitation film' sub-genre is known for what characteristic?",
        "options": ["High production values", "Provocative or sensational content", "Musical numbers", "Historical accuracy"],
        "answer": "Provocative or sensational content",
        "context": "Exploitation films push boundaries for shock value and entertainment."
    },
    {
        "question": "Which genre does NOT typically feature a clear protagonist-antagonist dynamic?",
        "options": ["Action", "Documentary", "Drama", "Horror"],
        "answer": "Documentary",
        "context": "Documentaries often present multiple perspectives without a clear hero-villain dynamic."
    },
    {
        "question": "Which genre is most associated with 'neo-noir' films like 'Blade Runner 2049'?",
        "options": ["Comedy", "Science Fiction/Film Noir", "Musical", "Animation"],
        "answer": "Science Fiction/Film Noir",
        "context": "Neo-noir updates classic noir with modern settings and sci-fi elements."
    },
    {
        "question": "Which genre does the film 'Parasite' primarily belong to?",
        "options": ["Comedy", "Thriller/Drama", "Action", "Horror"],
        "answer": "Thriller/Drama",
        "context": "Parasite blends social commentary with thriller elements, winning Best Picture in 2020."
    },
]

@app.route("/")
def index():
    session.clear()
    session["current"] = 0
    session["score"] = 0
    session["answers"] = []
    return render_template_string(START_TEMPLATE)

@app.route("/question/<int:qnum>", methods=["GET", "POST"])
def question(qnum):
    if qnum >= len(QUESTIONS):
        return redirect(url_for("results"))

    if "current" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        chosen = request.form.get("answer")
        correct = QUESTIONS[qnum]["answer"]
        is_correct = chosen == correct

        if is_correct:
            session["score"] = session.get("score", 0) + 1

        session.setdefault("answers", []).append({
            "question": qnum,
            "chosen": chosen,
            "correct": correct,
            "is_correct": is_correct
        })
        session["current"] = qnum + 1
        session.modified = True

        return render_template_string(
            FEEDBACK_TEMPLATE,
            qnum=qnum,
            correct=is_correct,
            chosen=chosen,
            correct_answer=correct,
            explanation=QUESTIONS[qnum]["context"],
            next_num=qnum + 1
        )

    total = len(QUESTIONS)
    q = QUESTIONS[qnum]
    return render_template_string(
        QUESTION_TEMPLATE,
        qnum=qnum,
        total=total,
        question=q["question"],
        options=q["options"],
        score=session.get("score", 0),
        context_hint=QUESTIONS[max(0, qnum - 1)]["context"] if qnum > 0 else None
    )

@app.route("/results")
def results():
    answers = session.get("answers", [])
    score = session.get("score", 0)
    total = len(QUESTIONS)
    return render_template_string(
        RESULTS_TEMPLATE,
        score=score,
        total=total,
        answers=answers,
        questions=QUESTIONS
    )

START_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Genre Quiz</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e0e0e0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 3rem;
            max-width: 520px;
            width: 90%;
            text-align: center;
        }
        h1 { font-size: 2rem; margin-bottom: 0.5rem; color: #e94560; }
        .subtitle { color: #aaa; margin-bottom: 2rem; font-size: 1.05rem; }
        .genre-icons { font-size: 2.5rem; margin: 1rem 0; letter-spacing: 0.5rem; }
        .btn {
            display: inline-block;
            background: #e94560;
            color: white;
            padding: 0.9rem 2.5rem;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.2s, transform 0.1s;
        }
        .btn:hover { background: #c73a52; transform: translateY(-1px); }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎬 Movie Genre Quiz</h1>
        <p class="subtitle">Test your knowledge of cinema genres</p>
        <div class="genre-icons">🎭 🎥 🎬 🍿</div>
        <p style="margin-bottom: 2rem; color: #ccc;">{{ total if total is defined else 34 }} questions about the diverse world of movie genres — from Film Noir to J-Horror.</p>
        <a href="/question/0" class="btn">Start Quiz</a>
    </div>
</body>
</html>
"""

QUESTION_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question {{ qnum + 1 }} of {{ total }}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e0e0e0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 2.5rem;
            max-width: 560px;
            width: 90%;
        }
        .progress-bar { background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; margin-bottom: 1.5rem; overflow: hidden; }
        .progress-fill { background: #e94560; height: 100%; border-radius: 10px; transition: width 0.3s; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
        .header h2 { font-size: 1.1rem; color: #aaa; }
        .score-badge { background: rgba(233,69,96,0.2); color: #e94560; padding: 0.3rem 0.8rem; border-radius: 20px; font-weight: bold; font-size: 0.9rem; }
        .question-text { font-size: 1.25rem; margin-bottom: 1.5rem; line-height: 1.5; }
        .options { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 1.5rem; }
        .option-btn {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 10px;
            padding: 1rem 1.2rem;
            color: #e0e0e0;
            font-size: 1rem;
            cursor: pointer;
            text-align: left;
            transition: background 0.2s, border-color 0.2s;
        }
        .option-btn:hover { background: rgba(233,69,96,0.15); border-color: #e94560; }
        .option-btn input { margin-right: 0.75rem; accent-color: #e94560; }
        .submit-btn {
            background: #e94560;
            color: white;
            padding: 0.85rem 2rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s;
        }
        .submit-btn:hover { background: #c73a52; }
        .context-hint {
            background: rgba(255,255,255,0.04);
            border-left: 3px solid #e94560;
            padding: 0.7rem 1rem;
            margin-bottom: 1.5rem;
            border-radius: 0 8px 8px 0;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="progress-bar">
            <div class="progress-fill" style="width: {{ ((qnum) / total * 100)|round }}%"></div>
        </div>
        <div class="header">
            <h2>Question {{ qnum + 1 }} of {{ total }}</h2>
            <span class="score-badge">Score: {{ score }}</span>
        </div>
        {% if context_hint %}
        <div class="context-hint">📖 Previous: {{ context_hint }}</div>
        {% endif %}
        <form method="POST">
            <p class="question-text">{{ question }}</p>
            <div class="options">
                {% for opt in options %}
                <label class="option-btn">
                    <input type="radio" name="answer" value="{{ opt }}" required>
                    {{ opt }}
                </label>
                {% endfor %}
            </div>
            <button type="submit" class="submit-btn">Submit Answer</button>
        </form>
    </div>
</body>
</html>
"""

FEEDBACK_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if correct %}Correct!{% else %}Wrong{% endif %}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e0e0e0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 2.5rem;
            max-width: 520px;
            width: 90%;
            text-align: center;
        }
        .icon { font-size: 3rem; margin-bottom: 1rem; }
        h2 { font-size: 1.5rem; margin-bottom: 1rem; }
        .correct-text { color: #4ecdc4; }
        .wrong-text { color: #e94560; }
        .detail-box {
            background: rgba(255,255,255,0.04);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            text-align: left;
        }
        .detail-box p { margin-bottom: 0.5rem; font-size: 0.95rem; }
        .detail-box .label { color: #aaa; }
        .context { color: #aaa; font-style: italic; margin-bottom: 1.5rem; font-size: 0.9rem; }
        .btn {
            display: inline-block;
            background: #e94560;
            color: white;
            padding: 0.85rem 2rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.2s;
        }
        .btn:hover { background: #c73a52; }
    </style>
</head>
<body>
    <div class="card">
        <div class="icon">{% if correct %}✅{% else %}❌{% endif %}</div>
        <h2 class="{% if correct %}correct-text{% else %}wrong-text{% endif %}">
            {% if correct %}Correct!{% else %}Not quite!{% endif %}
        </h2>
        <div class="detail-box">
            <p><span class="label">Your answer:</span> {{ chosen }}</p>
            {% if not correct %}
            <p><span class="label">Correct answer:</span> {{ correct_answer }}</p>
            {% endif %}
        </div>
        <p class="context">{{ explanation }}</p>
        <a href="/question/{{ next_num }}" class="btn">
            {% if next_num < 34 %}Next Question{% else %}See Results{% endif %}
        </a>
    </div>
</body>
</html>
"""

RESULTS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Results</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e0e0e0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 0;
        }
        .card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 2.5rem;
            max-width: 650px;
            width: 92%;
        }
        .header { text-align: center; margin-bottom: 2rem; }
        .header h1 { font-size: 2rem; color: #e94560; margin-bottom: 0.5rem; }
        .score-big { font-size: 4rem; font-weight: bold; color: #4ecdc4; }
        .score-label { color: #aaa; font-size: 1rem; margin-top: 0.3rem; }
        .grade { font-size: 1.3rem; margin-top: 0.8rem; }
        .answers-list { margin-top: 1.5rem; }
        .answer-row {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.7rem 1rem;
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }
        .answer-row .icon { font-size: 1.1rem; }
        .answer-row .q-text { flex: 1; }
        .answer-row .chosen { color: #aaa; }
        .answer-row.is-correct { border-left: 3px solid #4ecdc4; }
        .answer-row.is-wrong { border-left: 3px solid #e94560; }
        .restart-btn {
            display: block;
            background: #e94560;
            color: white;
            padding: 0.85rem 2rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
            text-align: center;
            margin-top: 2rem;
            transition: background 0.2s;
        }
        .restart-btn:hover { background: #c73a52; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <h1>🎬 Quiz Complete!</h1>
            <div class="score-big">{{ score }}/{{ total }}</div>
            <div class="score-label">questions correct</div>
            <div class="grade">
                {% if score >= total * 0.9 %}
                    🏆 Genre Master!
                {% elif score >= total * 0.7 %}
                    🎥 Cinephile!
                {% elif score >= total * 0.5 %}
                    🍿 Movie Buff
                {% else %}
                    🎬 Room to Grow
                {% endif %}
            </div>
        </div>
        <div class="answers-list">
            {% for a in answers %}
            <div class="answer-row {{ 'is-correct' if a.is_correct else 'is-wrong' }}">
                <span class="icon">{{ '✅' if a.is_correct else '❌' }}</span>
                <span class="q-text">Q{{ a.question + 1 }}</span>
                <span class="chosen">
                    {{ a.chosen }}
                    {% if not a.is_correct %} → {{ a.correct }}{% endif %}
                </span>
            </div>
            {% endfor %}
        </div>
        <a href="/" class="restart-btn">Try Again</a>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)

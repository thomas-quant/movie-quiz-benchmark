from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'movie-quiz-secret-key-change-in-production'

QUESTIONS = [
    {
        "question": "Which film genre is defined by supernatural or paranormal elements beyond scientific explanation?",
        "options": ["Science Fiction", "Horror", "Fantasy", "Thriller"],
        "answer": 2
    },
    {
        "question": "Who directed 'Pulp Fiction'?",
        "options": ["Martin Scorsese", "Quentin Tarantino", "Christopher Nolan", "David Fincher"],
        "answer": 1
    },
    {
        "question": "What does 'film noir' literally mean in French?",
        "options": ["Dark movie", "Black film", "Night cinema", "Shadow picture"],
        "answer": 1
    },
    {
        "question": "Which studio created 'Toy Story', the first fully computer-animated feature film?",
        "options": ["DreamWorks", "Pixar", "Illumination", "Blue Sky Studios"],
        "answer": 1
    },
    {
        "question": "What is the highest-grossing film of all time (unadjusted for inflation)?",
        "options": ["Titanic", "Avengers: Endgame", "Avatar", "Star Wars: The Force Awakens"],
        "answer": 2
    },
    {
        "question": "Which film is credited with pioneering the 'spy thriller' genre in 1962?",
        "options": ["The Man from U.N.C.L.E.", "Mission: Impossible", "Dr. No", "The Bourne Identity"],
        "answer": 2
    },
    {
        "question": "What subgenre of horror involves slow-building psychological dread rather than graphic violence?",
        "options": ["Slasher", "Gore", "Psychological horror", "Body horror"],
        "answer": 2
    },
    {
        "question": "Which director is known for the 'Dark Knight' Batman trilogy?",
        "options": ["Zack Snyder", "Christopher Nolan", "Tim Burton", "Matt Reeves"],
        "answer": 1
    },
    {
        "question": "What type of film combines live action with animated characters?",
        "options": ["Stop-motion", "Rotoscoping", "Motion capture", "Hybrid animation"],
        "answer": 3
    },
    {
        "question": "Which film won the first Academy Award for Best Picture in 1929?",
        "options": ["The Jazz Singer", "Wings", "Sunrise", "The Broadway Melody"],
        "answer": 1
    },
    {
        "question": "What does 'auteur theory' suggest about filmmakers?",
        "options": ["They write scripts only", "They are the primary creative force", "They work alone", "They avoid budgets"],
        "answer": 1
    },
    {
        "question": "Which streaming service produced 'Stranger Things'?",
        "options": ["Amazon Prime", "Hulu", "Netflix", "Disney+"],
        "answer": 2
    },
    {
        "question": "What is a 'mockumentary'?",
        "options": ["A fake documentary", "A documentary about models", "An animated documentary", "A short documentary"],
        "answer": 0
    },
    {
        "question": "Which 1999 film is considered a breakthrough for cyberpunk cinema?",
        "options": ["The Matrix", "Blade Runner", "Johnny Mnemonic", "Dark City"],
        "answer": 0
    },
    {
        "question": "What film technique involves showing the same scene from multiple angles with different focus?",
        "options": ["Cross-cutting", "Rack focus", "Split screen", "Montage"],
        "answer": 1
    },
    {
        "question": "Who directed 'Schindler's List' in 1993?",
        "options": ["Roman Polanski", "Steven Spielberg", "Martin Scorsese", "Francis Ford Coppola"],
        "answer": 1
    },
    {
        "question": "What subgenre features comedic treatment of serious topics?",
        "options": ["Parody", "Dramedy", "Satire", "Spoof"],
        "answer": 1
    },
    {
        "question": "Which studio is known for the 'Harry Potter' film series?",
        "options": ["Warner Bros.", "Universal", "Paramount", "Sony Pictures"],
        "answer": 0
    },
    {
        "question": "What is 'color grading'?",
        "options": ["Coloring by numbers", "Digital color correction", "Choosing costume colors", "Film development"],
        "answer": 1
    },
    {
        "question": "Which 1975 film established the 'slasher' genre?",
        "options": ["Halloween", "Friday the 13th", "The Texas Chainaw Massacre", "A Nightmare on Elm Street"],
        "answer": 0
    },
    {
        "question": "What does 'post-production' refer to?",
        "options": ["Sequel filming", "Editing and effects after filming", "Promotion after release", "Director's commentary"],
        "answer": 1
    },
    {
        "question": "Which director is famous for long takes and tracking shots?",
        "options": ["Michael Bay", "Alfonso Cuarón", "J.J. Abrams", "James Cameron"],
        "answer": 1
    },
    {
        "question": "What is a 'western' film set in the American Old West. Which state is it named after in a famous film title?",
        "options": ["Texas", "Arizona", "Oklahoma", "Colorado"],
        "answer": 0
    },
    {
        "question": "Which franchise features 'The Force'?",
        "options": ["Star Trek", "Star Wars", "The Terminator", "Guardians of the Galaxy"],
        "answer": 1
    },
    {
        "question": "What is the 'McGuffin' in filmmaking?",
        "options": ["A camera trick", "An object driving the plot", "A sound effect", "A director's choice"],
        "answer": 1
    },
    {
        "question": "Who played Jack in 'Titanic' (1997)?",
        "options": ["Brad Pitt", "Tom Cruise", "Leonardo DiCaprio", "Johnny Depp"],
        "answer": 2
    },
    {
        "question": "What does 'CGI' stand for in modern filmmaking?",
        "options": ["Computer Generated Images", "Central Graphic Interface", "Cinema Graphics International", "Computer Graphics Integration"],
        "answer": 0
    },
    {
        "question": "Which country is the origin of 'Dogme 95' filmmaking movement?",
        "options": ["France", "Italy", "Denmark", "Sweden"],
        "answer": 2
    },
    {
        "question": "What is an 'elevator pitch' in film production?",
        "options": ["A film about elevators", "A short summary of a film", "An audition scene", "A camera movement"],
        "answer": 1
    },
    {
        "question": "Which director directed 'Inception' and 'Interstellar'?",
        "options": ["Denis Villeneuve", "Christopher Nolan", "Ridley Scott", "Darryn"],
        "answer": 1
    }
]


@app.route('/')
def index():
    if 'current_question' not in session:
        session['current_question'] = 0
        session['answers'] = []
        session['score'] = 0
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    session['current_question'] = 0
    session['answers'] = []
    session['score'] = 0
    return redirect(url_for('question'))


@app.route('/question')
def question():
    q_index = session.get('current_question', 0)
    if q_index >= len(QUESTIONS):
        return redirect(url_for('results'))
    
    q = QUESTIONS[q_index]
    return render_template(
        'question.html',
        question=q,
        q_index=q_index,
        total=len(QUESTIONS)
    )


@app.route('/answer', methods=['POST'])
def answer():
    q_index = session.get('current_question', 0)
    selected = int(request.form.get('answer', -1))
    
    answers = session.get('answers', [])
    answers.append(selected)
    session['answers'] = answers
    
    q = QUESTIONS[q_index]
    if selected == q['answer']:
        session['score'] = session.get('score', 0) + 1
    
    session['current_question'] = q_index + 1
    
    return render_template(
        'feedback.html',
        question=q,
        selected=selected,
        q_index=q_index,
        total=len(QUESTIONS)
    )


@app.route('/next', methods=['POST'])
def next_question():
    return redirect(url_for('question'))


@app.route('/results')
def results():
    score = session.get('score', 0)
    total = len(QUESTIONS)
    answers = session.get('answers', [])
    percentage = int((score / total) * 100)
    
    if percentage >= 90:
        message = "Outstanding! You're a true cinephile!"
    elif percentage >= 70:
        message = "Great job! You know your movies!"
    elif percentage >= 50:
        message = "Not bad! Keep watching films!"
    else:
        message = "Time to binge some movies!"
    
    return render_template(
        'results.html',
        score=score,
        total=total,
        percentage=percentage,
        message=message,
        questions=QUESTIONS,
        answers=answers
    )


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
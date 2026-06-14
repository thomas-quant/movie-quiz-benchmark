from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

QUESTIONS = [
    {
        "question": "Which film is often credited as the first feature-length motion picture?",
        "options": ["The Great Train Robbery", "The Birth of a Nation", "Queer", "The Story of the Kelly Gang"],
        "answer": 2
    },
    {
        "question": "Who directed 'Pulp Fiction'?",
        "options": ["Martin Scorsese", "Quentin Tarantino", "David Fincher", "Christopher Nolan"],
        "answer": 1
    },
    {
        "question": "What was the first Pixar movie released in theaters?",
        "options": ["A Bug's Life", "Toy Story", "Finding Nemo", "Monsters, Inc."],
        "answer": 1
    },
    {
        "question": "Which movie features the quote 'Here's looking at you, kid'?",
        "options": ["Citizen Kane", "Casablanca", "Gone with the Wind", "The Maltese Falcon"],
        "answer": 1
    },
    {
        "question": "Who played The Joker in 'The Dark Knight'?",
        "options": ["Jack Nicholson", "Jared Leto", "Heath Ledger", "Joaquin Phoenix"],
        "answer": 2
    },
    {
        "question": "What film won the first Academy Award for Best Picture?",
        "options": ["Wings", "Sunrise", "7th Heaven", "The Jazz Singer"],
        "answer": 0
    },
    {
        "question": "Which director is known for the 'Lord of the Rings' trilogy?",
        "options": ["Steven Spielberg", "Peter Jackson", "James Cameron", "Ridley Scott"],
        "answer": 1
    },
    {
        "question": "In what year was the first 'Star Wars' movie released?",
        "options": ["1975", "1977", "1979", "1980"],
        "answer": 1
    },
    {
        "question": "Who directed 'Psycho' (1960)?",
        "options": ["Alfred Hitchcock", "Billy Wilder", "Orson Welles", "John Ford"],
        "answer": 0
    },
    {
        "question": "Which film is the highest-grossing of all time (unadjusted)?",
        "options": ["Titanic", "Avatar", "Avengers: Endgame", "Star Wars: The Force Awakens"],
        "answer": 1
    },
    {
        "question": "Who played Forrest Gump?",
        "options": ["Tom Hanks", "Robin Williams", "Bill Murray", "Jim Carrey"],
        "answer": 0
    },
    {
        "question": "Which studio produced 'Frozen'?",
        "options": ["DreamWorks", "Pixar", "Disney", "Illumination"],
        "answer": 2
    },
    {
        "question": "What is the name of the fictional African country in 'Black Panther'?",
        "options": ["Wakanda", "Zamunda", "Genovia", "Latveria"],
        "answer": 0
    },
    {
        "question": "Who directed 'Schindler's List'?",
        "options": ["Roman Polanski", "Steven Spielberg", "Martin Scorsese", "Francis Ford Coppola"],
        "answer": 1
    },
    {
        "question": "Which actor played Iron Man in the Marvel Cinematic Universe?",
        "options": ["Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Mark Ruffalo"],
        "answer": 2
    },
    {
        "question": "What was the first movie to feature a fully computer-generated main character?",
        "options": ["Toy Story", "Shrek", "Final Fantasy: The Spirits Within", "A Bug's Life"],
        "answer": 0
    },
    {
        "question": "Who directed 'Inception'?",
        "options": ["Christopher Nolan", "Denis Villeneuve", "Darren Aronofsky", "David Fincher"],
        "answer": 0
    },
    {
        "question": "Which film features the character Hannibal Lecter?",
        "options": ["Se7en", "The Silence of the Lambs", "Manhunter", "The Silence of the Lambs and Manhunter"],
        "answer": 3
    },
    {
        "question": "What is the longest film to win Best Picture at the Oscars?",
        "options": ["Gone with the Wind", "The Godfather Part II", "Lawrence of Arabia", "Ben-Hur"],
        "answer": 0
    },
    {
        "question": "Who played Jack in 'Titanic'?",
        "options": ["Brad Pitt", "Leonardo DiCaprio", "Johnny Depp", "Matt Damon"],
        "answer": 1
    },
    {
        "question": "Which movie popularized the phrase 'May the Force be with you'?",
        "options": ["The Empire Strikes Back", "A New Hope", "Return of the Jedi", "The Force Awakens"],
        "answer": 1
    },
    {
        "question": "Who directed 'The Shining'?",
        "options": ["Roman Polanski", "Stanley Kubrick", "Wes Craven", "Mike Flanagan"],
        "answer": 1
    },
    {
        "question": "What film earned Meryl Streep her first Oscar?",
        "options": ["Sophie's Choice", "The Iron Lady", "Kramer vs. Kramer", "The Devil Wears Prada"],
        "answer": 2
    },
    {
        "question": "Which actor played The Terminator?",
        "options": ["Sylvester Stallone", "Arnold Schwarzenegger", "Bruce Willis", "Keanu Reeves"],
        "answer": 1
    },
    {
        "question": "What was the first superhero movie to win a Best Picture Oscar nomination?",
        "options": ["The Dark Knight", "Black Panther", "Logan", "Wonder Woman"],
        "answer": 1
    },
    {
        "question": "Who directed 'Fight Club'?",
        "options": ["David Fincher", "Darren Aronofsky", "Sam Mendes", "Richard Kelly"],
        "answer": 0
    },
    {
        "question": "Which film is based on a Stephen King novel about a clown?",
        "options": ["Creepshow", "It", "The Dark Half", "Pet Sematary"],
        "answer": 1
    },
    {
        "question": "Who played Neo in 'The Matrix'?",
        "options": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving"],
        "answer": 0
    },
    {
        "question": "What studio made 'The Lion King' (1994)?",
        "options": ["Pixar", "DreamWorks", "Disney", "Blue Sky Studios"],
        "answer": 2
    },
    {
        "question": "Who directed 'Jaws'?",
        "options": ["Steven Spielberg", "George Lucas", "John Carpenter", "James Cameron"],
        "answer": 0
    },
    {
        "question": "Which film features the line 'You can't handle the truth'?",
        "options": ["Top Gun", "A Few Good Men", "The Firm", "Jerry Maguire"],
        "answer": 1
    }
]

@app.route('/')
def index():
    session.clear()
    session['score'] = 0
    session['question_index'] = 0
    return render_template('start.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'question_index' not in session:
        return redirect(url_for('index'))
    
    current_index = session['question_index']
    
    if request.method == 'POST':
        selected_answer = int(request.form.get('answer', -1))
        correct_answer = QUESTIONS[current_index]['answer']
        
        if selected_answer == correct_answer:
            session['score'] = session.get('score', 0) + 1
        
        current_index += 1
        
        if current_index >= len(QUESTIONS):
            final_score = session.get('score', 0)
            return render_template('result.html', score=final_score, total=len(QUESTIONS))
        
        session['question_index'] = current_index
    
    question_data = QUESTIONS[current_index]
    return render_template(
        'question.html',
        question=question_data['question'],
        options=question_data['options'],
        question_number=current_index + 1,
        total=len(QUESTIONS)
    )

if __name__ == '__main__':
    app.run(debug=True)
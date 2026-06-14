from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'movie_quiz_secret_key_123'

QUESTIONS = [
    {"question": "Which film genre typically features extraterrestrial or supernatural beings as antagonists?", "options": ["Horror", "Sci-Fi", "Western", "Musical"], "answer": "Horror"},
    {"question": "What type of movie is 'Die Hard' classified as?", "options": ["Romance", "Action", "Documentary", "Animation"], "answer": "Action"},
    {"question": "A film that uses music and songs to advance the plot is called a:", "options": ["Drama", "Musical", "Documentary", "Thriller"], "answer": "Musical"},
    {"question": "What genre is known for evoking fear, dread, or unease in viewers?", "options": ["Comedy", "Horror", "Romance", "Sport"], "answer": "Horror"},
    {"question": "Which genre explores themes of good versus evil in a futuristic or sci-fi setting?", "options": ["Western", "Film Noir", "Sci-Fi", "Romance"], "answer": "Sci-Fi"},
    {"question": "What do we call a film that makes use of extensive visual effects and fantastical imagery?", "options": ["Drama", "Fantasy", "Documentary", "Crime"], "answer": "Fantasy"},
    {"question": "Films that tell a story with animals as main characters, often animated, are known as:", "options": ["Biopic", "Animation", "War", "Sport"], "answer": "Animation"},
    {"question": "A movie focusing on a person's life story is called a:", "options": ["Thriller", "Biopic", "Comedy", "Horror"], "answer": "Biopic"},
    {"question": "What genre involves stories about legal disputes, courts, and lawyers?", "options": ["Crime", "Drama", "Courtroom Drama", "Western"], "answer": "Courtroom Drama"},
    {"question": "Which genre features stories set in the American Old West with cowboys and gunfights?", "options": ["War", "Western", "Thriller", "Musical"], "answer": "Western"},
    {"question": "Films that aim to educate or inform viewers about real-world topics are called:", "options": ["Drama", "Documentary", "Horror", "Fantasy"], "answer": "Documentary"},
    {"question": "What type of film uses suspense, tension, and unexpected plot twists to keep viewers on edge?", "options": ["Romance", "Comedy", "Thriller", "Sport"], "answer": "Thriller"},
    {"question": "A comedy that focuses on absurd or nonsensical situations is called:", "options": ["Slapstick", "Romance", "Horror", "War"], "answer": "Slapstick"},
    {"question": "Films dealing with romantic relationships and love stories fall under which genre?", "options": ["Drama", "Romance", "Comedy", "Thriller"], "answer": "Romance"},
    {"question": "What genre is characterized by exaggerated, larger-than-life characters and fast-paced action?", "options": ["Drama", "Film Noir", "Action", "Documentary"], "answer": "Action"},
    {"question": "A movie featuring zombies, vampires, or other undead creatures typically belongs to:", "options": ["Sci-Fi", "Horror", "Western", "Musical"], "answer": "Horror"},
    {"question": "Which genre is known for featuring elaborate dance routines and choreography?", "options": ["Horror", "Drama", "Musical", "Thriller"], "answer": "Musical"},
    {"question": "Movies that make you laugh through jokes, witty dialogue, or funny situations are:", "options": ["Horror", "Comedy", "Drama", "War"], "answer": "Comedy"},
    {"question": "What do we call films that depict historical events or figures from the past?", "options": ["Sci-Fi", "Historical Fiction", "Fantasy", "Horror"], "answer": "Historical Fiction"},
    {"question": "A film about a sports event, athlete, or sports industry is classified as:", "options": ["Drama", "Musical", "Sport", "Documentary"], "answer": "Sport"},
    {"question": "Which genre often involves a detective solving a mystery or crime?", "options": ["Romance", "Mystery", "Musical", "Horror"], "answer": "Mystery"},
    {"question": "Animated films featuring superheroes from comic book publishers like Marvel or DC are:", "options": ["Drama", "Superhero", "Western", "Documentary"], "answer": "Superhero"},
    {"question": "What type of film uses dark lighting, moral ambiguity, and cynical themes?", "options": ["Musical", "Film Noir", "Romance", "Comedy"], "answer": "Film Noir"},
    {"question": "Films that take place in space or involve advanced technology are:", "options": ["Fantasy", "Western", "Sci-Fi", "Crime"], "answer": "Sci-Fi"},
    {"question": "A movie that parodies or mocks a specific film, TV show, or genre is called:", "options": ["Documentary", "Parody/Spoof", "Drama", "Horror"], "answer": "Parody/Spoof"},
    {"question": "What genre involves stories about military conflicts and warfare?", "options": ["Romance", "War", "Musical", "Comedy"], "answer": "War"},
    {"question": "Films with a serious tone that explore complex emotional and relational issues are:", "options": ["Comedy", "Horror", "Drama", "Thriller"], "answer": "Drama"},
    {"question": "Which genre features stories where characters enter virtual worlds or simulations?", "options": ["Horror", "Sci-Fi", "Western", "Musical"], "answer": "Sci-Fi"},
    {"question": "A movie combining elements of horror and comedy is called a:", "options": ["Romance", "Comedy Horror", "Musical", "Drama"], "answer": "Comedy Horror"},
    {"question": "Films about espionage, spies, and secret agents fall into which genre?", "options": ["Romance", "Spy/Thriller", "Musical", "Western"], "answer": "Spy/Thriller"},
    {"question": "What type of movie uses stop-motion or CGI to create a world of living, moving creatures?", "options": ["Documentary", "Animation", "Live Action", "Film Noir"], "answer": "Animation"},
    {"question": "A movie depicting events from a famous book or literary work is called:", "options": ["Original Screenplay", "Adaptation", "Remake", "Spin-off"], "answer": "Adaptation"},
    {"question": "Which genre focuses on personal growth, self-discovery, and emotional journeys?", "options": ["Horror", "Coming-of-Age", "War", "Thriller"], "answer": "Coming-of-Age"},
    {"question": "Movies featuring superheroes with extraordinary powers fighting villains are:", "options": ["Western", "Fantasy", "Superhero", "Documentary"], "answer": "Superhero"},
    {"question": "What genre involves stories where animals are the main characters with human-like traits?", "options": ["Documentary", "Animation", "Live Action", "Horror"], "answer": "Animation"},
]


@app.route('/')
def start():
    session.clear()
    session['score'] = 0
    session['answers'] = []
    session['question_index'] = 0
    session['total_questions'] = len(QUESTIONS)
    session['shuffled_questions'] = random.sample(range(len(QUESTIONS)), len(QUESTIONS))
    return render_template('start.html', total=len(QUESTIONS))


@app.route('/question/<int:q_num>')
def question(q_num):
    if 'shuffled_questions' not in session:
        return redirect(url_for('start'))
    
    actual_index = session['shuffled_questions'][q_num]
    q = QUESTIONS[actual_index]
    question_num = q_num + 1
    
    return render_template('question.html', 
                         question=q['question'],
                         options=q['options'],
                         question_num=question_num,
                         total=session['total_questions'],
                         q_num=q_num)


@app.route('/answer/<int:q_num>', methods=['POST'])
def answer(q_num):
    selected = request.form.get('answer')
    actual_index = session['shuffled_questions'][q_num]
    q = QUESTIONS[actual_index]
    
    is_correct = selected == q['answer']
    if is_correct:
        session['score'] = session.get('score', 0) + 1
    
    session['answers'].append({
        'question': q['question'],
        'selected': selected,
        'correct': q['answer'],
        'is_correct': is_correct
    })
    
    session['question_index'] = q_num + 1
    
    if q_num + 1 >= session['total_questions']:
        return redirect(url_for('results'))
    
    return redirect(url_for('question', q_num=q_num + 1))


@app.route('/results')
def results():
    if 'answers' not in session:
        return redirect(url_for('start'))
    
    score = session.get('score', 0)
    total = session.get('total_questions', 0)
    percentage = int((score / total) * 100) if total > 0 else 0
    
    if percentage >= 80:
        grade = "Movie Master!"
    elif percentage >= 60:
        grade = "Film Enthusiast"
    elif percentage >= 40:
        grade = "Casual Viewer"
    else:
        grade = "Cinema Newbie"
    
    return render_template('results.html', 
                         score=score, 
                         total=total, 
                         percentage=percentage,
                         grade=grade,
                         answers=session['answers'])


if __name__ == '__main__':
    app.run(debug=True)

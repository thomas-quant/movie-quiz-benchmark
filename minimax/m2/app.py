from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'moviequizsecretkey123'

QUESTIONS = [
    {
        "question": "Which film genre is known for its focus on fear, anxiety, and suspense?",
        "options": ["Comedy", "Horror", "Documentary", "Western"],
        "answer": 1
    },
    {
        "question": "What genre typically features stories about space, advanced technology, and futuristic settings?",
        "options": ["Western", "Film Noir", "Science Fiction", "Musical"],
        "answer": 2
    },
    {
        "question": "Which genre is characterized by exaggerated, larger-than-life characters and exciting action?",
        "options": ["Drama", "Romance", "Action", "Art House"],
        "answer": 2
    },
    {
        "question": "Films that use songs and dance routines as a natural part of the storytelling belong to which genre?",
        "options": ["Thriller", "Musical", "Horror", "Comedy"],
        "answer": 1
    },
    {
        "question": "What genre traditionally involves investigating crimes and solving mysteries?",
        "options": ["Western", "Mystery", "War", "Animation"],
        "answer": 1
    },
    {
        "question": "Which genre features stories set in the American Old West with cowboys and sheriffs?",
        "options": ["Sci-Fi", "Western", "Film Noir", "Comedy"],
        "answer": 1
    },
    {
        "question": "What type of film aims to educate or inform viewers about real-world topics?",
        "options": ["Horror", "Documentary", "Fantasy", "Adventure"],
        "answer": 1
    },
    {
        "question": "Films that combine comedy with romantic elements fall into which genre?",
        "options": ["Romantic Comedy", "Dark Comedy", "Slapstick", "Parody"],
        "answer": 0
    },
    {
        "question": "Which genre is defined by its use of elaborate, fantastical worlds and magical elements?",
        "options": ["Realism", "Fantasy", "Documentary", "Thriller"],
        "answer": 1
    },
    {
        "question": "What genre typically features fast-paced, physically demanding stunts and sequences?",
        "options": ["Drama", "Action", "Romance", "Silent Film"],
        "answer": 1
    },
    {
        "question": "Films that portray historical events or figures accurately belong to which genre?",
        "options": ["Fantasy", "Historical Fiction", "Horror", "Comedy"],
        "answer": 1
    },
    {
        "question": "Which genre uses shadowy lighting and morally ambiguous characters to create atmosphere?",
        "options": ["Musical", "Film Noir", "Family", "Sports"],
        "answer": 1
    },
    {
        "question": "What genre focuses on personal relationships, emotional conflicts, and character development?",
        "options": ["Action", "Drama", "Horror", "Adventure"],
        "answer": 1
    },
    {
        "question": "Animated films often fall into various genres but commonly include which element?",
        "options": ["Live Action", "Computer-Generated Imagery", "Documentary Footage", "Newsreel"],
        "answer": 1
    },
    {
        "question": "Which genre explores the psychological motivations of criminals?",
        "options": ["Comedy", "Crime", "Musical", "Western"],
        "answer": 1
    },
    {
        "question": "Films about athletes and competitive sports typically belong to which genre?",
        "options": ["Sports", "War", "Sci-Fi", "Horror"],
        "answer": 0
    },
    {
        "question": "What genre involves stories about supernatural forces, ghosts, and the afterlife?",
        "options": ["Comedy", "Fantasy", "Horror", "Documentary"],
        "answer": 2
    },
    {
        "question": "Which genre features improvised dialogue and focuses on everyday life?",
        "options": ["Mumblecore", "Epic", "Film Noir", "Musical"],
        "answer": 0
    },
    {
        "question": "Movies about wars, battles, and military conflicts belong to which genre?",
        "options": ["Romance", "War", "Comedy", "Musical"],
        "answer": 1
    },
    {
        "question": "What genre uses black comedy to address serious topics like death and trauma?",
        "options": ["Romantic Comedy", "Dark Comedy", "Musical", "Family"],
        "answer": 1
    },
    {
        "question": "Which genre parodies other films, TV shows, or cultural phenomena?",
        "options": ["Drama", "Parody", "Documentary", "Western"],
        "answer": 1
    },
    {
        "question": "Films that explore themes of good versus evil with mythological elements fall into which genre?",
        "options": ["Film Noir", "Fantasy", "Reality TV", "News"],
        "answer": 1
    },
    {
        "question": "What genre features exaggerated, physical comedy with slapstick humor?",
        "options": ["Drama", "Slapstick", "Thriller", "Horror"],
        "answer": 1
    },
    {
        "question": "Which genre involves stories about spies, espionage, and secret missions?",
        "options": ["Western", "Comedy", "Spy/Thriller", "Musical"],
        "answer": 2
    },
    {
        "question": "Movies that feature non-professional actors and realistic settings are characteristic of which style?",
        "options": ["Surrealism", "Neo-Realism", "Expressionism", "Germanic"],
        "answer": 1
    },
    {
        "question": "What genre typically involves journeys, quests, and adventurous expeditions?",
        "options": ["Drama", "Adventure", "Documentary", "Horror"],
        "answer": 1
    },
    {
        "question": "Which genre uses surreal imagery and dreamlike sequences to explore the unconscious?",
        "options": ["Comedy", "Surrealism", "Western", "Musical"],
        "answer": 1
    },
    {
        "question": "Films about the Holocaust, World War II, and historical persecution belong to which genre?",
        "options": ["Comedy", "War/Historical", "Musical", "Adventure"],
        "answer": 1
    },
    {
        "question": "What genre combines elements of horror with comedic situations?",
        "options": ["Drama", "Comedy Horror", "Western", "Documentary"],
        "answer": 1
    },
    {
        "question": "Which genre features stories about aliens, monsters, and giant creatures?",
        "options": ["Romance", "Sci-Fi/Kaiju", "Musical", "Western"],
        "answer": 1
    },
    {
        "question": "Movies that reimagine classic literature or mythology in modern settings are known as what?",
        "options": ["Adaptations", "Reimaginings", "Film Noir", "Silent Films"],
        "answer": 1
    },
    {
        "question": "What genre explores the inner thoughts and psychological states of characters?",
        "options": ["Drama", "Psychological Thriller", "Comedy", "Musical"],
        "answer": 1
    },
    {
        "question": "Which genre involves stories about biopics of famous musicians, actors, or artists?",
        "options": ["Documentary", "Biopic", "Western", "Horror"],
        "answer": 1
    },
    {
        "question": "Films featuring robots, artificial intelligence, and technological dystopias belong to which sub-genre?",
        "options": ["Western", "Cyberpunk", "Musical", "Romance"],
        "answer": 1
    },
    {
        "question": "What genre typically involves stories about teenagers and coming-of-age themes?",
        "options": ["Western", "Teen/Coming-of-Age", "Horror", "Documentary"],
        "answer": 1
    },
    {
        "question": "Which genre uses found footage to create a sense of realism and immersion?",
        "options": ["Comedy", "Found Footage", "Musical", "Western"],
        "answer": 1
    },
    {
        "question": "Movies about family relationships, generational stories, and domestic life fall into which genre?",
        "options": ["War", "Family Drama", "Horror", "Sci-Fi"],
        "answer": 1
    },
    {
        "question": "What genre features slow-paced narratives with minimal dialogue and maximum atmosphere?",
        "options": ["Action", "Art House/Drama", "Comedy", "Musical"],
        "answer": 1
    },
    {
        "question": "Which genre involves stories about zombies, viral outbreaks, and post-apocalyptic survival?",
        "options": ["Romance", "Zombie/Apocalyptic", "Western", "Musical"],
        "answer": 1
    },
    {
        "question": "Films that explore sexuality, gender identity, and LGBTQ+ themes belong to which genre category?",
        "options": ["Western", "Drama/LGBTQ+", "Musical", "Horror"],
        "answer": 1
    },
    {
        "question": "What genre involves stories about heists, con artists, and elaborate schemes?",
        "options": ["Romance", "Crime/Heist", "Documentary", "Western"],
        "answer": 1
    }
]

@app.route('/')
def index():
    session.clear()
    session['score'] = 0
    session['question_index'] = 0
    session['answers'] = []
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'question_index' not in session:
        return redirect(url_for('index'))
    
    question_index = session['question_index']
    
    if question_index >= len(QUESTIONS):
        return redirect(url_for('results'))
    
    current_question = QUESTIONS[question_index]
    
    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        if selected_answer is not None:
            selected_answer = int(selected_answer)
            correct = selected_answer == current_question['answer']
            session['answers'].append({
                'question': current_question['question'],
                'selected': selected_answer,
                'correct': correct,
                'correct_answer': current_question['answer']
            })
            if correct:
                session['score'] = session.get('score', 0) + 1
            session['question_index'] = question_index + 1
            session.modified = True
        
        return redirect(url_for('question'))
    
    total = len(QUESTIONS)
    progress = ((question_index) / total) * 100
    
    return render_template(
        'question.html',
        question=current_question,
        question_num=question_index + 1,
        total=total,
        progress=progress,
        last_answer=session['answers'][-1] if session.get('answers') and question_index > 0 else None
    )

@app.route('/results')
def results():
    if 'question_index' not in session:
        return redirect(url_for('index'))
    
    score = session.get('score', 0)
    total = len(QUESTIONS)
    percentage = (score / total) * 100
    
    feedback = ""
    if percentage >= 90:
        feedback = "Outstanding! You're a true movie enthusiast!"
    elif percentage >= 70:
        feedback = "Great job! You really know your movie genres!"
    elif percentage >= 50:
        feedback = "Not bad! Keep watching more movies!"
    else:
        feedback = "Time to binge some more films!"
    
    return render_template(
        'results.html',
        score=score,
        total=total,
        percentage=percentage,
        feedback=feedback,
        answers=session.get('answers', [])
    )

@app.route('/restart')
def restart():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

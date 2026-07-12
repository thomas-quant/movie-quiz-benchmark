"""Question bank for the Movie Types quiz.

Each question is a dict:
    q       -> the question text
    options -> list of answer choices (rendered in order)
    answer  -> index (0-based) into ``options`` of the correct choice
    explain -> short note shown on the results page
"""

QUESTIONS = [
    {
        "q": "Which genre is built primarily to provoke fear and dread, often using "
             "monsters, ghosts, or the supernatural?",
        "options": ["Horror", "Comedy", "Western", "Musical"],
        "answer": 0,
        "explain": "Horror exists to frighten and unsettle the audience.",
    },
    {
        "q": "A film set in the American Old West with cowboys, gunfights, and "
             "frontier life belongs to which genre?",
        "options": ["War film", "Western", "Film noir", "Fantasy"],
        "answer": 1,
        "explain": "The Western is defined by its Old West frontier setting.",
    },
    {
        "q": "Which type of movie has the primary goal of making the audience laugh?",
        "options": ["Drama", "Thriller", "Comedy", "Documentary"],
        "answer": 2,
        "explain": "Comedy is designed above all to amuse and entertain.",
    },
    {
        "q": "Futuristic technology, space travel, and speculative scientific ideas "
             "are the hallmarks of which genre?",
        "options": ["Fantasy", "Science fiction", "Mystery", "Romance"],
        "answer": 1,
        "explain": "Science fiction extrapolates from science and technology.",
    },
    {
        "q": "A film that presents factual, real-life subjects rather than a "
             "fictional story is called a...",
        "options": ["Biopic", "Mockumentary", "Documentary", "Anthology"],
        "answer": 2,
        "explain": "Documentaries depict real people, events, and facts.",
    },
    {
        "q": "A light-hearted story that follows a couple's bumpy path to love is "
             "best described as a...",
        "options": ["Romantic comedy", "Slasher", "Epic", "Procedural"],
        "answer": 0,
        "explain": "The 'rom-com' blends romance with comedy.",
    },
    {
        "q": "Which genre is driven by suspense, danger, and a tense race against "
             "time?",
        "options": ["Musical", "Thriller", "Comedy", "Family"],
        "answer": 1,
        "explain": "Thrillers keep audiences on edge with mounting tension.",
    },
    {
        "q": "Song-and-dance numbers that advance the plot are the defining feature "
             "of which genre?",
        "options": ["Opera film", "Concert film", "Musical", "Dance documentary"],
        "answer": 2,
        "explain": "In a musical, characters break into song to tell the story.",
    },
    {
        "q": "Films created frame-by-frame or with computer-generated characters "
             "rather than live actors are called...",
        "options": ["Animation", "Stop-motion only", "Silent films", "Shorts"],
        "answer": 0,
        "explain": "Animation brings drawn or CGI characters to life.",
    },
    {
        "q": "Which classic style is a dark, cynical crime drama from the 1940s–50s "
             "known for shadowy, high-contrast visuals?",
        "options": ["Screwball comedy", "Film noir", "Spaghetti Western", "Kitchen-sink drama"],
        "answer": 1,
        "explain": "Film noir pairs moral murk with stark lighting.",
    },
    {
        "q": "Grand, large-scale films with sweeping historical or biblical settings "
             "and enormous casts are known as...",
        "options": ["Shorts", "Vignettes", "Epics", "Featurettes"],
        "answer": 2,
        "explain": "Epics are defined by their scale and grand scope.",
    },
    {
        "q": "A film centered on solving a crime or puzzle while hiding the culprit "
             "until the end is a...",
        "options": ["Mystery", "Romance", "Musical", "Sports film"],
        "answer": 0,
        "explain": "Mysteries withhold the solution to keep you guessing.",
    },
    {
        "q": "Movies about military conflict, soldiers, and the battlefield fall "
             "under which genre?",
        "options": ["Disaster film", "War film", "Heist film", "Road movie"],
        "answer": 1,
        "explain": "War films dramatize armed conflict and its toll.",
    },
    {
        "q": "Spies, secret gadgets, and international intrigue are central to which "
             "genre?",
        "options": ["Espionage / spy film", "Western", "Slapstick", "Nature documentary"],
        "answer": 0,
        "explain": "The spy genre revolves around espionage and intrigue.",
    },
    {
        "q": "Extended chases, fights, explosions, and stunt set-pieces are the "
             "signature of which genre?",
        "options": ["Drama", "Action", "Romance", "Biopic"],
        "answer": 1,
        "explain": "Action films prioritize physical, high-energy spectacle.",
    },
    {
        "q": "A serious narrative focused on realistic characters and emotional "
             "conflict is broadly called a...",
        "options": ["Farce", "Drama", "Spoof", "Caper"],
        "answer": 1,
        "explain": "Drama centers on grounded, emotional storytelling.",
    },
    {
        "q": "Stories set in magical worlds with mythical creatures, wizards, and "
             "quests belong to which genre?",
        "options": ["Science fiction", "Fantasy", "Noir", "Procedural"],
        "answer": 1,
        "explain": "Fantasy is built on magic and the mythical.",
    },
    {
        "q": "A film that imitates and exaggerates another work or genre to mock it "
             "for laughs is a...",
        "options": ["Parody / spoof", "Sequel", "Reboot", "Adaptation"],
        "answer": 0,
        "explain": "Parodies poke fun by exaggerating their target.",
    },
    {
        "q": "A horror subgenre in which a killer stalks and murders victims one by "
             "one is known as a...",
        "options": ["Found footage", "Slasher", "Body swap", "Whodunit"],
        "answer": 1,
        "explain": "Slashers feature a serial killer picking off a cast.",
    },
    {
        "q": "Wholesome movies aimed at children and the whole household are "
             "categorized as...",
        "options": ["Family films", "Exploitation films", "Art house", "Noir"],
        "answer": 0,
        "explain": "Family films are kept light and broadly appropriate.",
    },
    {
        "q": "A film dramatizing the real life story of an actual person is called "
             "a...",
        "options": ["Mockumentary", "Biopic", "Anthology", "Docudrama short"],
        "answer": 1,
        "explain": "A biopic ('biographical picture') portrays a real life.",
    },
    {
        "q": "Gangsters, mob families, and organized criminal life are the focus of "
             "which genre?",
        "options": ["Crime / gangster film", "Sports film", "Coming-of-age", "Musical"],
        "answer": 0,
        "explain": "The crime/gangster film centers on the criminal underworld.",
    },
    {
        "q": "A movie that deliberately mixes scares and laughs is best labelled...",
        "options": ["Horror comedy", "Period drama", "Mockbuster", "Newsreel"],
        "answer": 0,
        "explain": "Horror comedy fuses frights with humor.",
    },
    {
        "q": "Films that build dread through atmosphere and the mind rather than "
             "gore are often called...",
        "options": ["Splatter films", "Psychological horror", "Screwball", "Buddy films"],
        "answer": 1,
        "explain": "Psychological horror unsettles through tension and the mind.",
    },
    {
        "q": "A feature made of several separate short stories linked by a theme or "
             "framing device is an...",
        "options": ["Anthology film", "Epic", "Serial", "Featurette"],
        "answer": 0,
        "explain": "Anthology films stitch together distinct segments.",
    },
    {
        "q": "A story tracing a young person's emotional growth into adulthood is "
             "a...",
        "options": ["Coming-of-age film", "Disaster film", "Heist film", "Concert film"],
        "answer": 0,
        "explain": "Coming-of-age stories follow the passage into maturity.",
    },
    {
        "q": "Movies featuring caped crusaders with extraordinary powers fighting "
             "villains belong to which modern genre?",
        "options": ["Superhero film", "Kitchen-sink drama", "Western", "Noir"],
        "answer": 0,
        "explain": "The superhero film centers on powered heroes and villains.",
    },
    {
        "q": "A film depicting a bleak, oppressive, often totalitarian future "
             "society is described as...",
        "options": ["Utopian", "Dystopian", "Pastoral", "Romantic"],
        "answer": 1,
        "explain": "Dystopian films imagine a dark, controlling future.",
    },
    {
        "q": "A meticulously planned robbery carried out by a crew of specialists is "
             "the core of which genre?",
        "options": ["Heist film", "Nature film", "Musical", "Biopic"],
        "answer": 0,
        "explain": "The heist film is built around an elaborate robbery.",
    },
    {
        "q": "A comedy that uses fake documentary techniques to satirize its subject "
             "is a...",
        "options": ["Mockumentary", "Newsreel", "Travelogue", "Melodrama"],
        "answer": 0,
        "explain": "A mockumentary apes the documentary form for comedy.",
    },
    {
        "q": "A road movie is primarily structured around what?",
        "options": [
            "A journey or trip undertaken by the characters",
            "A single locked room",
            "A courtroom trial",
            "A haunted house",
        ],
        "answer": 0,
        "explain": "Road movies follow characters on a literal and personal journey.",
    },
    {
        "q": "Films built around catastrophic events such as earthquakes, floods, or "
             "sinking ships are called...",
        "options": ["Disaster films", "Caper films", "Period pieces", "Buddy comedies"],
        "answer": 0,
        "explain": "Disaster films center on large-scale catastrophes.",
    },
]

"""Question bank for the movie types quiz.

Each question is a dict with:
    text     - the question shown to the user
    choices  - list of 4 answer options
    answer   - index into choices of the correct option
"""

QUESTIONS = [
    {
        "text": "Which genre is defined by its intent to frighten and unsettle the audience?",
        "choices": ["Comedy", "Horror", "Musical", "Documentary"],
        "answer": 1,
    },
    {
        "text": "A film that tells a factual story using real footage and interviews is called a...",
        "choices": ["Mockumentary", "Biopic", "Documentary", "Docudrama"],
        "answer": 2,
    },
    {
        "text": "'Film noir' is best described as...",
        "choices": [
            "A dark, cynical crime drama style with shadowy visuals",
            "A French comedy tradition",
            "A type of silent film",
            "A nature documentary format",
        ],
        "answer": 0,
    },
    {
        "text": "Which genre typically features cowboys, frontier towns, and shootouts?",
        "choices": ["Gangster", "Western", "War", "Noir"],
        "answer": 1,
    },
    {
        "text": "A 'rom-com' is a blend of which two genres?",
        "choices": [
            "Romance and comedy",
            "Romance and crime",
            "Road movie and comedy",
            "Romance and combat",
        ],
        "answer": 0,
    },
    {
        "text": "Movies like '2001: A Space Odyssey' and 'Blade Runner' belong primarily to which genre?",
        "choices": ["Fantasy", "Science fiction", "Adventure", "Thriller"],
        "answer": 1,
    },
    {
        "text": "Which genre relies on suspense, tension, and high stakes to keep audiences on edge?",
        "choices": ["Thriller", "Musical", "Slapstick", "Period drama"],
        "answer": 0,
    },
    {
        "text": "A film dramatizing the life of a real person is known as a...",
        "choices": ["Biopic", "Anthology", "Mockumentary", "Melodrama"],
        "answer": 0,
    },
    {
        "text": "'The Lord of the Rings' is a classic example of which genre?",
        "choices": ["Science fiction", "Historical epic", "Fantasy", "Adventure noir"],
        "answer": 2,
    },
    {
        "text": "Which genre centers on song and dance numbers woven into the story?",
        "choices": ["Opera film", "Musical", "Concert film", "Melodrama"],
        "answer": 1,
    },
    {
        "text": "A 'mockumentary' like 'This Is Spinal Tap' is...",
        "choices": [
            "A documentary about comedy",
            "A fictional story shot in documentary style for comedic effect",
            "A documentary with re-enactments",
            "A parody of a specific famous film",
        ],
        "answer": 1,
    },
    {
        "text": "Which subgenre of horror features masked killers stalking groups of victims?",
        "choices": ["Found footage", "Slasher", "Body horror", "Gothic horror"],
        "answer": 1,
    },
    {
        "text": "'Slapstick' comedy is characterized by...",
        "choices": [
            "Witty wordplay and banter",
            "Exaggerated physical humor and pratfalls",
            "Dark, morbid jokes",
            "Improvised dialogue",
        ],
        "answer": 1,
    },
    {
        "text": "Films like 'Saving Private Ryan' and 'Dunkirk' belong to which genre?",
        "choices": ["Action", "War", "Historical romance", "Political thriller"],
        "answer": 1,
    },
    {
        "text": "Which genre follows criminals, heists, and law enforcement pursuits?",
        "choices": ["Crime", "Legal drama", "Mystery", "Espionage"],
        "answer": 0,
    },
    {
        "text": "A 'whodunit' is a subgenre of...",
        "choices": ["Horror", "Mystery", "Fantasy", "Western"],
        "answer": 1,
    },
    {
        "text": "Japanese animated films such as 'Spirited Away' are commonly referred to as...",
        "choices": ["Manga", "Anime", "Tokusatsu", "Chibi"],
        "answer": 1,
    },
    {
        "text": "Which term describes big-budget spectacle films designed for mass appeal?",
        "choices": ["Arthouse", "Blockbuster", "B-movie", "Indie"],
        "answer": 1,
    },
    {
        "text": "A low-budget film made outside the major studio system is called a(n)...",
        "choices": ["Blockbuster", "Studio picture", "Independent (indie) film", "Serial"],
        "answer": 2,
    },
    {
        "text": "'Kaiju' films, originating in Japan, feature...",
        "choices": [
            "Samurai duels",
            "Giant monsters like Godzilla",
            "Haunted houses",
            "Street racing",
        ],
        "answer": 1,
    },
    {
        "text": "Which genre blends scares with laughs, like 'Shaun of the Dead'?",
        "choices": ["Dark fantasy", "Horror comedy", "Psychological thriller", "Satire"],
        "answer": 1,
    },
    {
        "text": "A 'coming-of-age' film focuses on...",
        "choices": [
            "A character's growth from youth toward adulthood",
            "The founding of a nation",
            "An elderly protagonist's memories",
            "The rise of a business empire",
        ],
        "answer": 0,
    },
    {
        "text": "'Spaghetti Westerns' were primarily produced in which country?",
        "choices": ["United States", "Spain", "Italy", "Mexico"],
        "answer": 2,
    },
    {
        "text": "Which genre features spies, gadgets, and international intrigue?",
        "choices": ["Espionage/spy", "Heist", "Legal thriller", "Techno-drama"],
        "answer": 0,
    },
    {
        "text": "A 'road movie' is structured around...",
        "choices": [
            "A single location",
            "Characters traveling on a journey",
            "Car manufacturing",
            "A race against time in one city",
        ],
        "answer": 1,
    },
    {
        "text": "'Dystopian' films like 'The Hunger Games' depict...",
        "choices": [
            "Idealized perfect societies",
            "Nightmarish or oppressive future societies",
            "Ancient civilizations",
            "Rural farm life",
        ],
        "answer": 1,
    },
    {
        "text": "Which term describes a film that reimagines or updates an earlier film?",
        "choices": ["Sequel", "Prequel", "Remake", "Spin-off"],
        "answer": 2,
    },
    {
        "text": "'Found footage' horror, like 'The Blair Witch Project', presents the story as...",
        "choices": [
            "A narrated documentary",
            "Recovered amateur recordings made by the characters",
            "A live news broadcast",
            "An animated re-enactment",
        ],
        "answer": 1,
    },
    {
        "text": "A 'heist film' revolves around...",
        "choices": [
            "A courtroom battle",
            "Planning and executing a major theft",
            "A hostage negotiation",
            "A prison escape",
        ],
        "answer": 1,
    },
    {
        "text": "Which genre dramatizes historical events with large casts and grand scale?",
        "choices": ["Chamber drama", "Historical epic", "Kitchen-sink realism", "Neorealism"],
        "answer": 1,
    },
    {
        "text": "'Cyberpunk' science fiction typically combines...",
        "choices": [
            "High technology with gritty, dystopian societies",
            "Space travel with medieval fantasy",
            "Robots with musical numbers",
            "Time travel with romance",
        ],
        "answer": 0,
    },
    {
        "text": "An 'anthology film' is one that...",
        "choices": [
            "Adapts a famous novel",
            "Contains several separate short stories in one film",
            "Runs longer than three hours",
            "Is filmed in a single take",
        ],
        "answer": 1,
    },
]

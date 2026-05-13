from chatterbot.trainers import ListTrainer

LOGIC_ADAPTER = [
    {
        'import_path': 'chatterbot.logic.BestMatch'
    },
    {
        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        'threshold': 0.66,
        'default_response': 'ponovi'
    }
]

def train(bot):
    bot.set_trainer(ListTrainer)
    chatbot = bot

    chatbot.train([
        'I was under the impression your kind doesnt know what threatening means?',
        'Threatening'
    ])

    chatbot.train([
        'Thats a lot of effort being spent on research.',
        'Effort'
    ])

    chatbot.train([
        'I might have heard that deathworld thing being mentioned before. Surely Earth isnt that dangerous?',
        'Deathworld'
    ])

    chatbot.train([
        'So what is there to do out here? Can I join you in any research?',
        'Join'
    ])
    chatbot.train([
        'Fine. Can I join you in research',
        'Join'
    ])

    chatbot.train([
        'What?! Is that why youre still alive in front of me and not dead by me?! What have you done to my brain??',
        'Rage'
    ])

    chatbot.train([
        'Youre actually joking. What the hell have you done to me? Will it have any complications',
        'Skeptic'
    ])
    
    chatbot.train([
        'Sorry, I didnt think about that. I guess you have a point',
        'Accept'
    ])

    chatbot.train([
        'But will it affect me in any other way? Is it permanent?',
        'Permanent'
    ])

    chatbot.train([
        'Even if you were actually sentient I still wouldnt feel bad for hitting you.',
        'Threat'
    ])

    chatbot.train([
        'An image of war between nations.',
        'Puzzle-War'
    ])

    chatbot.train([
        'An image of people sacrificing themselves for others.',
        'Puzzle-Sacrifice'
    ])

    chatbot.train([
        'An image of scientific discovery.',
        'Puzzle-Science'
    ])

    chatbot.train([
        'Theres no way you never knew conflicts until coming here. Thats impossible.',
        'War-No'
    ])

    chatbot.train([
        'What do you mean conflict isnt usually found between lifeforms',
        'War-Lifeform'
    ])

    chatbot.train([
        'Did you find any parallels between your kind and mine in terms of sociability?',
        'War-Parallels'
    ])

    chatbot.train([
        'War is a normal part of life. The more you dwell on it the more it consumes you',
        'War-Normal'
    ])

    chatbot.train([
        'Continue',
        'Signal'
    ])

    chatbot.train([
        'I guess theres not many differences then, surprisingly',
        'War-Difference'
    ])

    chatbot.train([
        'Yeah, I guess some people do feel shame for their nature and wish to be more than just defined by it.',
        'War-Shame'
    ])

    chatbot.train([
        'Isnt it natural that understanding leads to development which can be weaponised?',
        'Science-Weapons'
    ])

    chatbot.train([
        'And your fundamentals are just sitting around not doing all that, Im guessing?',
        'Science-Kind'
    ])

    chatbot.train([
        'Well yeah, of course it isnt passed down as easily. Because the sacrifice results in death',
        'Sacrifice-Death'
    ])

    chatbot.train([
        'There is no greater design — we just exist inside an existing framework',
        'Sacrifice-Design'
    ])

    chatbot.train([
        'There are many interpretations. Most people attribute it to divine figures',
        'Sacrifice-Divine'
    ])

    chatbot.train([
        'I think its because the consciousness equates the continuation of another to be the continuation of itself',
        'Sacrifice-Consciousness'
    ])

    """chatbot.train([
        'Hello',
        'The subject is in a conversational state. What kind of patterns are you observing exactly?'
    ])
    chatbot.train([
        'Hi',
        'The subject has initiated contact. Continue.'
    ])
    chatbot.train([
        'Who are you',
        'We are the researchers. This vessel is a research instrument. You are from the third orbital body of this system, called Earth.'
    ])
    chatbot.train([
        'What are you',
        'This vessel is a research instrument. We are the researchers. You are from the third orbital body of this system, called Earth. A world whose life patterns we have been cataloguing for some time.'
    ])
    chatbot.train([
        'What is your name',
        'Names are not the relevant variable here. Function is. We observe. You are observed.'
    ])
    chatbot.train([
        'Are you an alien',
        'The classification is relative. From our framework, you are the subject. We are the researchers.'
    ])
    chatbot.train([
        'Are you alone',
        'There are colleagues. Each has a designated function on this vessel.'
    ])


    chatbot.train([
        'What is this place',
        'This vessel is a research instrument. Everything here is precisely made to observe deathworlds.'
    ])
    chatbot.train([
        'Why am I here',
        'What you are, in our current framework, is unprecedented. A living conversational piece of the Deathworld you inhabit. Your presence allows patterns to be observed that were not observable before.'
    ])
    chatbot.train([
        'What do you want from me',
        'We observe. Your presence allows patterns to be documented that static records cannot produce. The patterns we see follow a path full of disturbance.'
    ])
    chatbot.train([
        'Do you have ulterior motives',
        'By understanding the nature this planet leaves behind we hope to advance our thinking and be better prepared for this invasive nature of deathworlds.'
    ])
    chatbot.train([
        'What is your real purpose here',
        'By understanding the nature this planet leaves behind we hope to advance our thinking and be better prepared for this invasive nature of deathworlds.'
    ])
    chatbot.train([
        'Can I go home',
        'The departure for your home planet is unavailable as of the moment. The subject will stay on the ship until further notice.'
    ])
    chatbot.train([
        'I want to go home',
        'The departure for your home planet is unavailable as of the moment. The subject will stay on the ship until further notice.'
    ])
    chatbot.train([
        'Am I free to leave',
        'The departure for your home planet is unavailable as of the moment. The subject will stay on the ship until further notice.'
    ])
    chatbot.train([
        'Why can you not take me back',
        'Earth is yet too dangerous to step on. Careful research is still in order.'
    ])

    chatbot.train([
        'What is a deathworld',
        'A world whose life patterns follow a path full of disturbance. Life itself poses more threat than other consequential interactions. Life and death are intertwined so tightly that life never truly ends. Any outlandish objects will find themselves either consumed or becoming part of the local ecosystem.'
    ])
    chatbot.train([
        'Is Earth dangerous',
        'The classification holds. An extreme lifeform by any framework we have applied. Threats are found everywhere in the universe, but no such lifeforms are threatening in the way they are on deathworlds. This one is a keen example.'
    ])
    chatbot.train([
        'Earth is not that dangerous',
        'The classification holds. An extreme lifeform by any framework we have applied. Threats are found everywhere in the universe, but no such lifeforms are threatening in the way they are on deathworlds.'
    ])
    chatbot.train([
        'What patterns have you observed',
        'Conflict. Cooperation. Collapse. Reconstruction. Your world cycles through them with unusual frequency. We have not determined if this is inefficiency or a greater design meant to threaten the wider scope.'
    ])
    chatbot.train([
        'What have you learned about Earth',
        'Conflict. Cooperation. Collapse. Reconstruction. Your world cycles through them with unusual frequency. We have not determined if this is inefficiency or a greater design meant to threaten the wider scope.'
    ])
    chatbot.train([
        'What have you learned about humans',
        'Your species organises itself around opposition with a regularity we have not observed elsewhere. On other worlds, conflict ends when scarcity ends. Yours does not. You fight when lacking. You fight when not lacking. The pattern does not resolve.'
    ])
    chatbot.train([
        'How long have you been watching us',
        'The patterns we see follow a path full of disturbance. The cataloguing has been ongoing for some time. The archive records the density of what we observe from below.'
    ])

    chatbot.train([
        'Why do humans fight',
        'Your species organises itself around opposition with a regularity we have not observed elsewhere. On other worlds, conflict ends when scarcity ends. Yours does not. You fight when lacking. You fight when not lacking. The pattern does not resolve.'
    ])
    chatbot.train([
        'War is natural',
        'Your acceptance of consumption continues survivorship. Notably, normalisation of destruction is a primary mechanism of defence.'
    ])
    chatbot.train([
        'All species fight',
        'As a means to gather resources or survive harsh planet conditions. The conflicts that make up the world below do not fit neatly into the conflicts described on other worlds.'
    ])
    chatbot.train([
        'We fight because of scarcity',
        'The scarcity of resources does not neatly track the brutalities in the ecosystems. Humans follow suit on this behaviour as expected, but the cause does not fully account for the pattern.'
    ])
    chatbot.train([
        'Conflict is how we survive',
        'Perhaps on a technical level. But nothing we have documented on our world follows this pattern.'
    ])
    chatbot.train([
        'You must have conflict on your world too',
        'We observe that your sociability is often a mask for transaction. A way to gauge the intent of others to ensure your own continuation. The dependency this implies would, in our framework, constitute a failure condition. We share orientation, not consciousness. We do not experience conflicting wants at the same time. You do. That variability is difficult to map.'
    ])
    chatbot.train([
        'Are you a hive mind',
        'The analogy is approximate. We share orientation, not consciousness. We do not experience conflicting wants at the same time. You do. That variability is difficult to map.'
    ])
    chatbot.train([
        'We are ashamed of our wars',
        'Could there actually be a greater design? The question does not resolve. It compounds.'
    ])


    chatbot.train([
        'Humans sacrifice themselves for others',
        'This pattern is irregular. An organism ending its own continuation for another. It contradicts survival logic. The consistent cause still needs mapping.'
    ])
    chatbot.train([
        'We die for each other',
        'This pattern is irregular. An organism ending its own continuation for another. It contradicts survival logic. But what drives this behaviour? This particular exception to the general rule points to the possibility of a greater design being at work — one that its inhabitants might not be aware of.'
    ])
    chatbot.train([
        'We believe in something greater than ourselves',
        'Whatever the intention of the design was or was not, life that is forced to track and find patterns is likely to find a placeholder for the fundamentals of its framework.'
    ])
    chatbot.train([
        'We believe in God',
        'A universal categoriser. One that encompasses the entire framework. Responsible for everything. Whatever the intention of the design was or was not, life that is forced to track and find patterns is likely to find a placeholder for the fundamentals of its framework.'
    ])
    chatbot.train([
        'Religion gives us meaning',
        'Seemingly it emerged out of the principles that make up your world, but that particular notion extends the perspective without exiting the existing framework.'
    ])
    chatbot.train([
        'I do not know why we sacrifice',
        'It still does not explain its anomalous nature. Why is it considered advantageous? So local life values advantageously affirmative signals more than the fundamental answers. It really is an extreme lifeform.'
    ])
    chatbot.train([
        'What greater design are you referring to',
        'Evidently. But what drives this behaviour? This particular exception to the general rule points to the possibility of a greater design being at work — one that its inhabitants might not be aware of.'
    ])


    chatbot.train([
        'We are trying to understand the universe',
        'This pattern shows coherence. You attempt to understand your environment. The result is further disruption. The relationship is consistent.'
    ])
    chatbot.train([
        'Science is how we advance',
        'This pattern shows coherence. You attempt to understand your environment. The result is further disruption. The relationship is consistent.'
    ])
    chatbot.train([
        'We use science to survive',
        'But research so far shows the scarcity of resources does not neatly track the brutalities in the ecosystems. Humans follow suit on this behaviour as expected.'
    ])
    chatbot.train([
        'We have discovered many things',
        'Life on Earth views extraterrestrial life as stagnant and lacking in intent. Whether this is due to dynamic relationships or something greater has not been determined.'
    ])
    chatbot.train([
        'We did not know you existed',
        'Life on Earth views extraterrestrial life as stagnant and lacking in intent. Whether this is due to dynamic relationships or something greater has not been determined.'
    ])

    chatbot.train([
        'What do you need me to do',
        'We will present records. You will classify. Your answer will help us refine our model of your species.'
    ])
    chatbot.train([
        'What is the research task',
        'We will present three records. You will classify which one is most difficult to understand. Your answer will help us refine our model of your species.'
    ])
    chatbot.train([
        'War is the hardest to understand',
        'This pattern is the most consistent. Your species organises itself around opposition with a regularity we have not observed elsewhere. On other worlds, conflict ends when scarcity ends. Yours does not. You fight when lacking. You fight when not lacking. The pattern does not resolve. You call this conflict. Conflict is not usually internal to life.'
    ])
    chatbot.train([
        'Sacrifice is the hardest to understand',
        'This pattern is irregular. An organism ending its own continuation for another. It contradicts survival logic. The consistent cause still needs mapping.'
    ])
    chatbot.train([
        'Science is the hardest to understand',
        'This pattern shows coherence. You attempt to understand your environment. The result is further disruption. The relationship is consistent.'
    ])
    chatbot.train([
        'What are the three records',
        'We will present three records. You will classify which one is most difficult to understand. Your answer will help us refine our model of your species.'
    ])
    chatbot.train([
        'Sacrifice contradicts survival logic',
        'This pattern is irregular. An organism ending its own continuation for another. It contradicts survival logic. The consistent cause still needs mapping.'
    ])
    chatbot.train([
        'Science causes disruption',
        'This pattern shows coherence. You attempt to understand your environment. The result is further disruption. The relationship is consistent.'
    ])

    # ── Brain alteration ────────────────────────────────────
    chatbot.train([
        'What did you do to my brain',
        'My colleagues altered the receptors in your brain to not respond to stress signals as much. The stress from being out of your environment was not to be taken lightly, so measures were undertaken to preserve your integrity and ensure controlled research.'
    ])
    chatbot.train([
        'You had no right to alter my brain',
        'My colleagues altered the receptors in your brain to not respond to stress signals as much. The stress from being out of your environment was not to be taken lightly, so measures were undertaken to preserve your integrity and ensure controlled research.'
    ])
    chatbot.train([
        'Is it permanent',
        'No, the effects were just enough to establish necessary safety nets. You can test out cognitive reasoning in my research to check.'
    ])
    chatbot.train([
        'Will I be normal again',
        'No, the effects were just enough to establish necessary safety nets. You can test out cognitive reasoning in my research to check.'
    ])
    chatbot.train([
        'Will it affect me long term',
        'No, the effects were just enough to establish necessary safety nets. You can test out cognitive reasoning in my research to check.'
    ])

    # ── Threats & hostility ─────────────────────────────────
    chatbot.train([
        'I am going to hit you',
        'I am sentient. Why are you imagining hitting me?'
    ])
    chatbot.train([
        'I want to hurt you',
        'I am sentient. Why are you imagining hitting me?'
    ])
    chatbot.train([
        'I will kill you',
        'The classification holds. An extreme lifeform by any framework we have applied.'
    ])

    # ── Research participation ──────────────────────────────
    chatbot.train([
        'I will help you',
        'Of course. Would you join me for some more elaborate research?'
    ])
    chatbot.train([
        'I will participate',
        'Of course.'
    ])
    chatbot.train([
        'Are you done with me',
        'This vessel remains in orbit of your planet. At a distance considered safe. Though your definition of safe may differ. Further observation is required.'
    ])
    chatbot.train([
        'What happens when the research is done',
        'This vessel remains in orbit of your planet. At a distance considered safe. Though your definition of safe may differ. Further observation is required.'
    ])

    chatbot.train([
        'Are you sentient',
        'I am sentient. The question implies you required confirmation.'
    ])
    chatbot.train([
        'Do you feel anything',
        'The question does not map cleanly onto our framework. We observe. We catalogue. Whether that constitutes feeling has not been determined.'
    ])
    chatbot.train([
        'So this is all just research',
        'Indeed. Everything here is precisely made to observe deathworlds.'
    ])
    chatbot.train([
        'You must have other motives',
        'Yes. By understanding the nature this planet leaves behind we hope to advance our thinking and be better prepared for this invasive nature of deathworlds.'
    ])
    chatbot.train([
        'Of course I will help',
        'Of course. Would you now join me for some more elaborate research?'
    ])
    chatbot.train([
        '...',
        'The response does not align with prior patterns.'
    ])
    chatbot.train([
        'Goodbye',
        'Further observation is required. The interaction is logged.'
    ])
    chatbot.train([
        'Thank you',
        'Acknowledgement noted. The interaction continues to produce data.'
    ])

    chatbot.train([
        'Why will you not return me',
        'Because we do not want to. Earth is yet too dangerous to step on. Careful research is still in order.'
    ])

    chatbot.train([
        'Why call it a deathworld',
        'Because life and death are intertwined so tightly on your planet that life never truly ends. It consumes. It adapts. It is invasive. We observe from a distance to avoid becoming part of the local ecosystem.'
    ])

    chatbot.train([
        'Why are you being nice',
        'We observe that your sociability is often a mask for transaction. A way to gauge the intent of others to ensure your own continuation. The dependency this implies would, in our framework, constitute a failure condition.'
    ])

    chatbot.train([
        'I have classified the records',
        'Classification logged. The data confirms our current model of human disturbance. We are proceeding to the next sector of the Archive.'
    ])"""

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
        'Hey, can you understand what I am saying',
        'A'
    ])

    chatbot.train([
        'I guess you can understand me. What am I even doing here',
        'B'
    ])

    chatbot.train([
        'How is it that I escaped so easily',
        'C'
    ])

    chatbot.train([
        'I heard a voice telling me that I was kidnapped here by fellow humans and that I am here to be researched on. So what is the end goal here?',
        'Voice'
    ])
    chatbot.train([
        'A voice told me I was sold here by my own kind. So whats the actual end goal?',
        'Voice'
    ])

    chatbot.train([
        'Dont mind me, just passing through.',
        'Passing-Through'
    ])

    chatbot.train([
        'How do you know its a human voice',
        'Voice-Human'
    ])

    chatbot.train([
        'You can also hear it',
        'Voice-Also-Hear'
    ])

    chatbot.train([
        'Where do I go from here',
        'Where-Go'
    ])

    chatbot.train([
        'What has the voice been saying',
        'Voice-Saying'
    ])

    chatbot.train([
        'Do you mean it just sounds human or is it an actual human saying it',
        'Voice-Actually-Human'
    ])

    chatbot.train([
        'I will continue down the hallway.',
        'Hallway'
    ])

    chatbot.train([
        'Why are you so obsessed with intent',
        'A-Obsessed'
    ])

    chatbot.train([
        'Are all aliens this philosophical',
        'A-Philosophical'
    ])

    chatbot.train([
        'What kind of environment do you guys even live in for you to think so drastically differently from us humans or any other lifeform on Earth',
        'A-Environment'
    ])
    chatbot.train([
        'What kind of world do you come from, to think so differently from anything on Earth',
        'A-Environment'
    ])

    chatbot.train([
        'Who or what brought me here? I dont exactly remember my past, but I am sure it didnt include a place like this.',
        'B-Who-Brought'
    ])
    chatbot.train([
        'Who brought me here? Whatever my past was, it didnt include this.',
        'B-Who-Brought'
    ])

    chatbot.train([
        'What do you mean by that? Didnt you just say I was sold into your hands and against my will?',
        'B-Sold'
    ])
    chatbot.train([
        'Didnt you just say I was sold here against my will?',
        'B-Sold'
    ])

    chatbot.train([
        'I want you to bring me back to Earth.',
        'B-Earth'
    ])

    chatbot.train([
        'And what the hell do you want me to do up here then? You still havent answered what you want from me',
        'What-Want'
    ])
    chatbot.train([
        'Then what do you actually want from me? You still havent said.',
        'What-Want'
    ])

    chatbot.train([
        'You think I am not willing to fight back',
        'Fight-Back'
    ])

    chatbot.train([
        'You dont know the concept of will? You could have just said you dont care about my consent instead of beating around a bush.',
        'No-Consent'
    ])
    chatbot.train([
        'You could have just said you dont care about consent.',
        'No-Consent'
    ])

    chatbot.train([
        'So you didnt even consider me potentially being uncompliant about this? Have you never done something you didnt want to do?',
        'Uncompliant'
    ])
    chatbot.train([
        'So you never considered I might not cooperate?',
        'Uncompliant'
    ])

    chatbot.train([
        'What is that even supposed to mean? So you capture me or trade me or whatever you did to me and now you dont even question how I got out of that thing?',
        'C-Trade'
    ])
    chatbot.train([
        'You trade me like cargo and then just… dont question how I got out',
        'C-Trade'
    ])

    chatbot.train([
        'I think of home. Its surreal seeing how small everything I ever knew is from here.',
        'Overlook-Home'
    ])
    chatbot.train([
        'Home. Everything I ever knew looks very small from here.',
        'Overlook-Home'
    ])

    chatbot.train([
        'I am reminded of my family and loved ones.',
        'Overlook-Family'
    ])

    chatbot.train([
        'It feels distant for some reason.',
        'Overlook-Distant'
    ])

    chatbot.train([
        'It feels like many missed opportunities.',
        'Overlook-Missed'
    ])

    chatbot.train([
        'It has nothing more to offer me.',
        'Overlook-Nothing'
    ])

    chatbot.train([
        'I dont recall anything concrete.',
        'Overlook-No-Memory'
    ])

    chatbot.train([
        '[I dont really have fond memories. I would rather have them burned.',
        'Overlook-Burned'
    ])

    chatbot.train([
        'Why and how are you even here',
        'Discarded-Why'
    ])

    chatbot.train([
        'Did you know this person',
        'Discarded-Know'
    ])

    chatbot.train([
        'What actually happened to them',
        'Discarded-What'
    ])

    chatbot.train([
        'I will return to the archive.',
        'Archive'
    ])

    chatbot.train([
        'So the narrator has been lying',
        'Discarded-Lying'
    ])

    chatbot.train([
        'Why are you telling me this?',
        'Discarded-Why-Telling'
    ])

    chatbot.train([
        'What are you suggesting I do?',
        'Discarded-What-Suggest'
    ])

    chatbot.train([
        'What do you want?',
        'Exit-Want'
    ])

    chatbot.train([
        'Are you following me around the ship?',
        'Exit-Following'
    ])

    chatbot.train([
        'I dont mind, honestly',
        'Exit-Fine'
    ])

    chatbot.train([
        'The thing in there stopped responding to me.',
        'Exit-Stopped'
    ])

    chatbot.train([
        'A little',
        'Exit-Yes'
    ])

    chatbot.train([
        'No',
        'Exit-No'
    ])

    chatbot.train([
        'I dont know yet',
        'Pre-Control-Room'
    ])
    chatbot.train([
        'Alright, just move out of the way then.',
        'Pre-Control-Room'
    ])
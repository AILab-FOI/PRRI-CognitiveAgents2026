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
        'What exactly do you need from me',
        'What-Need'
    ])

    chatbot.train([
        'You used me. You used the other person too and they died.',
        'Used-Me'
    ])

    chatbot.train([
        'Youve been watching me this whole time through the biochip.',
        'Biochip'
    ])

    chatbot.train([
        'The body in that room. You said the ship processes everything. It didnt process them',
        'Body'
    ])

    chatbot.train([
        'Your organisation. Who do they actually answer to?',
        'Organization'
    ])

    chatbot.train([
        'Did you grieve them? The first person',
        'Grieve'
    ])

    chatbot.train([
        'Do you actually believe humanity is worth what youve done for it?',
        'Believe'
    ])

    chatbot.train([
        'Continue',
        'Continue'
    ])

    chatbot.train([
        'Who are you really',
        'Who'
    ])

    chatbot.train([
        'So everything I said to the aliens, you heard.',
        'Heard'
    ])

    chatbot.train([
        'Did you ever intervene in what I said to them',
        'Intervene'
    ])

    chatbot.train([
        'Thats not an answer',
        'Not-Answer'
    ])

    chatbot.train([
        'I think you do',
        'Think'
    ])

    chatbot.train([
        'And now?',
        'Now'
    ])

    chatbot.train([
        'Were you ever going to tell me any of this?',
        'Tell-Me'
    ])
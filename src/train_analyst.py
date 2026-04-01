from chatterbot.trainers import ListTrainer

LOGIC_ADAPTER = [
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.66,
            'default_response': ' ponovi'
        }
    ]

def train(bot):
    bot.set_trainer(ListTrainer)
    chatbot = bot

    chatbot.train([
        'Yoharrro',
        'Yoyo'
    ])

    chatbot.train([
        'Meow',
        'Meow'
    ])

    chatbot.train([
        'Analize',
        'Sir yes sir'
    ])
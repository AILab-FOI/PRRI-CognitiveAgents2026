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
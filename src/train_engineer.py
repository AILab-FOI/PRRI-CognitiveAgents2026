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

    # ── Hello ────────────────────────────────────────────────────────────────
    chatbot.train(['Hello', 'Hello'])
    chatbot.train(['Hi there', 'Hello'])
    chatbot.train(['Hey', 'Hello'])
    chatbot.train(['Greetings', 'Hello'])

    # ── Who ──────────────────────────────────────────────────────────────────
    chatbot.train(['Who are you', 'Who'])
    chatbot.train(['What are you', 'Who'])
    chatbot.train(['Can you tell me who you are', 'Who'])
    chatbot.train(['Introduce yourself', 'Who'])

    # ── What ─────────────────────────────────────────────────────────────────
    chatbot.train(['What are you doing', 'What'])
    chatbot.train(['What are you working on', 'What'])
    chatbot.train(['What is your function here', 'What'])
    chatbot.train(['What exactly are you doing right now', 'What'])

    # ── C (Explore) ──────────────────────────────────────────────────────────
    chatbot.train(['Explore the room', 'C'])
    chatbot.train(['I want to look around', 'C'])
    chatbot.train(['I am just looking around', 'C'])
    chatbot.train(['Let me explore', 'C'])
    chatbot.train(['I would like to see what is in here', 'C'])

    # ── Research-Intro ───────────────────────────────────────────────────────
    chatbot.train(['Sure', 'Research-Intro'])
    chatbot.train(['Yes I will help', 'Research-Intro'])
    chatbot.train(['Alright I am interested', 'Research-Intro'])
    chatbot.train(['Yes I am willing to assist', 'Research-Intro'])
    chatbot.train(['Sounds good to me', 'Research-Intro'])

    # ── No ───────────────────────────────────────────────────────────────────
    chatbot.train(['No', 'No'])
    chatbot.train(['No thank you', 'No'])
    chatbot.train(['I am not interested', 'No'])
    chatbot.train(['I would rather not', 'No'])
    chatbot.train(['I will pass', 'No'])

    # ── Rifle ────────────────────────────────────────────────────────────────
    chatbot.train(['The disassembled assault rifle', 'Rifle'])
    chatbot.train(['The gun', 'Rifle'])
    chatbot.train(['That weapon over there', 'Rifle'])
    chatbot.train(['I want to look at the rifle', 'Rifle'])
    chatbot.train(['Tell me about the rifle', 'Rifle'])

    # ── Camera ───────────────────────────────────────────────────────────────
    chatbot.train(['The photography camera', 'Camera'])
    chatbot.train(['Switch to the camera', 'Camera'])
    chatbot.train(['The camera', 'Camera'])
    chatbot.train(['That camera over there', 'Camera'])
    chatbot.train(['Tell me about the camera', 'Camera'])

    # ── Rifle-Force ──────────────────────────────────────────────────────────
    chatbot.train(['Tool of force', 'Rifle-Force'])
    chatbot.train(['It is a weapon of force', 'Rifle-Force'])
    chatbot.train(['It is used to apply force', 'Rifle-Force'])
    chatbot.train(['A device made to project force', 'Rifle-Force'])
    chatbot.train(['Something that forces an outcome', 'Rifle-Force'])

    # ── Rifle-Power ──────────────────────────────────────────────────────────
    chatbot.train(['Tool of power', 'Rifle-Power'])
    chatbot.train(['It represents power', 'Rifle-Power'])
    chatbot.train(['It is a symbol of power', 'Rifle-Power'])
    chatbot.train(['It gives the user power', 'Rifle-Power'])
    chatbot.train(['A tool that grants power over others', 'Rifle-Power'])

    # ── Rifle-War ────────────────────────────────────────────────────────────
    chatbot.train(['Weapon used in war', 'Rifle-War'])
    chatbot.train(['It is used in warfare', 'Rifle-War'])
    chatbot.train(['A weapon designed for war', 'Rifle-War'])
    chatbot.train(['It is what soldiers use in war', 'Rifle-War'])
    chatbot.train(['Something used to fight wars', 'Rifle-War'])

    # ── Leave ────────────────────────────────────────────────────────────────
    chatbot.train(['Leave the engineering bay', 'Leave'])
    chatbot.train(['Exit the engineering bay', 'Leave'])
    chatbot.train(['I am leaving the engineering bay', 'Leave'])
    chatbot.train(['I want to go', 'Leave'])
    chatbot.train(['I am done here', 'Leave'])

    # ── Camera-Memory ────────────────────────────────────────────────────────
    chatbot.train(['Stores memories.', 'Camera-Memory'])
    chatbot.train(['It captures and stores memories', 'Camera-Memory'])
    chatbot.train(['A way to hold onto memories', 'Camera-Memory'])
    chatbot.train(['It preserves a moment in time', 'Camera-Memory'])
    chatbot.train(['It keeps a memory alive', 'Camera-Memory'])

    # ── Camera-Share ─────────────────────────────────────────────────────────
    chatbot.train(['Shares experiences.', 'Camera-Share'])
    chatbot.train(['It lets you share what you have seen', 'Camera-Share'])
    chatbot.train(['You can share experiences with others through it', 'Camera-Share'])
    chatbot.train(['A way to show others what you experienced', 'Camera-Share'])
    chatbot.train(['It is used to communicate moments with other people', 'Camera-Share'])

    # ── Camera-Obsession ─────────────────────────────────────────────────────
    chatbot.train(['Obsession replaces experience.', 'Camera-Obsession'])
    chatbot.train(['Sometimes the obsession with capturing replaces actually living', 'Camera-Obsession'])
    chatbot.train(['People get so focused on recording that they stop experiencing', 'Camera-Obsession'])
    chatbot.train(['You stop living the moment and only start recording it', 'Camera-Obsession'])
    chatbot.train(['The recording becomes the experience and that becomes the problem', 'Camera-Obsession'])

    # ── Camera-Imprecision ───────────────────────────────────────────────────
    chatbot.train(['The organisms. The imprecision is the point', 'Camera-Imprecision'])
    chatbot.train(['The organisms make it imprecise and that imprecision is the whole point', 'Camera-Imprecision'])
    chatbot.train(['The living things in it and the blur is part of the purpose', 'Camera-Imprecision'])
    chatbot.train(['The organisms are captured and the imprecision is what gives it meaning', 'Camera-Imprecision'])

    # ── Camera-Accuracy ──────────────────────────────────────────────────────
    chatbot.train(['The device is more accurate. Accuracy is what matters', 'Camera-Accuracy'])
    chatbot.train(['The camera is more precise than human memory and that is the point', 'Camera-Accuracy'])
    chatbot.train(['Accuracy is the purpose and the device provides that', 'Camera-Accuracy'])
    chatbot.train(['What matters is precision and the device is more precise than memory', 'Camera-Accuracy'])

    # ── Camera-Alone ─────────────────────────────────────────────────────────
    chatbot.train(['Because we dont want to experience things alone', 'Camera-Alone'])
    chatbot.train(['We use it so we do not have to experience things alone', 'Camera-Alone'])
    chatbot.train(['People want to share what they see because they do not want to be alone in it', 'Camera-Alone'])
    chatbot.train(['So someone else can experience what you experienced', 'Camera-Alone'])
    chatbot.train(['We do not want to experience things in isolation', 'Camera-Alone'])

    # ── Camera-Residue ───────────────────────────────────────────────────────
    chatbot.train(['Because the moment leaves something behind that cant be kept any other way', 'Camera-Residue'])
    chatbot.train(['Some moments leave something behind that cannot be kept any other way', 'Camera-Residue'])
    chatbot.train(['There are moments that leave a trace you need to hold onto', 'Camera-Residue'])
    chatbot.train(['A moment passes and leaves a feeling that disappears unless you capture it', 'Camera-Residue'])

    # ── Camera-Point ─────────────────────────────────────────────────────────
    chatbot.train(['Thats the point', 'Camera-Point'])
    chatbot.train(['Yes exactly that is the point', 'Camera-Point'])
    chatbot.train(['That is precisely the point', 'Camera-Point'])
    chatbot.train(['Yes that is the whole point of it', 'Camera-Point'])

    # ── Camera-Problem ───────────────────────────────────────────────────────
    chatbot.train(['No, thats the problem', 'Camera-Problem'])
    chatbot.train(['No actually that is the problem with it', 'Camera-Problem'])
    chatbot.train(['No that is the flaw in how we use it', 'Camera-Problem'])
    chatbot.train(['Actually that is what makes it problematic', 'Camera-Problem'])
    chatbot.train(['No it is more of a problem than a feature', 'Camera-Problem'])
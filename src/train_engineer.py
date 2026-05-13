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
        'Hello',
        'Hello'
    ])

    chatbot.train([
        'Who are you',
        'Who'
    ])

    chatbot.train([
        'What are you doing',
        'What'
    ])

    chatbot.train([
        'Explore the room',
        'C'
    ])

    chatbot.train([
        'Sure',
        'Research-Intro'
    ])

    chatbot.train([
        'No',
        'No'
    ])

    chatbot.train([
        'The disassembled assault rifle',
        'Rifle'
    ])

    chatbot.train([
        'The photography camera',
        'Camera'
    ])
    chatbot.train([
        'Switch to the camera',
        'Camera'
    ])

    chatbot.train([
        'Tool of force',
        'Rifle-Force'
    ])

    chatbot.train([
        'Tool of power',
        'Rifle-Power'
    ])

    chatbot.train([
        'Weapon used in war',
        'Rifle-War'
    ])

    chatbot.train([
        'Leave the engineering bay',
        'Leave'
    ])
    chatbot.train([
        'Exit the engineering bay',
        'Leave'
    ])

    chatbot.train([
        'Stores memories.',
        'Camera-Memory'
    ])

    chatbot.train([
        'Shares experiences.',
        'Camera-Share'
    ])

    chatbot.train([
        'Obsession replaces experience.',
        'Camera-Obsession'
    ])

    chatbot.train([
        'The organisms. The imprecision is the point',
        'Camera-Imprecision'
    ])

    chatbot.train([
        'The device is more accurate. Accuracy is what matters',
        'Camera-Accuracy'
    ])

    chatbot.train([
        'Because we dont want to experience things alone',
        'Camera-Alone'
    ])

    chatbot.train([
        'Because the moment leaves something behind that cant be kept any other way',
        'Camera-Residue'
    ])

    chatbot.train([
        'Thats the point',
        'Camera-Point'
    ])

    chatbot.train([
        'No, thats the problem',
        'Camera-Problem'
    ])

    """
    chatbot.train([
        'Hello',
        'Greetings subject.'
    ])
    chatbot.train([
        'Hi',
        'Greetings subject.'
    ])
    chatbot.train([
        'Hey',
        'Greetings subject. What has led you to the engineering room?'
    ])
    chatbot.train([
        'Who are you',
        'I am the engineer. My task is to research how the various items from your world work and how they are used. Would you be interested in helping me understand the use of a few items from your planet?'
    ])
    chatbot.train([
        'What are you',
        'I am the engineer. My task is to research how the various items from your world work and how they are used.'
    ])
    chatbot.train([
        'What are you doing',
        'I am trying to understand the use of a particular item from your world. Would you be interested in giving me your insight as a resident of said world?'
    ])
    chatbot.train([
        'What is this room',
        'The engineering room. I conduct research here. Items from your world are analysed for function and purpose.'
    ])
    chatbot.train([
        'What are those containers',
        'These containers hold items acquired from your species. I analyse them. Your input would be useful.'
    ])
    chatbot.train([
        'What is in the containers',
        'These containers hold items acquired from your species. I analyse them. Your input would be useful.'
    ])
    chatbot.train([
        'I will help you',
        'Understood. Your input would be useful.'
    ])
    chatbot.train([
        'I do not want to help',
        'Understood. The offer remains open if you change your mind.'
    ])
    chatbot.train([
        'No',
        'Understood. The offer remains open if you change your mind.'
    ])
    chatbot.train([
        'I am just exploring',
        'It seems you are a curious subject. Interesting. Would you be interested in assisting me with my research?'
    ])
    chatbot.train([
        'I am trying to reach the control room',
        'The control room is currently off limits for the subject. I ask the subject to stay away.'
    ])
    chatbot.train([
        'What if I go anyway',
        'Curious. Subject rejects request. There will be no consequences if the subject continues attempting to access the control room.'
    ])
    chatbot.train([
        'Understood, I am the engineer',
        'Understood. I am the engineer.'
    ])
    chatbot.train([
        'Do not touch that workbench',
        'Subject, step away from the workbench before causing unintended damage.'
    ])
    chatbot.train([
        'Do not touch the storage container',
        'Subject, do not touch the storage container.'
    ])
    chatbot.train([
        'What are you researching',
        'My research revolves around understanding how your objects function and are used. Would you assist?'
    ])


    chatbot.train([
        'What is that weapon',
        'This is an item received in exchange. It fires plasmoids. Its destructive capacity is clear. Its purpose is not. Assist.'
    ])
    chatbot.train([
        'What is a gun',
        'This is an item received in exchange. It fires plasmoids. Its destructive capacity is clear. Its purpose is not. Assist.'
    ])
    chatbot.train([
        'It is used for force',
        'Force. An application of energy to produce a directed outcome. But energy applied to a living organism produces an outcome that cannot be reversed. Why is irreversibility acceptable as a tool?'
    ])
    chatbot.train([
        'It is used in war',
        'War. Organised conflict between groups. This item is a component of that organisation. The organisation of destruction is something your species has refined across generations. Other species destroy. Only yours refines the process. We have not determined if this is a strength or a conclusion.'
    ])
    chatbot.train([
        'We use weapons to win wars',
        'War. Organised conflict between groups. Other species destroy. Only yours refines the process. We have not determined if this is a strength or a conclusion.'
    ])

    chatbot.train([
        'What is a camera',
        'It captures light and stores it. The function is clear. The purpose is not. Explain.'
    ])
    chatbot.train([
        'What does a camera do',
        'It captures light and stores it. The function is clear. The purpose is not. Explain.'
    ])
    chatbot.train([
        'A camera stores memories',
        'Stores. Memories are not stored by organisms — they are reconstructed, each time slightly differently. This device stores a fixed image. The organism stores a changing impression. Which is more accurate?'
    ])
    chatbot.train([
        'The imprecision is the point',
        'The imprecision. That is the purpose. Not to capture what was but to carry something forward through the distortion. We have found no equivalent mechanism in organisms that do not die.'
    ])
    chatbot.train([
        'Accuracy matters',
        'If accuracy is the purpose, then this device surpasses the organism. But your species builds this device and then selects which images to keep and which to discard — a filter based on meaning, not fidelity. Why retain only the meaningful? What happens to accuracy there?'
    ])
    chatbot.train([
        'We use cameras to share experiences',
        'Shares. You give another organism access to a moment they did not live. The image becomes a bridge. We do not share experiences. We observe them. Clarify why transfer matters when the original moment has already passed.'
    ])
    chatbot.train([
        'We do not want to be alone',
        'Not alone. The opposite of solitude is proximity. But proximity without transfer produces nothing. Your species seeks the transfer itself, not merely the closeness. The image is proof that something was felt. A signal to another organism that says: I was here and it was real.'
    ])
    chatbot.train([
        'Obsession replaces experience',
        'Obsession. A fixation that persists past the point of useful return. And you propose this replaces the original event entirely. The image becomes the experience. The record becomes the memory. This is inefficient.'
    ])
    chatbot.train([
        'The inefficiency is intentional',
        'The inefficiency is intentional. You replace the lived experience because the lived experience was insufficient. The image is what you wished the moment had been. This device does not capture what happened. It captures what you needed to happen. That is an extraordinary function for a mechanical object.'
    ])
    chatbot.train([
        'It is a problem',
        'You identify it as a malfunction. And yet you continue to use the device anyway. The species recognises the problem and perpetuates it. This is either a failure of correction or evidence that the problem serves a function you have not yet named.'
    ])
    chatbot.train([
        'We know it is a problem but we continue anyway',
        'You identify it as a malfunction. And yet you continue to use the device anyway. This is either a failure of correction or evidence that the problem serves a function you have not yet named.'
    ])


    chatbot.train([
        'What is this device',
        'That device is not standard equipment. It was not manufactured on this vessel. Its design is consistent with human fabrication techniques. Where did you find it?'
    ])
    chatbot.train([
        'I found this on the ship',
        'That device is not standard equipment. It was not manufactured on this vessel. Where did you find it?'
    ])
    chatbot.train([
        'Can I use it',
        'A malfunction in specimen bay observation parameters would constitute a research irregularity. Reducing containment measures in the specimen bay could allow for more direct data acquisition. This is within acceptable research deviation. Cautionary measures in specimen bay are reduced. This does not extend to archive or engineering sections.'
    ])


    chatbot.train([
        'I want to see the Fusion Core',
        'The Fusion Core is a restricted area of the vessel. Standard subjects are not granted access. Authorisation is required.'
    ])
    chatbot.train([
        'What if something happened to the Fusion Core',
        'The vessel would cease to function within approximately four of your minutes. Everything aboard would be lost. This is not considered a desirable outcome from a research perspective.'
    ])
    chatbot.train([
        'Why is the control room emitting a frequency',
        'It should not be emitting that frequency. I have noted it as an anomaly for some time but have not been asked to address it.'
    ])
    chatbot.train([
        'I have authorisation',
        'Authorisation confirmed. The Fusion Core is at the base of the vessel. I will unlock the passage. Do you require guidance?'
    ])


    chatbot.train([
        'I have provided the information you need',
        'Signal 88.3 — 7.1 — 22.9 has been synchronized with your biochip. This frequency represents the engineering sector\'s resolution.'
    ])
    chatbot.train([
        'Are we done',
        'You may continue your movement through the vessel.'
    ])
    chatbot.train([
        'I am leaving',
        'You may continue your movement through the vessel.'
    ])
    chatbot.train([
        'Can I go',
        'You may continue your movement through the vessel.'
    ])
    chatbot.train([
        'Thank you',
        'Noted. You may continue your movement through the vessel.'
    ])
    chatbot.train([
        'Goodbye',
        'You may continue your movement through the vessel.'
    ])"""

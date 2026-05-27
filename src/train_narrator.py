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

    # ── What-Need ────────────────────────────────────────────────────────────
    chatbot.train(['What exactly do you need from me', 'What-Need'])
    chatbot.train(['What is it you need from me', 'What-Need'])
    chatbot.train(['What exactly are you looking for from me', 'What-Need'])
    chatbot.train(['Tell me what you actually need', 'What-Need'])
    chatbot.train(['What do you want me to do for you', 'What-Need'])

    # ── Used-Me ──────────────────────────────────────────────────────────────
    chatbot.train(['You used me. You used the other person too and they died.', 'Used-Me'])
    chatbot.train(['You used me and used the other person too and they died because of it', 'Used-Me'])
    chatbot.train(['You used both of us. The other person did not survive.', 'Used-Me'])
    chatbot.train(['You manipulated me and the other person ended up dead', 'Used-Me'])
    chatbot.train(['You used me like you used them and they did not make it', 'Used-Me'])

    # ── Biochip ──────────────────────────────────────────────────────────────
    chatbot.train(['Youve been watching me this whole time through the biochip.', 'Biochip'])
    chatbot.train(['You have been monitoring me through the biochip the whole time', 'Biochip'])
    chatbot.train(['The biochip has been giving you everything I said and did', 'Biochip'])
    chatbot.train(['You watched everything I did through that chip in my brain', 'Biochip'])
    chatbot.train(['You have been listening through the biochip this whole time havent you', 'Biochip'])

    # ── Body ─────────────────────────────────────────────────────────────────
    chatbot.train(['The body in that room. You said the ship processes everything. It didnt process them', 'Body'])
    chatbot.train(['The ship processes everything you said. So why is there still a body in that room', 'Body'])
    chatbot.train(['You told me the ship processes everything. Then why is someone still there', 'Body'])
    chatbot.train(['That person in the discarded room was not processed. Why not', 'Body'])
    chatbot.train(['There is a body in there and you said the ship handles everything. Explain that', 'Body'])

    # ── Organization ─────────────────────────────────────────────────────────
    chatbot.train(['Your organisation. Who do they actually answer to?', 'Organization'])
    chatbot.train(['Who does your organization answer to', 'Organization'])
    chatbot.train(['Who is actually in charge of your organization', 'Organization'])
    chatbot.train(['What authority does your organization operate under', 'Organization'])
    chatbot.train(['Who controls the organization you work for', 'Organization'])

    # ── Grieve ───────────────────────────────────────────────────────────────
    chatbot.train(['Did you grieve them? The first person', 'Grieve'])
    chatbot.train(['Did you mourn the first person', 'Grieve'])
    chatbot.train(['Did you feel anything when the first one died', 'Grieve'])
    chatbot.train(['Have you grieved for what happened to the first person', 'Grieve'])
    chatbot.train(['Do you even grieve for the people you lose', 'Grieve'])

    # ── Believe ──────────────────────────────────────────────────────────────
    chatbot.train(['Do you actually believe humanity is worth what youve done for it?', 'Believe'])
    chatbot.train(['Do you actually think humanity is worth all of this', 'Believe'])
    chatbot.train(['Do you really believe what you did was worth it for humanity', 'Believe'])
    chatbot.train(['Is humanity actually worth what you put both of us through', 'Believe'])
    chatbot.train(['Do you genuinely believe humanity deserved all of this', 'Believe'])

    # ── Continue ─────────────────────────────────────────────────────────────
    chatbot.train(['Continue', 'Continue'])
    chatbot.train(['Go on', 'Continue'])
    chatbot.train(['Keep going', 'Continue'])
    chatbot.train(['I want to hear more', 'Continue'])
    chatbot.train(['Please continue', 'Continue'])

    # ── Who ──────────────────────────────────────────────────────────────────
    chatbot.train(['Who are you really', 'Who'])
    chatbot.train(['Who are you', 'Who'])
    chatbot.train(['Who exactly are you', 'Who'])
    chatbot.train(['Can you tell me who you really are', 'Who'])
    chatbot.train(['What is your real identity', 'Who'])

    # ── Heard ────────────────────────────────────────────────────────────────
    chatbot.train(['So everything I said to the aliens, you heard.', 'Heard'])
    chatbot.train(['So you heard everything I said to the aliens', 'Heard'])
    chatbot.train(['You were listening to every conversation I had with them', 'Heard'])
    chatbot.train(['Everything I said to them you heard through the biochip', 'Heard'])
    chatbot.train(['You received everything I told the aliens', 'Heard'])

    # ── Intervene ────────────────────────────────────────────────────────────
    chatbot.train(['Did you ever intervene in what I said to them', 'Intervene'])
    chatbot.train(['Did you ever step in and change what I said to them', 'Intervene'])
    chatbot.train(['Have you ever interfered with my conversations with the aliens', 'Intervene'])
    chatbot.train(['Did you change anything about my interactions with them', 'Intervene'])
    chatbot.train(['Were you ever involved in shaping what I communicated to them', 'Intervene'])

    # ── Not-Answer ───────────────────────────────────────────────────────────
    chatbot.train(['Thats not an answer', 'Not-Answer'])
    chatbot.train(['You are not actually answering me', 'Not-Answer'])
    chatbot.train(['That is not what I asked', 'Not-Answer'])
    chatbot.train(['You are avoiding the question', 'Not-Answer'])
    chatbot.train(['That does not answer what I asked', 'Not-Answer'])

    # ── Think ────────────────────────────────────────────────────────────────
    chatbot.train(['I think you do', 'Think'])
    chatbot.train(['I believe you do', 'Think'])
    chatbot.train(['I think that is what you feel', 'Think'])
    chatbot.train(['I am pretty sure you do', 'Think'])
    chatbot.train(['You do I think you do', 'Think'])

    # ── Now ──────────────────────────────────────────────────────────────────
    chatbot.train(['And now?', 'Now'])
    chatbot.train(['So what happens now', 'Now'])
    chatbot.train(['What now', 'Now'])
    chatbot.train(['Where do we go from here', 'Now'])
    chatbot.train(['What comes next', 'Now'])

    # ── Tell-Me ──────────────────────────────────────────────────────────────
    chatbot.train(['Were you ever going to tell me any of this?', 'Tell-Me'])
    chatbot.train(['Were you ever planning to tell me any of this', 'Tell-Me'])
    chatbot.train(['Were you going to tell me the truth at any point', 'Tell-Me'])
    chatbot.train(['When were you going to tell me all of this', 'Tell-Me'])
    chatbot.train(['Did you ever intend to tell me', 'Tell-Me'])
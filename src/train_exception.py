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

    # ── A ────────────────────────────────────────────────────────────────────
    chatbot.train(['Hey, can you understand what I am saying', 'A'])
    chatbot.train(['Can you hear me', 'A'])
    chatbot.train(['Do you understand what I am saying', 'A'])
    chatbot.train(['Can you understand me at all', 'A'])
    chatbot.train(['Are you able to understand me', 'A'])

    # ── B ────────────────────────────────────────────────────────────────────
    chatbot.train(['I guess you can understand me. What am I even doing here', 'B'])
    chatbot.train(['What am I supposed to be doing here', 'B'])
    chatbot.train(['Why am I here', 'B'])
    chatbot.train(['What is the point of all this', 'B'])
    chatbot.train(['I do not even know why I am here', 'B'])

    # ── C ────────────────────────────────────────────────────────────────────
    chatbot.train(['How is it that I escaped so easily', 'C'])
    chatbot.train(['How did I get out so easily', 'C'])
    chatbot.train(['Why was escaping so simple', 'C'])
    chatbot.train(['Getting out of there was way too easy', 'C'])
    chatbot.train(['That seemed far too easy to escape from', 'C'])

    # ── Voice ────────────────────────────────────────────────────────────────
    chatbot.train(['I heard a voice telling me that I was kidnapped here by fellow humans and that I am here to be researched on. So what is the end goal here?', 'Voice'])
    chatbot.train(['A voice told me I was sold here by my own kind. So whats the actual end goal?', 'Voice'])
    chatbot.train(['Someone told me I was sold here by my own people. What exactly is the plan?', 'Voice'])
    chatbot.train(['I heard a voice say I was brought here to be studied. What is the actual goal?', 'Voice'])
    chatbot.train(['A voice said humans sold me to you. What do you actually want with me?', 'Voice'])

    # ── Passing-Through ──────────────────────────────────────────────────────
    chatbot.train(['Dont mind me, just passing through.', 'Passing-Through'])
    chatbot.train(['Just passing by', 'Passing-Through'])
    chatbot.train(['I am just walking through', 'Passing-Through'])
    chatbot.train(['Pay no attention to me I am just going through', 'Passing-Through'])
    chatbot.train(['Do not mind me just passing', 'Passing-Through'])

    # ── Voice-Human ──────────────────────────────────────────────────────────
    chatbot.train(['How do you know its a human voice', 'Voice-Human'])
    chatbot.train(['How do you know that voice is human', 'Voice-Human'])
    chatbot.train(['What makes you think it is human', 'Voice-Human'])
    chatbot.train(['Why would it be a human voice', 'Voice-Human'])
    chatbot.train(['Are you sure it is a human voice', 'Voice-Human'])

    # ── Voice-Also-Hear ──────────────────────────────────────────────────────
    chatbot.train(['You can also hear it', 'Voice-Also-Hear'])
    chatbot.train(['So you hear it too', 'Voice-Also-Hear'])
    chatbot.train(['Can you hear it as well', 'Voice-Also-Hear'])
    chatbot.train(['You can hear the voice too', 'Voice-Also-Hear'])
    chatbot.train(['You also hear what I am hearing', 'Voice-Also-Hear'])

    # ── Where-Go ─────────────────────────────────────────────────────────────
    chatbot.train(['Where do I go from here', 'Where-Go'])
    chatbot.train(['What direction should I go', 'Where-Go'])
    chatbot.train(['Which way do I go', 'Where-Go'])
    chatbot.train(['Where should I head', 'Where-Go'])
    chatbot.train(['What should I do next', 'Where-Go'])

    # ── Voice-Saying ─────────────────────────────────────────────────────────
    chatbot.train(['What has the voice been saying', 'Voice-Saying'])
    chatbot.train(['What does the voice keep saying', 'Voice-Saying'])
    chatbot.train(['What is the voice telling you', 'Voice-Saying'])
    chatbot.train(['What words does the voice say', 'Voice-Saying'])
    chatbot.train(['What message is the voice giving', 'Voice-Saying'])

    # ── Voice-Actually-Human ─────────────────────────────────────────────────
    chatbot.train(['Do you mean it just sounds human or is it an actual human saying it', 'Voice-Actually-Human'])
    chatbot.train(['Is it really a human voice or just something that sounds like one', 'Voice-Actually-Human'])
    chatbot.train(['Are you saying it is literally a human or just sounds like one', 'Voice-Actually-Human'])
    chatbot.train(['Do you mean it is genuinely a human speaking or just sounds that way', 'Voice-Actually-Human'])
    chatbot.train(['Is the voice actually from a human being or just humanlike', 'Voice-Actually-Human'])

    # ── Hallway ──────────────────────────────────────────────────────────────
    chatbot.train(['I will continue down the hallway.', 'Hallway'])
    chatbot.train(['I will head down the hallway', 'Hallway'])
    chatbot.train(['Let me go through the hallway', 'Hallway'])
    chatbot.train(['I am going to go down the hall', 'Hallway'])
    chatbot.train(['Moving through the hallway', 'Hallway'])

    # ── A-Obsessed ───────────────────────────────────────────────────────────
    chatbot.train(['Why are you so obsessed with intent', 'A-Obsessed'])
    chatbot.train(['Why are you so focused on intent', 'A-Obsessed'])
    chatbot.train(['Why does intent matter so much to you', 'A-Obsessed'])
    chatbot.train(['You seem very fixated on the question of intent', 'A-Obsessed'])
    chatbot.train(['What is your obsession with why things are done', 'A-Obsessed'])

    # ── A-Philosophical ──────────────────────────────────────────────────────
    chatbot.train(['Are all aliens this philosophical', 'A-Philosophical'])
    chatbot.train(['Your kind is very philosophical', 'A-Philosophical'])
    chatbot.train(['That is a very philosophical way to look at things', 'A-Philosophical'])
    chatbot.train(['You think about things in a very philosophical way', 'A-Philosophical'])
    chatbot.train(['Is everyone from your world this philosophical', 'A-Philosophical'])

    # ── A-Environment ────────────────────────────────────────────────────────
    chatbot.train(['What kind of environment do you guys even live in for you to think so drastically differently from us humans or any other lifeform on Earth', 'A-Environment'])
    chatbot.train(['What kind of world do you come from, to think so differently from anything on Earth', 'A-Environment'])
    chatbot.train(['What kind of place produces the way you think', 'A-Environment'])
    chatbot.train(['Where do you come from that makes you see things so differently', 'A-Environment'])
    chatbot.train(['What world shaped you to think this differently from humans', 'A-Environment'])

    # ── B-Who-Brought ────────────────────────────────────────────────────────
    chatbot.train(['Who or what brought me here? I dont exactly remember my past, but I am sure it didnt include a place like this.', 'B-Who-Brought'])
    chatbot.train(['Who brought me here? Whatever my past was, it didnt include this.', 'B-Who-Brought'])
    chatbot.train(['What actually brought me to this place', 'B-Who-Brought'])
    chatbot.train(['How did I end up here', 'B-Who-Brought'])
    chatbot.train(['I dont remember how I got here but I know it was not voluntary', 'B-Who-Brought'])

    # ── B-Sold ───────────────────────────────────────────────────────────────
    chatbot.train(['What do you mean by that? Didnt you just say I was sold into your hands and against my will?', 'B-Sold'])
    chatbot.train(['Didnt you just say I was sold here against my will?', 'B-Sold'])
    chatbot.train(['You just said I was sold here. What does that mean exactly?', 'B-Sold'])
    chatbot.train(['Wait are you saying I was traded or sold to get here', 'B-Sold'])
    chatbot.train(['I thought you said I was sold to you against my will', 'B-Sold'])

    # ── B-Earth ──────────────────────────────────────────────────────────────
    chatbot.train(['I want you to bring me back to Earth.', 'B-Earth'])
    chatbot.train(['Send me back to Earth', 'B-Earth'])
    chatbot.train(['Take me back home', 'B-Earth'])
    chatbot.train(['I want to go back to Earth', 'B-Earth'])
    chatbot.train(['Return me to Earth', 'B-Earth'])

    # ── What-Want ────────────────────────────────────────────────────────────
    chatbot.train(['And what the hell do you want me to do up here then? You still havent answered what you want from me', 'What-Want'])
    chatbot.train(['Then what do you actually want from me? You still havent said.', 'What-Want'])
    chatbot.train(['So what do you actually want from me', 'What-Want'])
    chatbot.train(['Tell me what you want from me already', 'What-Want'])
    chatbot.train(['You still have not answered what you want from me', 'What-Want'])

    # ── Fight-Back ───────────────────────────────────────────────────────────
    chatbot.train(['You think I am not willing to fight back', 'Fight-Back'])
    chatbot.train(['Do you think I wont fight back', 'Fight-Back'])
    chatbot.train(['I am not afraid to fight back', 'Fight-Back'])
    chatbot.train(['You think I would not resist', 'Fight-Back'])
    chatbot.train(['I will fight back if I have to', 'Fight-Back'])

    # ── No-Consent ───────────────────────────────────────────────────────────
    chatbot.train(['You dont know the concept of will? You could have just said you dont care about my consent instead of beating around a bush.', 'No-Consent'])
    chatbot.train(['You could have just said you dont care about consent.', 'No-Consent'])
    chatbot.train(['You could have admitted you dont care about consent', 'No-Consent'])
    chatbot.train(['Just admit you did not care whether I agreed or not', 'No-Consent'])
    chatbot.train(['You do not know what consent means do you', 'No-Consent'])

    # ── Uncompliant ──────────────────────────────────────────────────────────
    chatbot.train(['So you didnt even consider me potentially being uncompliant about this? Have you never done something you didnt want to do?', 'Uncompliant'])
    chatbot.train(['So you never considered I might not cooperate?', 'Uncompliant'])
    chatbot.train(['Did it never occur to you that I might resist', 'Uncompliant'])
    chatbot.train(['You never thought about the possibility I might not go along with this', 'Uncompliant'])
    chatbot.train(['What if I simply refused to cooperate', 'Uncompliant'])

    # ── C-Trade ──────────────────────────────────────────────────────────────
    chatbot.train(['What is that even supposed to mean? So you capture me or trade me or whatever you did to me and now you dont even question how I got out of that thing?', 'C-Trade'])
    chatbot.train(['You trade me like cargo and then just dont question how I got out', 'C-Trade'])
    chatbot.train(['You traded me and you do not even care how I escaped', 'C-Trade'])
    chatbot.train(['So I was traded or captured and you have no questions about how I got free', 'C-Trade'])
    chatbot.train(['You brought me here like property and have no curiosity about how I got out', 'C-Trade'])

    # ── Overlook-Home ────────────────────────────────────────────────────────
    chatbot.train(['I think of home. Its surreal seeing how small everything I ever knew is from here.', 'Overlook-Home'])
    chatbot.train(['Home. Everything I ever knew looks very small from here.', 'Overlook-Home'])
    chatbot.train(['I see Earth and it reminds me of home', 'Overlook-Home'])
    chatbot.train(['Looking at Earth from here makes me think about home', 'Overlook-Home'])
    chatbot.train(['It is strange seeing how small home looks from up here', 'Overlook-Home'])

    # ── Overlook-Family ──────────────────────────────────────────────────────
    chatbot.train(['I am reminded of my family and loved ones.', 'Overlook-Family'])
    chatbot.train(['My family comes to mind looking at it', 'Overlook-Family'])
    chatbot.train(['I think of my family and the people I love', 'Overlook-Family'])
    chatbot.train(['Looking at Earth I think of the people I left behind', 'Overlook-Family'])
    chatbot.train(['It makes me think of the people who matter to me', 'Overlook-Family'])

    # ── Overlook-Distant ─────────────────────────────────────────────────────
    chatbot.train(['It feels distant for some reason.', 'Overlook-Distant'])
    chatbot.train(['It feels far away somehow', 'Overlook-Distant'])
    chatbot.train(['For some reason I feel detached from it', 'Overlook-Distant'])
    chatbot.train(['Looking at it I just feel disconnected', 'Overlook-Distant'])
    chatbot.train(['It seems further away than it looks', 'Overlook-Distant'])

    # ── Overlook-Missed ──────────────────────────────────────────────────────
    chatbot.train(['It feels like many missed opportunities.', 'Overlook-Missed'])
    chatbot.train(['I think about all the things I never got to do', 'Overlook-Missed'])
    chatbot.train(['It makes me think about missed chances', 'Overlook-Missed'])
    chatbot.train(['So many opportunities I never took', 'Overlook-Missed'])
    chatbot.train(['I am reminded of the things I left unfinished', 'Overlook-Missed'])

    # ── Overlook-Nothing ─────────────────────────────────────────────────────
    chatbot.train(['It has nothing more to offer me.', 'Overlook-Nothing'])
    chatbot.train(['There is nothing left there for me', 'Overlook-Nothing'])
    chatbot.train(['Earth has nothing more to give me', 'Overlook-Nothing'])
    chatbot.train(['I have no reason to go back', 'Overlook-Nothing'])
    chatbot.train(['It stopped being something I needed a long time ago', 'Overlook-Nothing'])

    # ── Overlook-No-Memory ───────────────────────────────────────────────────
    chatbot.train(['I dont recall anything concrete.', 'Overlook-No-Memory'])
    chatbot.train(['Nothing specific comes to mind', 'Overlook-No-Memory'])
    chatbot.train(['I cannot remember anything specific about it', 'Overlook-No-Memory'])
    chatbot.train(['My mind draws a blank', 'Overlook-No-Memory'])
    chatbot.train(['There is nothing concrete I can recall', 'Overlook-No-Memory'])

    # ── Overlook-Burned ──────────────────────────────────────────────────────
    chatbot.train(['I dont really have fond memories. I would rather have them burned.', 'Overlook-Burned'])
    chatbot.train(['I would rather not remember any of it', 'Overlook-Burned'])
    chatbot.train(['I do not have good memories of it', 'Overlook-Burned'])
    chatbot.train(['I would rather forget everything from that place', 'Overlook-Burned'])
    chatbot.train(['Nothing worth keeping from there', 'Overlook-Burned'])

    # ── Discarded-Why ────────────────────────────────────────────────────────
    chatbot.train(['Why and how are you even here', 'Discarded-Why'])
    chatbot.train(['How and why are you here', 'Discarded-Why'])
    chatbot.train(['What brought you to this place', 'Discarded-Why'])
    chatbot.train(['Why are you here of all places', 'Discarded-Why'])
    chatbot.train(['How did you end up here', 'Discarded-Why'])

    # ── Discarded-Know ───────────────────────────────────────────────────────
    chatbot.train(['Did you know this person', 'Discarded-Know'])
    chatbot.train(['Were you acquainted with this person', 'Discarded-Know'])
    chatbot.train(['Did you have a connection to this person', 'Discarded-Know'])
    chatbot.train(['Did you know who this was', 'Discarded-Know'])
    chatbot.train(['Were you familiar with the person who was here', 'Discarded-Know'])

    # ── Discarded-What ───────────────────────────────────────────────────────
    chatbot.train(['What actually happened to them', 'Discarded-What'])
    chatbot.train(['What happened to this person', 'Discarded-What'])
    chatbot.train(['What did they do to this person', 'Discarded-What'])
    chatbot.train(['How did this person end up here', 'Discarded-What'])
    chatbot.train(['What was done to them', 'Discarded-What'])

    # ── Archive ──────────────────────────────────────────────────────────────
    chatbot.train(['I will return to the archive.', 'Archive'])
    chatbot.train(['I am going back to the archive', 'Archive'])
    chatbot.train(['Take me back to the archive', 'Archive'])
    chatbot.train(['I need to go back to the archive', 'Archive'])
    chatbot.train(['Let me return to the archive', 'Archive'])

    # ── Discarded-Lying ──────────────────────────────────────────────────────
    chatbot.train(['So the narrator has been lying', 'Discarded-Lying'])
    chatbot.train(['The narrator has been lying this whole time', 'Discarded-Lying'])
    chatbot.train(['So the narrator lied about all of this', 'Discarded-Lying'])
    chatbot.train(['Everything the narrator said was a lie', 'Discarded-Lying'])
    chatbot.train(['The narrator has not been telling the truth', 'Discarded-Lying'])

    # ── Discarded-Why-Telling ────────────────────────────────────────────────
    chatbot.train(['Why are you telling me this?', 'Discarded-Why-Telling'])
    chatbot.train(['Why tell me this now', 'Discarded-Why-Telling'])
    chatbot.train(['What is your reason for telling me this', 'Discarded-Why-Telling'])
    chatbot.train(['Why are you sharing this with me', 'Discarded-Why-Telling'])
    chatbot.train(['What made you decide to tell me', 'Discarded-Why-Telling'])

    # ── Discarded-What-Suggest ───────────────────────────────────────────────
    chatbot.train(['What are you suggesting I do?', 'Discarded-What-Suggest'])
    chatbot.train(['What do you think I should do', 'Discarded-What-Suggest'])
    chatbot.train(['What are you suggesting I do about this', 'Discarded-What-Suggest'])
    chatbot.train(['What would you have me do with this information', 'Discarded-What-Suggest'])
    chatbot.train(['So what is your suggestion', 'Discarded-What-Suggest'])

    # ── Exit-Want ────────────────────────────────────────────────────────────
    chatbot.train(['What do you want?', 'Exit-Want'])
    chatbot.train(['What is it you want', 'Exit-Want'])
    chatbot.train(['What do you actually want', 'Exit-Want'])
    chatbot.train(['Why are you here what do you want', 'Exit-Want'])
    chatbot.train(['Tell me what you want', 'Exit-Want'])

    # ── Exit-Following ───────────────────────────────────────────────────────
    chatbot.train(['Are you following me around the ship?', 'Exit-Following'])
    chatbot.train(['Have you been following me', 'Exit-Following'])
    chatbot.train(['Are you trailing me around the ship', 'Exit-Following'])
    chatbot.train(['Why are you following me', 'Exit-Following'])
    chatbot.train(['I keep seeing you everywhere are you following me', 'Exit-Following'])

    # ── Exit-Fine ────────────────────────────────────────────────────────────
    chatbot.train(['I dont mind, honestly', 'Exit-Fine'])
    chatbot.train(['That is fine with me', 'Exit-Fine'])
    chatbot.train(['I do not have a problem with that', 'Exit-Fine'])
    chatbot.train(['It does not bother me', 'Exit-Fine'])
    chatbot.train(['Fine by me', 'Exit-Fine'])

    # ── Exit-Stopped ─────────────────────────────────────────────────────────
    chatbot.train(['The thing in there stopped responding to me.', 'Exit-Stopped'])
    chatbot.train(['The machine in there stopped working', 'Exit-Stopped'])
    chatbot.train(['Whatever was in that room stopped responding', 'Exit-Stopped'])
    chatbot.train(['Something in there just stopped working', 'Exit-Stopped'])
    chatbot.train(['It is not responding to me anymore', 'Exit-Stopped'])

    # ── Exit-Yes ─────────────────────────────────────────────────────────────
    chatbot.train(['A little', 'Exit-Yes'])
    chatbot.train(['Yeah a little', 'Exit-Yes'])
    chatbot.train(['Somewhat', 'Exit-Yes'])
    chatbot.train(['Yes a bit', 'Exit-Yes'])
    chatbot.train(['Kind of', 'Exit-Yes'])

    # ── Exit-No ──────────────────────────────────────────────────────────────
    chatbot.train(['No', 'Exit-No'])
    chatbot.train(['Not really', 'Exit-No'])
    chatbot.train(['No not at all', 'Exit-No'])
    chatbot.train(['I would say no', 'Exit-No'])
    chatbot.train(['No I do not', 'Exit-No'])

    # ── Pre-Control-Room ─────────────────────────────────────────────────────
    chatbot.train(['I dont know yet', 'Pre-Control-Room'])
    chatbot.train(['Alright, just move out of the way then.', 'Pre-Control-Room'])
    chatbot.train(['I have not decided yet', 'Pre-Control-Room'])
    chatbot.train(['Move aside please', 'Pre-Control-Room'])
    chatbot.train(['Step out of the way', 'Pre-Control-Room'])
    chatbot.train(['I am just going through', 'Pre-Control-Room'])
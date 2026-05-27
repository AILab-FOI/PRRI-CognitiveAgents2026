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

    # ── Brain ────────────────────────────────────────────────────────────────
    chatbot.train(['Are you the colleague who messed with my brain?', 'Brain'])
    chatbot.train(['Did you tamper with my brain', 'Brain'])
    chatbot.train(['You were the one who altered my brain werent you', 'Brain'])
    chatbot.train(['Was it you that interfered with my head', 'Brain'])
    chatbot.train(['Are you responsible for what was done to my brain', 'Brain'])

    # ── Place ────────────────────────────────────────────────────────────────
    chatbot.train(['What exactly is this place?', 'Place'])
    chatbot.train(['Where am I right now', 'Place'])
    chatbot.train(['What kind of facility is this', 'Place'])
    chatbot.train(['Can you tell me what this room is', 'Place'])
    chatbot.train(['What is this location', 'Place'])

    # ── Alive ────────────────────────────────────────────────────────────────
    chatbot.train(['Are those things alive', 'Alive'])
    chatbot.train(['Are those specimens alive', 'Alive'])
    chatbot.train(['Is there life in those containers', 'Alive'])
    chatbot.train(['Do those things have life in them', 'Alive'])
    chatbot.train(['Are the things in here living', 'Alive'])

    # ── Studying ─────────────────────────────────────────────────────────────
    chatbot.train(['Youre studying me arent you', 'Studying'])
    chatbot.train(['You are observing me right now', 'Studying'])
    chatbot.train(['Am I being studied', 'Studying'])
    chatbot.train(['You are analyzing me arent you', 'Studying'])
    chatbot.train(['I am a subject of your research', 'Studying'])

    # ── Wrong ────────────────────────────────────────────────────────────────
    chatbot.train(['This is wrong', 'Wrong'])
    chatbot.train(['What you are doing is wrong', 'Wrong'])
    chatbot.train(['This should not be happening', 'Wrong'])
    chatbot.train(['None of this is right', 'Wrong'])
    chatbot.train(['This is morally wrong', 'Wrong'])

    # ── Memory ───────────────────────────────────────────────────────────────
    chatbot.train(['I dont remember anything', 'Memory'])
    chatbot.train(['I have no memory of how I got here', 'Memory'])
    chatbot.train(['My memories are gone', 'Memory'])
    chatbot.train(['I cant recall anything', 'Memory'])
    chatbot.train(['Everything before this is blank to me', 'Memory'])

    # ── Who-I ────────────────────────────────────────────────────────────────
    chatbot.train(['I remember who Im meant to be', 'Who-I'])
    chatbot.train(['I still know who I am', 'Who-I'])
    chatbot.train(['My identity is intact', 'Who-I'])
    chatbot.train(['I havent forgotten who I am', 'Who-I'])
    chatbot.train(['I know my own identity', 'Who-I'])

    # ── Build ────────────────────────────────────────────────────────────────
    chatbot.train(['Why even build something like this in my brain', 'Build'])
    chatbot.train(['Why did you implant something in my head', 'Build'])
    chatbot.train(['Why put a device in my brain', 'Build'])
    chatbot.train(['What was the reason for adding something to my brain', 'Build'])
    chatbot.train(['Why would you construct something inside my mind', 'Build'])

    # ── Puzzle-Intro ─────────────────────────────────────────────────────────
    chatbot.train(['Continue to the specimen test', 'Puzzle-Intro'])
    chatbot.train(['Lets proceed with the test', 'Puzzle-Intro'])
    chatbot.train(['Show me the specimen', 'Puzzle-Intro'])
    chatbot.train(['Move on to the specimen', 'Puzzle-Intro'])
    chatbot.train(['Take me to the test', 'Puzzle-Intro'])
    chatbot.train(['I want to see the specimen test', 'Puzzle-Intro'])

    # ── Worse ────────────────────────────────────────────────────────────────
    chatbot.train(['Thats somehow worse than if youd just taken them', 'Worse'])
    chatbot.train(['That makes it even worse', 'Worse'])
    chatbot.train(['That is actually more disturbing than just taking them', 'Worse'])
    chatbot.train(['Somehow that feels like a bigger violation', 'Worse'])
    chatbot.train(['That is worse not better', 'Worse'])

    # ── Recording ────────────────────────────────────────────────────────────
    chatbot.train(['So Im just a live recording to you.', 'Recording'])
    chatbot.train(['I am just data to you', 'Recording'])
    chatbot.train(['You see me as a walking recording', 'Recording'])
    chatbot.train(['To you I am just a living data source', 'Recording'])
    chatbot.train(['I am nothing more than a live feed to you', 'Recording'])

    # ── Compare ──────────────────────────────────────────────────────────────
    chatbot.train(['Compare to what?', 'Compare'])
    chatbot.train(['What are you comparing me to', 'Compare'])
    chatbot.train(['What is the baseline you are comparing against', 'Compare'])
    chatbot.train(['What exactly am I being compared to', 'Compare'])
    chatbot.train(['Compared to who', 'Compare'])

    # ── Sample ───────────────────────────────────────────────────────────────
    chatbot.train(['So Im just another sample', 'Sample'])
    chatbot.train(['Am I just a specimen to you', 'Sample'])
    chatbot.train(['I am nothing but a sample in your collection', 'Sample'])
    chatbot.train(['You treat me like just another test subject', 'Sample'])
    chatbot.train(['I am just one more subject for you to analyze', 'Sample'])

    # ── Moving ───────────────────────────────────────────────────────────────
    chatbot.train(['Theyre moving', 'Moving'])
    chatbot.train(['Those things are moving', 'Moving'])
    chatbot.train(['I can see them moving', 'Moving'])
    chatbot.train(['The specimens are moving', 'Moving'])
    chatbot.train(['They just moved', 'Moving'])

    # ── Feel-Alive ───────────────────────────────────────────────────────────
    chatbot.train(['They feel alive', 'Feel-Alive'])
    chatbot.train(['Those specimens feel like living things', 'Feel-Alive'])
    chatbot.train(['Something about them feels alive', 'Feel-Alive'])
    chatbot.train(['There is something alive about them', 'Feel-Alive'])
    chatbot.train(['They give off a sense of being alive', 'Feel-Alive'])

    # ── Blurry ───────────────────────────────────────────────────────────────
    chatbot.train(['I feel like the definition cant be that blurry.', 'Blurry'])
    chatbot.train(['The line between alive and not alive shouldnt be this unclear', 'Blurry'])
    chatbot.train(['Surely alive and not alive is a clear distinction', 'Blurry'])
    chatbot.train(['That distinction cant really be so vague', 'Blurry'])
    chatbot.train(['The definition of alive should be clearer than that', 'Blurry'])

    # ── Consent ──────────────────────────────────────────────────────────────
    chatbot.train(['Youre experimenting on me without consent', 'Consent'])
    chatbot.train(['I never agreed to this', 'Consent'])
    chatbot.train(['You did not ask for my permission', 'Consent'])
    chatbot.train(['This was done without my knowledge or consent', 'Consent'])
    chatbot.train(['You had no right to do this without my consent', 'Consent'])

    # ── Objects ──────────────────────────────────────────────────────────────
    chatbot.train(['Youre treating people like objects', 'Objects'])
    chatbot.train(['You treat humans as if they are just things', 'Objects'])
    chatbot.train(['We are not objects to be studied', 'Objects'])
    chatbot.train(['People are not specimens for you to analyze', 'Objects'])
    chatbot.train(['You reduce people to data points', 'Objects'])

    # ── Understand ───────────────────────────────────────────────────────────
    chatbot.train(['You dont even understand what youre doing.', 'Understand'])
    chatbot.train(['You have no idea what the consequences are', 'Understand'])
    chatbot.train(['You clearly do not grasp the implications of this', 'Understand'])
    chatbot.train(['You do not understand the impact of your research', 'Understand'])
    chatbot.train(['You are operating without any real comprehension', 'Understand'])

    # ── Course ───────────────────────────────────────────────────────────────
    chatbot.train(['Of course its required', 'Course'])
    chatbot.train(['Obviously it is necessary', 'Course'])
    chatbot.train(['It had to be done', 'Course'])
    chatbot.train(['That was clearly a requirement', 'Course'])
    chatbot.train(['Of course that was needed', 'Course'])

    # ── Why-Doing ────────────────────────────────────────────────────────────
    chatbot.train(['So you dont even know why youre doing this', 'Why-Doing'])
    chatbot.train(['You are doing this without knowing the reason', 'Why-Doing'])
    chatbot.train(['You do not have a clear purpose for this research', 'Why-Doing'])
    chatbot.train(['You have no real answer for why this is happening', 'Why-Doing'])
    chatbot.train(['You cannot explain the purpose of what you are doing', 'Why-Doing'])

    # ── Learned ──────────────────────────────────────────────────────────────
    chatbot.train(['What have you learned so far', 'Learned'])
    chatbot.train(['What findings have you collected', 'Learned'])
    chatbot.train(['What conclusions have you reached', 'Learned'])
    chatbot.train(['What have you discovered about me', 'Learned'])
    chatbot.train(['What does your research show', 'Learned'])

    # ── Left ─────────────────────────────────────────────────────────────────
    chatbot.train(['The left one is structured differently', 'Left'])
    chatbot.train(['The one on the left has a different structure', 'Left'])
    chatbot.train(['I notice the left specimen is structured differently', 'Left'])
    chatbot.train(['There is something different about the structure of the left one', 'Left'])
    chatbot.train(['The left specimen looks different from the right', 'Left'])

    # ── Right ────────────────────────────────────────────────────────────────
    chatbot.train(['The right one feels fake', 'Right'])
    chatbot.train(['The one on the right seems artificial', 'Right'])
    chatbot.train(['The right specimen does not feel real', 'Right'])
    chatbot.train(['Something about the right one seems off', 'Right'])
    chatbot.train(['The right one does not look natural', 'Right'])

    # ── Probability ──────────────────────────────────────────────────────────
    chatbot.train(['One of these is probably wrong', 'Probability'])
    chatbot.train(['I think one of them is incorrect', 'Probability'])
    chatbot.train(['There is likely a false one here', 'Probability'])
    chatbot.train(['One of these probably does not belong', 'Probability'])
    chatbot.train(['I am guessing one of these is the odd one out', 'Probability'])

    # ── No-Signal ────────────────────────────────────────────────────────────
    chatbot.train(['No thanks Ill just keep exploring the ship', 'No-Signal'])
    chatbot.train(['I would rather not I will continue on my own', 'No-Signal'])
    chatbot.train(['I will pass on that', 'No-Signal'])
    chatbot.train(['I am going to skip the test', 'No-Signal'])
    chatbot.train(['I would prefer to keep moving', 'No-Signal'])

    # ── Greater-Design ───────────────────────────────────────────────────────
    chatbot.train(['The greater design is a bundle of theories that mean to explain the greater purposes of our existence', 'Greater-Design'])
    chatbot.train(['A bundle of theories trying to explain why any of this exists.', 'Greater-Design'])
    chatbot.train(['A collection of theories about why existence has meaning', 'Greater-Design'])
    chatbot.train(['Ideas about why everything exists and what it all means', 'Greater-Design'])
    chatbot.train(['It is the set of ideas humans use to explain why any of this is here', 'Greater-Design'])
    chatbot.train(['Theories that try to find meaning and purpose behind existence itself', 'Greater-Design'])

    # ── Carry-Yes ────────────────────────────────────────────────────────────
    chatbot.train(['I suppose I do. Everyone does, whether they admit it or not', 'Carry-Yes'])
    chatbot.train(['Yes I carry something unresolved', 'Carry-Yes'])
    chatbot.train(['I think everyone has something unresolved they carry with them', 'Carry-Yes'])
    chatbot.train(['Yeah I do carry something I have not worked out', 'Carry-Yes'])
    chatbot.train(['I carry it whether I want to or not', 'Carry-Yes'])

    # ── Carry-Know ───────────────────────────────────────────────────────────
    chatbot.train(['Not really. I just know it exists.', 'Carry-Know'])
    chatbot.train(['I know it is there but I do not carry it with me', 'Carry-Know'])
    chatbot.train(['I am aware of it but it does not weigh on me', 'Carry-Know'])
    chatbot.train(['I know about it but I do not really think about it', 'Carry-Know'])
    chatbot.train(['It exists but I keep it at a distance', 'Carry-Know'])

    # ── Carry-Used ───────────────────────────────────────────────────────────
    chatbot.train(['I used to. Not so much anymore', 'Carry-Used'])
    chatbot.train(['I did once but not now', 'Carry-Used'])
    chatbot.train(['There was a time when I did but that has passed', 'Carry-Used'])
    chatbot.train(['I used to carry it but I have let it go', 'Carry-Used'])
    chatbot.train(['Maybe at some point but not anymore', 'Carry-Used'])

    # ── Carry-No ─────────────────────────────────────────────────────────────
    chatbot.train(['I dont think about it much', 'Carry-No'])
    chatbot.train(['Not really it does not occupy my thoughts', 'Carry-No'])
    chatbot.train(['No I do not carry anything like that', 'Carry-No'])
    chatbot.train(['I try not to think about those kinds of things', 'Carry-No'])
    chatbot.train(['I do not spend time on unresolved things', 'Carry-No'])

    # ── Exit ─────────────────────────────────────────────────────────────────
    chatbot.train(['Exit the specimen bay', 'Exit'])
    chatbot.train(['I want to leave', 'Exit'])
    chatbot.train(['Let me out of here', 'Exit'])
    chatbot.train(['I am done here I want to leave the specimen bay', 'Exit'])
    chatbot.train(['I would like to exit now', 'Exit'])
    chatbot.train(['Time to go', 'Exit'])
    chatbot.train(['I am leaving', 'Exit'])
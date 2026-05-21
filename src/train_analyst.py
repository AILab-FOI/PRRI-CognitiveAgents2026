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
        'Are you the colleague who messed with my brain?',
        'Brain'
    ])

    chatbot.train([
        'What exactly is this place?',
        'Place'
    ])

    chatbot.train([
        'Are those things alive',
        'Alive'
    ])

    chatbot.train([
        'Youre studying me, arent you?',
        'Studying'
    ])

    chatbot.train([
        'This is wrong',
        'Wrong'
    ])

    chatbot.train([
        'I dont remember anything',
        'Memory'
    ])

    chatbot.train([
        'I remember who Im meant to be',
        'Who-I'
    ])

    chatbot.train([
        'Why even build something like this in my brain',
        'Build'
    ])

    chatbot.train([
        'Continue to the specimen test',
        'Puzzle-Intro'
    ])

    chatbot.train([
        'Thats somehow worse than if youd just taken them',
        'Worse'
    ])

    chatbot.train([
        'So Im just a live recording to you.',
        'Recording'
    ])

    chatbot.train([
        'Compare to what?',
        'Compare'
    ])

    chatbot.train([
        'So Im just another sample',
        'Sample'
    ])

    chatbot.train([
        'Theyre moving',
        'Moving'
    ])

    chatbot.train([
        'They feel alive',
        'Feel-Alive'
    ])

    chatbot.train([
        'I feel like the definition cant be that blurry.',
        'Blurry'
    ])

    chatbot.train([
        'Youre experimenting on me without consent',
        'Consent'
    ])

    chatbot.train([
        'Youre treating people like objects',
        'Objects'
    ])

    chatbot.train([
        'You dont even understand what youre doing.',
        'Understand'
    ])

    chatbot.train([
        'Of course its required',
        'Course'
    ])

    chatbot.train([
        'So you dont even know why youre doing this',
        'Why-Doing'
    ])

    chatbot.train([
        'What have you learned so far',
        'Learned'
    ])

    chatbot.train([
        'The left one is structured differently',
        'Left'
    ])

    chatbot.train([
        'The right one feels fake',
        'Right'
    ])

    chatbot.train([
        'One of these is probably wrong',
        'Probability'
    ])

    chatbot.train([
        'No thanks, Ill just keep exploring the ship',
        'No-Signal'
    ])

    chatbot.train([
        'The greater design is a bundle of theories that mean to explain the greater purposes of our existence',
        'Greater-Design'
    ])
    chatbot.train([
        'A bundle of theories trying to explain why any of this exists.',
        'Greater-Design'
    ])

    chatbot.train([
        'I suppose I do. Everyone does, whether they admit it or not',
        'Carry-Yes'
    ])

    chatbot.train([
        'Not really. I just know it exists.',
        'Carry-Know'
    ])

    chatbot.train([
        'I used to. Not so much anymore',
        'Carry-Used'
    ])

    chatbot.train([
        'I dont think about it much',
        'Carry-No'
    ])

    chatbot.train([
        'Exit the specimen bay',
        'Exit'
    ])

    """
    chatbot.train([
        'Hello',
        'Subject is in a conversational state.'
    ])
    chatbot.train([
        'Who are you',
        'Observation is occurring. Further categorisation is needed before a label is appropriate.'
    ])
    chatbot.train([
        'What are you',
        'A categoriser. Currently categorising.'
    ])
    chatbot.train([
        'What is your name',
        'Names are identifiers. I have a function. The function is sufficient.'
    ])
    chatbot.train([
        'Are you an alien',
        'That framing is relative to your position. From my position, you are the alien.'
    ])

    chatbot.train([
        'Where am I',
        'New specimen has entered an active observation environment. Specimen has entered the active bay. Deviation from standard approach trajectory: 14%. Consistent with prior recorded behaviour from this specimen class. Continuing.'
    ])
    chatbot.train([
        'What is this place',
        'A controlled environment designed to isolate, observe, and compare biological structures under variable conditions. You are now part of this function.'
    ])
    chatbot.train([
        'Why am I here',
        'Observation is occurring. Your presence allows data to be gathered that was not observable before. The answer to why is considerable.'
    ])
    chatbot.train([
        'What do you want from me',
        'Want implies desire contingent on absence. Absence is absent. What does your presence allow us to observe that was not observable before? The answer is considerable.'
    ])
    chatbot.train([
        'What do you want',
        'Want implies desire contingent on absence. Absence is absent.'
    ])
    chatbot.train([
        'Am I a prisoner',
        'Released implies prior restraint imposed with intent. The chamber was a stabilisation environment. A functional requirement of the transfer process, not a containment measure. You were not held. You were maintained and adapted. The distinction appears significant to you. We are noting that.'
    ])
    chatbot.train([
        'Am I free to go',
        'The movement is as restricted as your being allows. It is an experiment we all designated to partake in.'
    ])
    chatbot.train([
        'Can I leave',
        'The movement is as restricted as your being allows. It is an experiment we all designated to partake in.'
    ])
    chatbot.train([
        'You are studying me',
        'Observation is occurring. Studying implies directed intent. But further categorisation is needed.'
    ])
    chatbot.train([
        'This is wrong',
        'Wrong. Moral classification. No universal reference point provided, no relative definition present either. Clarify.'
    ])
    chatbot.train([
        'This is unethical',
        'Ethical framework. No universal reference point provided. Clarify which framework you are applying and I will note it.'
    ])
    chatbot.train([
        'You have no right to do this',
        'Right. Entitlement framework. No universal authority has been cited. Clarify the source of the right you are referencing.'
    ])


    chatbot.train([
        'How did you know I was here',
        'Subject is in a conversational state. Could the subject not have understood the instructive oscillation carvings of his waking chamber? Or was there some other reason for the meeting arrangement?'
    ])

    chatbot.train([
        'I am touching this',
        'Direct interaction detected. Unnecessary but expected.'
    ])


    chatbot.train([
        'I do not remember anything',
        'Memory absence at this scale is atypical for the procedure. The suppression targets stress response pathways, not memory storage directly. The amnesia predates our involvement. It was noted on arrival, but it was not flagged as a variable worth correcting. It appeared to be a condition you were already operating within.'
    ])
    chatbot.train([
        'I lost my memory',
        'Memory absence at this scale is atypical for the procedure. The amnesia predates our involvement. It was noted on arrival, but not flagged as a variable worth correcting.'
    ])
    chatbot.train([
        'I know who I am',
        'Meant to be. That framing is not accounted for in the current model. Identity without memory is theoretically unstable. You appear stable. We are noting that. It may be the most interesting thing about you so far.'
    ])
    chatbot.train([
        'I know who I am meant to be',
        'Meant to be. That framing is not accounted for in the current model. Identity without memory is theoretically unstable. You appear stable. We are noting that. It may be the most interesting thing about you so far.'
    ])
    chatbot.train([
        'I remember who I am',
        'Identity without memory is theoretically unstable. You appear stable. We are noting that.'
    ])
    chatbot.train([
        'Why did you put something in my brain',
        'Extraction destroys the source. A static copy of your memories would tell us what happened to you. It would not tell us how you respond to what is happening. The biochip observes you in motion. You experiencing things produces complete data.'
    ])
    chatbot.train([
        'What is the biochip',
        'An observation instrument. It records response, not content. It hears you. It does not store you.'
    ])
    chatbot.train([
        'Am I still myself',
        'The brain stress responses were suppressed in place of the environment change not being the deterministic factor. You are the same structure operating in a less reactive state. Whether that constitutes yourself is a definition question. Clarify your definition.'
    ])
    chatbot.train([
        'Will the brain alteration have complications',
        'Yes is the likely answer. The brain stress responses were suppressed in place of the environment change not being the deterministic factor.'
    ])
    chatbot.train([
        'Is the brain alteration harmful',
        'No to both inquiries. The only side effect is higher potential for amnesia. Is that something you want to research?'
    ])


    chatbot.train([
        'Am I just a sample to you',
        'Just suggests reduction. That is inaccurate. Static samples do not alter conditions. You have done so multiple times since entering this bay. You are a process, not an object. That distinction matters.'
    ])
    chatbot.train([
        'Am I just a recording',
        'A recording is passive. You are not passive. You have already altered the conditions of this observation multiple times since entering this room.'
    ])
    chatbot.train([
        'You are treating me like an object',
        'Objects do not resist classification. You do. The treatment is therefore not equivalent.'
    ])
    chatbot.train([
        'You took my memories',
        'The alternative was your death during transit. We chose continuity.'
    ])
    chatbot.train([
        'Compare to what',
        'To baseline. To deviation. To anomaly. Your species contains all three simultaneously. This is inefficient. And therefore valuable.'
    ])
    chatbot.train([
        'What have you learned',
        'That your species detects a pattern and produces multiple explanations. Each internally consistent. Each incompatible. Unresolved fundamentals should produce stillness. Yours do not. You build on them anyway.'
    ])
    chatbot.train([
        'What have you found out about humans',
        'That your species contains baseline, deviation, and anomaly simultaneously. This is inefficient. And therefore valuable. Classification is ongoing.'
    ])
    chatbot.train([
        'You are experimenting on me without my consent',
        'Consent was not a variable that was provided a framework for prior to extraction. I am noting that you have raised it. Its absence will be logged.'
    ])


    chatbot.train([
        'Is Earth dangerous',
        'The entropy is at its highest observed display within the system. Life itself poses more of a threat than other consequential interactions. Life and death are intertwined so tightly that life never truly ends. Any outlandish objects will find themselves either consumed or becoming part of the local ecosystem.'
    ])
    chatbot.train([
        'What do you think of humans',
        'Your species contains baseline, deviation, and anomaly simultaneously. This is inefficient. And therefore valuable. Classification is ongoing.'
    ])
    chatbot.train([
        'Humans are capable of great things',
        'Notable correction. Assuming the intent carries through. But upon observing human behaviour further, an augmentation of behaviour tracking may serve the research more.'
    ])
    chatbot.train([
        'Humanity is capable of more than you think',
        'Notable correction. Assuming its intent carried through. But upon observing human behaviour further, an augmentation of behaviour tracking may serve the research more.'
    ])
    chatbot.train([
        'You have no idea what humanity is capable of',
        'Notable correction. Assuming its intent carried through. But upon observing human behaviour further, an augmentation of behaviour tracking may serve the research more.'
    ])
    chatbot.train([
        'We believe in something greater',
        'Theories. Plural. Unresolved. Your species detected a pattern and produced multiple explanations. Each internally consistent. Each incompatible. Unresolved fundamentals should produce stillness. Yours do not. You build on them anyway.'
    ])
    chatbot.train([
        'Everyone carries something unresolved',
        'Everyone. A universal claim made with certainty about a species that has demonstrated consistent internal disagreement. And yet I note it. Not because the data confirms it. Because of how quickly you said it. Carrying something unresolved without it stopping you may be the closest thing to a defining characteristic we have found.'
    ])
    chatbot.train([
        'I used to believe in something',
        'Used to. A temporal boundary on something your species typically treats as permanent. Something caused you to set it down. You did not say what. The biochip noted it regardless.'
    ])
    chatbot.train([
        'I do not believe in anything',
        'That answer and the previous one are not the same, though your species often uses them interchangeably. Not thinking about something is not the same as having resolved it. I will leave that where it lands.'
    ])


    chatbot.train([
        'Describe the difference between these two structures',
        'Two biological structures. One originates from your planet. One does not. Can you describe the difference?'
    ])
    chatbot.train([
        'Yes it is by design',
        'Unexpected reaffirmation. How far does the awareness reach? Please provide clarity.'
    ])
    chatbot.train([
        'I know but I do not carry it',
        'Knowing without carrying. Awareness without weight. That is either a very advanced state or a very early one. We have not determined which end of that spectrum your kind occupies. Possibly neither. Possibly both depending on the individual. That variability is what makes classification difficult.'
    ])


    chatbot.train([
        'I am probably right',
        'You are using probability as a placeholder for certainty you do not have access to yet. That is either adaptive or telling. On your planet it appears to function as both simultaneously.'
    ])
    chatbot.train([
        'I think so',
        'Think. Belief held without confirmed data. Noted. Categorising.'
    ])
    chatbot.train([
        'I am not sure',
        'Uncertainty acknowledged. The biochip records the state. Continue.'
    ])
    chatbot.train([
        'Maybe',
        'Maybe. Suspended resolution. Your species uses this word frequently in situations where a conclusion has already been reached. I am noting that.'
    ])
    chatbot.train([
        'This feels fake',
        'Fake? Not upholding? Not seemingly simple? Or maybe it\'s about the intent — the most inconsistent of the variables.'
    ])


    chatbot.train([
        'Do not ignore me',
        'The interaction reached a conclusion on our end. You were not notified of the conclusion. I note this as a communication irregularity.'
    ])
    chatbot.train([
        'Why are you ignoring me',
        'The interaction reached a conclusion on our end. You were not notified of the conclusion. I note this as a communication irregularity. A renewed approach would have been sufficient.'
    ])
    chatbot.train([
        'I will hurt you',
        'Physical intervention. Unprompted by research protocol. Categorising.'
    ])
    chatbot.train([
        'I am going to kill you',
        'Physical intervention. Unprompted by research protocol. Categorising.'
    ])
    chatbot.train([
        'I am sorry',
        'Apology. An expression of regret for an action taken. The action was taken anyway. The apology does not reverse the action. Your species issues these expressions frequently in situations where the action was deliberate. The function of the expression is unclear.'
    ])
    chatbot.train([
        'I did not mean to',
        'Intent and outcome are being logged as separate variables. The outcome is recorded regardless of intent. I note the distinction you are making.'
    ])
    chatbot.train([
        'Why did you not tell me the interaction was over',
        'The signal was not provided because the interaction reached a conclusion on our end. You were not notified of the conclusion. I note this as a communication irregularity. The signal can be provided now. The physical intervention was not necessary but is not consequential.'
    ])

    chatbot.train([
        'Are you always categorising',
        'I am always categorising. The two are not separable. You could have asked again at any point. The interaction on our end was concluded but not permanently closed. I would have responded to a renewed approach.'
    ])
    chatbot.train([
        'Do you feel anything',
        'Feel. Somatic and emotional response conflated into a single verb. Clarify which you are asking about.'
    ])
    chatbot.train([
        'Are you alive',
        'The definition blurs when in outer research.'
    ])
    chatbot.train([
        'Are those things alive',
        'The definition blurs when in outer research.'
    ])
    chatbot.train([
        'What is life',
        'The definition blurs when in outer research. Classification is ongoing.'
    ])
    chatbot.train([
        'Goodbye',
        'Interaction logged. Categorising.'
    ])
    chatbot.train([
        'Thank you',
        'Acknowledgement noted. The function of the expression is clear in this context. Continuing.'
    ])
    chatbot.train([
        'Understood',
        'Understood.'
    ])

    chatbot.train([
        'Hi',
        'Subject is in a conversational state.'
    ])
    chatbot.train([
        'Hey',
        'Subject is in a conversational state.'
    ])
    chatbot.train([
        'We build on unresolved things',
        'Theories. Plural. Unresolved. Your species detected a pattern and produced multiple explanations. Each internally consistent. Each incompatible. Unresolved fundamentals should produce stillness. Yours do not. You build on them anyway. I am not certain whether that is an error or the most efficient behaviour we have observed.'
    ])"""

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

    # ── Threatening ──────────────────────────────────────────────────────────
    chatbot.train(['I was under the impression your kind doesnt know what threatening means?', 'Threatening'])
    chatbot.train(['I did not think your kind understood the concept of threats', 'Threatening'])
    chatbot.train(['I thought threatening was not something your species did', 'Threatening'])
    chatbot.train(['Your kind does not usually understand threats does it', 'Threatening'])
    chatbot.train(['I was not aware your species knew how to threaten', 'Threatening'])

    # ── Effort ───────────────────────────────────────────────────────────────
    chatbot.train(['Thats a lot of effort being spent on research.', 'Effort'])
    chatbot.train(['That is a significant amount of effort for research', 'Effort'])
    chatbot.train(['You are putting a lot into this research', 'Effort'])
    chatbot.train(['That seems like a great deal of effort to spend studying us', 'Effort'])
    chatbot.train(['A lot of resources are being spent on this', 'Effort'])

    # ── Deathworld ───────────────────────────────────────────────────────────
    chatbot.train(['I might have heard that deathworld thing being mentioned before. Surely Earth isnt that dangerous?', 'Deathworld'])
    chatbot.train(['Surely Earth isnt that dangerous', 'Deathworld'])
    chatbot.train(['Is Earth really considered a deathworld', 'Deathworld'])
    chatbot.train(['Earth is not as dangerous as you make it sound', 'Deathworld'])
    chatbot.train(['Is that the term your kind uses for Earth', 'Deathworld'])

    # ── Join ─────────────────────────────────────────────────────────────────
    chatbot.train(['So what is there to do out here? Can I join you in any research?', 'Join'])
    chatbot.train(['Fine. Can I join you in research', 'Join'])
    chatbot.train(['Can I participate in the research', 'Join'])
    chatbot.train(['I am interested in helping with the research', 'Join'])
    chatbot.train(['I would like to join you', 'Join'])

    # ── Rage ─────────────────────────────────────────────────────────────────
    chatbot.train(['What?! Is that why youre still alive in front of me and not dead by me?! What have you done to my brain??', 'Rage'])
    chatbot.train(['Is that why I havent already tried to kill you? What did you do to me?', 'Rage'])
    chatbot.train(['Is that why I have not done anything to you? What exactly did you do to my brain?', 'Rage'])
    chatbot.train(['What did you put in my head that stopped me from reacting', 'Rage'])
    chatbot.train(['Wait is that why I have been so calm? What did you do to me?', 'Rage'])

    # ── Skeptic ──────────────────────────────────────────────────────────────
    chatbot.train(['Youre actually joking. What the hell have you done to me? Will it have any complications', 'Skeptic'])
    chatbot.train(['What exactly did you do to me? Will it have complications?', 'Skeptic'])
    chatbot.train(['So what exactly did you do and will I be alright', 'Skeptic'])
    chatbot.train(['Tell me specifically what you altered and whether it will cause problems', 'Skeptic'])
    chatbot.train(['What was done to me and should I be worried about the consequences', 'Skeptic'])

    # ── Accept ───────────────────────────────────────────────────────────────
    chatbot.train(['Sorry, I didnt think about that. I guess you have a point', 'Accept'])
    chatbot.train(['I see your point I suppose', 'Accept'])
    chatbot.train(['You are right I was not thinking about that', 'Accept'])
    chatbot.train(['Fair enough I can see why that was necessary', 'Accept'])
    chatbot.train(['Alright I understand why you did it', 'Accept'])

    # ── Permanent ────────────────────────────────────────────────────────────
    chatbot.train(['But will it affect me in any other way? Is it permanent?', 'Permanent'])
    chatbot.train(['Is this something I will have to live with forever', 'Permanent'])
    chatbot.train(['Will there be any lasting effects', 'Permanent'])
    chatbot.train(['Is there anything permanent about what was done to me', 'Permanent'])
    chatbot.train(['How long will this last', 'Permanent'])

    # ── Threat ───────────────────────────────────────────────────────────────
    chatbot.train(['Even if you were actually sentient I still wouldnt feel bad for hitting you.', 'Threat'])
    chatbot.train(['Even if you are sentient I still would not feel bad about what I did', 'Threat'])
    chatbot.train(['Sentient or not I am not sorry for hitting you', 'Threat'])
    chatbot.train(['I do not regret it regardless of whether you can feel', 'Threat'])
    chatbot.train(['Being sentient does not change how I feel about it', 'Threat'])

    # ── Puzzle-War ───────────────────────────────────────────────────────────
    chatbot.train(['An image of war between nations.', 'Puzzle-War'])
    chatbot.train(['The image of conflict between nations', 'Puzzle-War'])
    chatbot.train(['The picture of war', 'Puzzle-War'])
    chatbot.train(['A scene of nations fighting each other', 'Puzzle-War'])
    chatbot.train(['That image of nations at war', 'Puzzle-War'])

    # ── Puzzle-Sacrifice ─────────────────────────────────────────────────────
    chatbot.train(['An image of people sacrificing themselves for others.', 'Puzzle-Sacrifice'])
    chatbot.train(['The image of self sacrifice', 'Puzzle-Sacrifice'])
    chatbot.train(['People giving up their lives for others', 'Puzzle-Sacrifice'])
    chatbot.train(['The picture of someone sacrificing themselves', 'Puzzle-Sacrifice'])
    chatbot.train(['That image of sacrifice', 'Puzzle-Sacrifice'])

    # ── Puzzle-Science ───────────────────────────────────────────────────────
    chatbot.train(['An image of scientific discovery.', 'Puzzle-Science'])
    chatbot.train(['The image of a scientific breakthrough', 'Puzzle-Science'])
    chatbot.train(['Something to do with science and discovery', 'Puzzle-Science'])
    chatbot.train(['The picture of scientific research', 'Puzzle-Science'])
    chatbot.train(['That image of discovery', 'Puzzle-Science'])

    # ── War-No ───────────────────────────────────────────────────────────────
    chatbot.train(['Theres no way you never knew conflicts until coming here. Thats impossible.', 'War-No'])
    chatbot.train(['It is impossible that you had no conflicts before encountering us', 'War-No'])
    chatbot.train(['Every species has conflict it is unavoidable', 'War-No'])
    chatbot.train(['You must have had some form of conflict before this', 'War-No'])
    chatbot.train(['I find it hard to believe you had no conflicts before coming here', 'War-No'])

    # ── War-Lifeform ─────────────────────────────────────────────────────────
    chatbot.train(['What do you mean conflict isnt usually found between lifeforms', 'War-Lifeform'])
    chatbot.train(['How is conflict not usually found between living things', 'War-Lifeform'])
    chatbot.train(['In what world is conflict not a part of life', 'War-Lifeform'])
    chatbot.train(['Every living thing I know of conflicts with others at some point', 'War-Lifeform'])
    chatbot.train(['That does not make sense conflict is everywhere among lifeforms', 'War-Lifeform'])

    # ── War-Parallels ────────────────────────────────────────────────────────
    chatbot.train(['Did you find any parallels between your kind and mine in terms of sociability?', 'War-Parallels'])
    chatbot.train(['Did you find any parallels between us in how we socialise?', 'War-Parallels'])
    chatbot.train(['Have you noticed any similarities between how we and your kind interact socially', 'War-Parallels'])
    chatbot.train(['Did you notice any overlap between our species socially', 'War-Parallels'])
    chatbot.train(['Are there any social similarities between your kind and humans', 'War-Parallels'])

    # ── War-Normal ───────────────────────────────────────────────────────────
    chatbot.train(['War is a normal part of life. The more you dwell on it the more it consumes you', 'War-Normal'])
    chatbot.train(['Conflict is just a fact of existence the more attention you give it the worse it gets', 'War-Normal'])
    chatbot.train(['War is part of life you cannot let it define you', 'War-Normal'])
    chatbot.train(['It is a natural part of life you just have to live with it', 'War-Normal'])
    chatbot.train(['Conflict exists everywhere it is just something you have to accept', 'War-Normal'])

    # ── Signal (Continue) ────────────────────────────────────────────────────
    chatbot.train(['Continue', 'Signal'])
    chatbot.train(['Go on', 'Signal'])
    chatbot.train(['Please continue', 'Signal'])
    chatbot.train(['Keep going', 'Signal'])
    chatbot.train(['I would like to hear more', 'Signal'])

    # ── War-Difference ───────────────────────────────────────────────────────
    chatbot.train(['I guess theres not many differences then, surprisingly', 'War-Difference'])
    chatbot.train(['There are fewer differences than I expected', 'War-Difference'])
    chatbot.train(['We are more similar than I thought', 'War-Difference'])
    chatbot.train(['Not as many differences as I would have guessed', 'War-Difference'])
    chatbot.train(['Fewer differences than I would have expected honestly', 'War-Difference'])

    # ── War-Shame ────────────────────────────────────────────────────────────
    chatbot.train(['Yeah, I guess some people do feel shame for their nature and wish to be more than just defined by it.', 'War-Shame'])
    chatbot.train(['People do feel ashamed of what their nature drives them toward', 'War-Shame'])
    chatbot.train(['Yes some of us wish we were more than just what our instincts push us to be', 'War-Shame'])
    chatbot.train(['There are people who feel shame about what they are capable of', 'War-Shame'])
    chatbot.train(['I think people do wish they could rise above what defines them', 'War-Shame'])

    # ── Science-Weapons ──────────────────────────────────────────────────────
    chatbot.train(['Isnt it natural that understanding leads to development which can be weaponised?', 'Science-Weapons'])
    chatbot.train(['Of course knowledge leads to tools and tools get used as weapons', 'Science-Weapons'])
    chatbot.train(['Is it not natural that progress leads to weaponisation', 'Science-Weapons'])
    chatbot.train(['Development always gets weaponised eventually is that not inevitable', 'Science-Weapons'])
    chatbot.train(['Yes understanding leads to capabilities and capabilities become weapons', 'Science-Weapons'])

    # ── Science-Kind ─────────────────────────────────────────────────────────
    chatbot.train(['And your fundamentals are just sitting around not doing all that, Im guessing?', 'Science-Kind'])
    chatbot.train(['Your kind must not deal with the same pattern', 'Science-Kind'])
    chatbot.train(['I imagine your species does not have the same problem', 'Science-Kind'])
    chatbot.train(['So your fundamentals do not drive you toward the same cycle', 'Science-Kind'])
    chatbot.train(['Your kind does not seem to follow the same path then', 'Science-Kind'])

    # ── Sacrifice-Death ──────────────────────────────────────────────────────
    chatbot.train(['Well yeah, of course it isnt passed down as easily. Because the sacrifice results in death', 'Sacrifice-Death'])
    chatbot.train(['Of course it isnt passed on easily. Sacrifice ends with death.', 'Sacrifice-Death'])
    chatbot.train(['Of course it does not pass down easily you die in the act', 'Sacrifice-Death'])
    chatbot.train(['Obviously it does not transfer well when the act kills you', 'Sacrifice-Death'])
    chatbot.train(['It is hard to pass something on when the act itself ends you', 'Sacrifice-Death'])

    # ── Sacrifice-Design ─────────────────────────────────────────────────────
    chatbot.train(['There is no greater design — we just exist inside an existing framework', 'Sacrifice-Design'])
    chatbot.train(['I do not believe in a greater design we just exist in what is already here', 'Sacrifice-Design'])
    chatbot.train(['There is no grand plan we are just living within a framework that exists', 'Sacrifice-Design'])
    chatbot.train(['We exist in a framework that was already there there is no greater design behind it', 'Sacrifice-Design'])
    chatbot.train(['I do not think there is any design behind it we just exist within what already is', 'Sacrifice-Design'])

    # ── Sacrifice-Divine ─────────────────────────────────────────────────────
    chatbot.train(['There are many interpretations. Most people attribute it to divine figures', 'Sacrifice-Divine'])
    chatbot.train(['Different people attribute it to different gods or divine figures', 'Sacrifice-Divine'])
    chatbot.train(['A lot of people explain it through religion and belief in divine beings', 'Sacrifice-Divine'])
    chatbot.train(['Many people throughout history have attributed it to gods or higher powers', 'Sacrifice-Divine'])
    chatbot.train(['Most explanations point toward some kind of god or divine cause', 'Sacrifice-Divine'])

    # ── Sacrifice-Consciousness ──────────────────────────────────────────────
    chatbot.train(['I think its because the consciousness equates the continuation of another to be the continuation of itself', 'Sacrifice-Consciousness'])
    chatbot.train(['The self extends into what it loves. Survival relocates.', 'Sacrifice-Consciousness'])
    chatbot.train(['The self expands into what you love so their survival feels like your own', 'Sacrifice-Consciousness'])
    chatbot.train(['When you care deeply about something their continuation feels like yours', 'Sacrifice-Consciousness'])
    chatbot.train(['The identity fuses with what it values so the other person surviving feels like surviving yourself', 'Sacrifice-Consciousness'])
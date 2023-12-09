# Season 0 Scene 1: Waking Up
label s0s1:
    # play audio cicada volume 0.5
    scene bg spotlight with dissolve
    centered "Everyone is born a star."
    
    centered "Some twinkle brighter than others, but all are stars in their own right."
    show bg star river 1 with dissolve
    "Eight billion stars populate this beautiful planet we call home, and infinitely many more spread across the cosmos and paint our night sky."

    "Every speck of light, no matter how tiny, flows downstream in the direction that our universe, Fate, intended."

    "And then..."
    
    scene bg star river 2 with dissolve
    "There's me."
    
    show bg star river 3
    "Adrift in this sea of stars."
    
    show bg star river 4
    "Stranded, without a direction to call my own."

    show bg star river 5 with Dissolve(1.5)

    "Before I knew it, it was August. A whole four months have gone by since my graduation."

    "Just the other day, I tallied my nineteenth lap around the Sun."

    "A full nineteen years of… me."

    "In that time, I've watched my childhood come and go. They were the happiest years of my life."

    "For me, adulthood is just beginning. By now, my direction should be clear. My path should be paved for me."

    "And yet, when I opened the gates to the great beyond, there was no big opportunity waiting for me. Job offers and higher education didn't greet me out the front door like they did for others."

    "Instead, I'm stuck floating in place, with nothing but the threat of eventual death motivating my next steps."

    "... That's a bit grim, isn't it? When I look at it that way, I can't help but get a little worried."

    "They say one's future is determined by their environment – that all liquids take the shape of their containers."

    "Some people grow up knowing exactly what they want to do with their lives. Some inherit a family business, others have everything from their college to their retirement planned out."

    "But, growing up, I didn't have a set path."
    
    "Mom made sure that I would always have a choice. She'd never force me to do anything I didn't want to."
    
    "I'm forever grateful for that, and yet…"
    
    window hide
    scene black with dissolve

    centered "I'm lost."

    centered "…"

    scene bg spotlight with Dissolve(1)

    centered "Seika..."

    scene black with dissolve
    centered "My name."

    scene bg spotlight with Dissolve(1)

    centered "Seika."

    scene black with dissolve

    centered "\"Star song\". My mom's first gift to me."

    centered "To me, my name holds a lot of significance."

    centered "From the moment I was born, I've always wanted to live up to–"
    
    scene bg spotlight
    centered "{size=*1.5}Seika!{/size}"
    window auto
    
    scene bg cafe
    show natsuha pout at center
    show seika shock at r
    with vpunch
    play music unplanned_rendezvous
    define n_name = "Fashionable Girl"
    s "Wah!"
    "I see my friend, who's nearly climbed over the table, her face just under a foot away from mine."
    "She looks at me with a furrowed brow, examining my face like a worried but curious puppy."
    
    show natsuha pout at l 
    with move
    n "Geez Seika, you're always spacin' out when I'm telling a story."
    n "Am I really that boring?"
    s sad "Eh? S-Sorry... I just have a few things on my mind, honest!"
    n happy "Ehehe, just messin' with ya."
    n neutral "Anyways, like I was saying, the old dude started yellin' at me! Said I took too long and that his beef bowl got cold. I was only, like, five minutes late!"
    show seika neutral
    "This is Natsuha. She's been my friend since middle school, and we've been joined at the hip ever since." 
    "For almost as long as I've known her, she's been working all the most random part-time jobs I've never heard of."
    "Magic show performer, karaoke drink bar attendant, tuna market auctioneer, festival pyrotechnician – where did she even get the license for that!?"
    "Anyway, it sounds like she got a new job as a fast food delivery girl since we last met… just after graduation."
    "After we got out of high school, she's only gotten more and more busy with everything. You really can't help but admire her go-getter attitude."
    $ n_name = "Natsuha"
    n happy "There was also this cute top I saw at the mall the other day! I gotta go back and see if it's still...{w} there."
    n neutral "Earth to Seika? You're doing that spacin' out thing again."
    s shock "Ah, sorry! Bad habit."
    s neutral "So we're going to the mall after lunch then?"
    n happy "Yes!"
    n neutral "Wait, no."
    n happy "You're not worming your way out of this one, Seika! You've got something on your mind and I wanna hear it."
    n shock "Ahh, could it be..."
    n happy "... you're in LUV?"
    s shock "What!? No!"
    n pout "Ah, booo."
    n neutral "Like seriously though, what's up?"
    s sad "I guess I feel a little lost right now? All of our school friends are either at university or working."
    s "You're doing, what, three jobs now? Seeing you, I feel like I should be doing more."
    n neutral "Yah, but all that's my thing. I know I make it sound fun, but you don't hafta do my thing."
    n "Why don't you find your own thing? Something you wanna do, y'know?"
    s sad "But, I don't know, I just feel like I wasted the time in between graduation and now."
    n happy "Aww, Seika, don't say that! No such thing as wasted time, dummy." 
    n neutral "Ooh, what about your med school exam? You told me you were gonna take it right before graduation. How'd ya do?"
    s "..."
    n concern "... Seika?"
    s sad "I was a few marks short..."
    n shock "That close?! C'mon, you're trying again next year, right?"
    s neutral "Yeah, I will, but I also want to be open to other opportunities."
    n neutral "Didn't you say you wanted to help people on your career aspirations survey?"
    n happy "Hehe, you got super embarrassed when I called you a big ol\' sweetheart!"
    s shock "H-hey! Don't bring that up now! How do you even remember that?"
    n neutral "Cause it's like, my job to remember stuff like that. Your birthday, your favorite foods, heck, even your shoe size."
    n happy "And, unlike you, I don\'t have the memory of a hamster."
    s happy "You're so mean!"
    "It's kind of hazy, but I do remember putting down all sorts of careers that involve helping people."
    "Like... being a doctor, or social worker, or teacher."
    "That's right, helping people is how I wanted to make a mark on the world."
    s neutral "Besides, I'm volunteering at the hospital. Maybe I'll find that spark again, you know?"
    s "Or... or maybe I'll discover a new path to take."
    n happy "I'm sure you'll find something! You love dreaming big, something'll have to stick."
    s "Yeah, and maybe I don't need to stick to medicine either. If I want to stick to my dream of helping people, I need to keep my mind open to whatever life throws at me."
    s "Say, you're always hunting for jobs, Natsuha. Do you know of any work that I can do?"
    n neutral "'Course, there's always a bunch! I'll send some of 'em to you if you want?"
    s happy "That'll help, thanks!"
    s neutral "And sorry, all we've talked about is me. What about you, Natsuha? Do you have any big dreams?"
    n "Me? Nah, not really."
    s "But Natsuha, you're one of the coolest people I know! You're talented and fashionable and hardworking!"
    s "With your looks and fashion sense you could be a model or a fashion designer! Doesn't that sound cool?"
    n concern "Mmm, it kinda does."
    s happy "Imagine that, Natsuha! I can already see you on the cover of a flashy, trendy magazine."
    n "It sounds pretty cool and all, but don't you go worrying about me, Seika."
    n happy "You just focus on yourself and what you wanna do, and I'll be supporting you. Hundred-ten percent!"
    s neutral "Yeah, sorry again for rambling. Chatting with you gave me all these ideas and…{w} I feel a little hopeful about things again."
    n "Chill, you're gonna make me blush!"
    n neutral "Tell you what, after lunch I figured we could go to a new crepe place that opened up. My treat!"
    s sad "Crepes!? But aren't those kinda expensive..."
    n "Ah don't worry about it, I gots me a little bit of spending money from working overtime this summer."
    n happy "Plus, we don't see each other often, so I don't mind splurging a bit!"
    s happy "Alright, I won't say no to free sweets!"
    stop music fadeout 2.0
    scene bg spotlight with dissolve
    show text "{b}Season 0{/b}: Summer Dreaming"
    with dissolve
    $ renpy.pause()
    scene black with dissolve
    scene bg shop district with dissolve
    play music starbound
    # play audio cicada volume 0.2
    "After we paid for our respective drinks, we went to the crepe shop and decided to share one together."
    "Afterwards, Natsuha suggested we walk off the calories and explore the city, taking me to the shopping district to do some window shopping."
    "As the two of us walk down the street, Natsuha occasionally pointed and directed me to a shop window to look at pretty dresses."
    show natsuha neutral at r 
    show seika neutral at l
    with moveinright
    n "Maaaan, that one's cute!"
    n concern "But geez, look at that price tag. Maybe someda–"
    show natsuha at center
    with move
    with hpunch
    show seika shock
    n shock "Hey!"
    s "You okay, Natsuha?"
    show natsuha at r
    with move
    n pout "I'm fine, but people are so rude! What are they in such a hurry for?"
    show seika sad at center
    with move
    n concern "... Uh, Seika?" 
    s "I'm gonna check it out!"
    hide seika with moveoutright
    n shock "Seika? Hey, where are you goin'? Seika!"
    hide natsuha with moveoutright
    stop sound fadeout 1.0

    show black with moveinright
    with Pause(0.5)
    scene bg citycrossing
    show black
    hide black with moveoutleft
    "I turn the corner and accidentally bump into the back of a stranger."
    "I apologize, but they seem to be too fixated elsewhere to notice."
    "Taking a deep breath, I swim my way through the sea of people to see what they're all looking at."
    return
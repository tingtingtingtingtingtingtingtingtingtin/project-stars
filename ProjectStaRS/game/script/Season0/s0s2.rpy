# Season 0 Scene 2

label s0s2:
    scene bg citycenter with fade
    stop music fadeout 2.0
    play audio crowd
    n "Seika!"
    "I think I hear my name, but it sounds so distant I'm not sure if I'm imagining it or not."
    "All that matters is getting closer."
    s "Woah... is that a stage?"
    "It looks like one, at least, at the top of a set of stairs."
    "Most people keep walking, but that doesn't mean I'm the only one gathering around the steps." 
    show m with dissolve
    "On stage, the white-haired girl goes about setting up equipment I can't even put a name to with a strangely flat expression on her face."
    s "She looks so cool...!"
    "The girl steps to the center of the stage and taps her mic."
    "Everything seems to be in order because she nods to herself and puts both hands around it."
    
    $ m_name = "White-haired Girl"
    m "Ahem."
    "I hear a deep breath, and then..."
    window hide
    show m_performance with dissolve
    $ renpy.pause(0.5)
    window show
    "She sings."
    "The ambient chatter of the city around me melts away, drowned out by the sound of her voice." 
    "There's a crowd around me, but at that moment, she and I are the only people in the world."
    "My hand clenches over my chest, unbidden.{w} It's like I've suddenly forgotten how to breathe."
    "She twirls and glides across the stage gracefully, her white hair fluttering behind her like powder snow."
    "She doesn't miss a step. She doesn't miss a note."
    "She's incredible. She's beautiful. And yet..."
    "Even as she sings her heart out, her eyes are like shards of ice, without even a spark of joy in them."
    "The last notes of her song seem to hang in the air as she points to the sky one last time and comes to a stop."
    "She holds her final pose, and for a moment, time has frozen."
    window hide
    hide m_performance with dissolve
    window show
    "The illusion is broken when she moves again, and the world comes back into existence, the rush of chatter and life washing over me."
    "The late summer heat thaws me from my stupor. When I look around, the crowd around me has dispersed."
    s "!?"
    "People would just {i}leave{/i} after a performance that incredible? How could they?"
    "I find myself outraged on the girl's behalf."
    "I don't like being angry, but something about her singing has moved... {i}something{/i} in me. Something I didn't know existed."

    m "Dammit...!"
    "When I turn back to the stage, the girl is glaring at her feet, shoulders hunched."
    "I didn't think of her as scary before, but when her face is scrunched up like that, I can't help but feel that way." 
    "But people can't choose their faces, and I would be frowning too if I performed like that and nobody cared."
    m "Huh?"
    "I clap, and I'm proud when I don't falter, even when she turns that glare on me."
    s "That was amazing!"
    m "Tch. I don't need your pity."
    s "Huh?! I would never…" 
    "Okay, I guess if I really didn't like something I wouldn't tell that to someone, but I really, really meant it that time!"
    "Doesn't she know how incredible she is?"
    show seika sad at left
    with moveinbottom
    s "It's... It's not pity! I really thought it was an amazing performance!"
    show m:
        xalign 0.7
    with move
    m "?!"
    m "What the hell are you doing up here?"
    show seika sad at l
    with move
    show m at r
    with move
    m "H-hey, watch the equipment!"
    "I realize I've stepped on stage without thinking."
    s shock "Ah! I'm sorry!"
    m "Just go away! I don't need you messing my stuff up."
    s "Oh no! Did I actually–"
    m "No, but you might've! You clearly don't know what you're doing."
    s "Sorry! Sorry! I just wanted to say you did a super good job!"
    m "What are you, stupid? It was terrible, and you can stop trying to make me feel better about it."
    s sad "..."
    "The girl seems to practically throw some of her equipment into their bags as she packs."
    s "You should be proud of your performance."
    m "Why are you still {i}here{/i}?"
    s "Because I thought you were incredible!"
    m "I {i}get{/i} it already! You've done your nice thing of the day, now screw off!"
    s "Why won't you believe me?"
    m "Are you blind? Because nobody else is still around!"
    "I open my mouth to respond, but... I can't. She's right, I really am the only one who stayed to the end." 
    "Before I can find the right words, I hear rapid footsteps behind me."
    show natsuha with moveinleft
    show seika shock
    n pout "Hey! There's no reason for you to be that rude!"
    m "Who the hell are you?"
    n "That doesn't matter. You owe my friend an apology."
    m "Like hell I do. She can shove her pity where the sun doesn't shine."
    "The girl, having finished packing up her equipment, slings her bag over her shoulder and stalks off."
    hide m with moveoutright
    show natsuha at right
    with move
    n "If you keep throwing pity parties you need to stop being surprised when people show up to them!"
    s "N-Natsuha, it's okay, really…!"
    show natsuha at r
    with move
    "Natsuha shakes her head and sighs, touching a hand to her temple." 
    "I've never heard her raise her voice like that in a while. She's usually so gentle, but I know she's been busy with work the past few months."
    "She must be stressed."
    n concern "Sorry, Seika. Are you okay?"
    s sad "Huh? Me? Yeah, I'm fine. She didn't really say anything hurtful."
    n "..."
    s shock "Don't look at me like that! It's true! She's like… a big scary dog, but it didn't feel like she was saying all that to me, you know?"
    s sad "Like, sure, what she said made me sad, but it wasn't because my feelings were hurt."
    "I look down the sidewalk she's long since disappeared down."
    "I can't help but feel a trickle of the pity she accused me of, though it's for a different reason than she probably thought."
    n "Seika..."
    s neutral "Never mind that, though! Did you hear her performance? It was incredible, wasn't it?"
    n neutral "Yes, I suppose. That doesn't mean she can say all that to you and get away with it."
    s happy "I'm telling you, Natsuha, it's fine! Really, she was so dazzling…"
    show black with moveinright
    stop music fadeout 1.0
    "We head home together after that."
    "Natsuha and I fill the air with chatter all the way, but I can't remember a thing about what we talked about."
    "The girl's song plays on repeat in my head, her silhouette on those stairs burned into my eyes."
    # image bg citycrossing noon = im.MatrixColor("images/bg/citycrossing.png", im.matrix.tint(.85,.60,.50)*im.matrix.brightness(0.10))
    # image seika neutral noon = im.MatrixColor("images/seika/neutral.png", im.matrix.tint(.85,.60,.50)*im.matrix.brightness(0.10))
    # image natsuha neutral noon = im.MatrixColor("images/natsuha/neutral.png", im.matrix.tint(.85,.60,.50)*im.matrix.brightness(0.20))
    scene bg citycrossing
    show seika neutral at l
    show natsuha neutral at r
    show black
    hide black with moveoutleft
    play music starbound
    s "Hm? What's that?"
    n "What's what?"
    show flier with moveinbottom
    # flyer.png
    n concern "This is…"
    s "\"Horizon Productions\"..."
    s "\"Open auditions to be an idol\"?"
    s "Is that what that girl is?"
    "An... idol?"
    "My fingers tremble around the edges of the flyer."
    "Could I… Could I be like that too?"
    n concern "... Hey. Let's go home, Seika."
    show natsuha at center
    with move
    hide flier with moveoutbottom
    s shock "Um...!? What are you doing!?"
    show natsuha at r
    with move
    n neutral "I'm just tossing it. Someone's been littering these everywhere, and I'm fed up with seeing 'em."
    s "W-Wait! If you don't want it, can I have it instead?"
    n "Even though this one's crumpled up?"
    s "I can still read it!"
    n concern "Haha, I know you dream big, but I didn't think you'd dream this big! You know being an idol's real hard, right?"
    s sad "O-Oh..."
    n "Seika..."
    n "..."
    n happy "Well, I don't know much about it, haha! I've just heard rumors about it, really. It's rough in the industry, ya know?"
    s "That girl was so cool, Natsuha... I wanna be like her."
    n concern "Seika, did you {i}see{/i} the way she treated you?"
    n "If someone as sweet as you started cussin' at people in broad daylight, I wouldn't know what I'd do with myself."
    n "You just need to... be Seika."
    s shock "N-No! That's not what I meant."
    s sad "... Nacchan, what if being an idol is the most Seika thing ever?"
    n "Seika, are you sure? It's super tough work. Do you even have any musical experience?"
    s shock "... Ah."
    n happy "Chin up, Seika! Not everything's for everyone. If everyone could do everything it'd be pretty boring, right?"
    n "You just gotta keep tryin' new things and—"
    s happy "Then I'll learn it all!"
    n shock "Eh?"
    s neutral "You're so right! I have to try new things until they stick!"
    n "Uh, that's not..."
    s "I really, really want to try it, Nacchan! And you should too! With you at my side, I won't make too many dumb mistakes!"
    n concern "..."
    scene bg sky noon with dissolve
    n "....."
    n "Here, have it."
    "Natsuha uncrumples the flyer and hands it to me."
    s "Thank you so much! I'll keep it somewhere safe."
    "I hold the flyer tight to my chest, careful not to let it slip away."
    n "... You need to do a lot of research, okay? Something like this is really serious, and I don't want you getting hurt."
    n "Promise me you'll back out if you change your mind, got it?"
    s "Okay, okay! I promise!"
    "I said as much, but I already knew nothing could change my mind."
    "My heart was already set on being an idol, to shine brightly in my own right."
    return
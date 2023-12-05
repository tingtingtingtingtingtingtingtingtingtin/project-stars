# Season 0 Scene 2

label s0s2:
    scene bg stage with fade
    play music starbound2
    n "Seika!"
    "Something about the crowd draws me to where they're gathered."
    "I think I hear my name, but it sounds so distant I'm not sure if I'm imagining it or not."
    "All that matters is getting closer."
    s "Woah... is that a stage?"
    "It looks like one, at least, at the top of a set of stairs. I can't help but be pulled closer."
    "Most people keep walking, but that doesn't mean I'm the only one gathering around the steps." 
    show m with dissolve
    "On stage, the white-haired girl goes about setting up equipment I can't even put a name to with a strangely flat expression on her face."
    s "She looks so cool...!"
    "The steps to the center of the stage and taps her mic."
    "Everything seems to be in order because she nods to herself and puts both hands around it."
    
    $ m_name = "White-haired Girl"
    m "Ahem."
    "I hear a deep breath, and then..."
    window hide
    hide m with dissolve
    show m_performance with dissolve
    $ renpy.pause(0.5)
    window show
    "She sings."
    "The ambient chatter of the city around me melts away, drowned out by the sound of her voice." 
    "There's a crowd around me, but in that moment, it's like she and I are the only people in the world."
    s "It's beautiful..."
    "My hand clenches over my chest, unbidden.{w} It's like I've suddenly forgotten how to breathe, my heart beating to the rhythm of her song."
    "I've never been so blown away by a performance, but I can't help but notice the look on the girl's face."
    "Even as she sings her heart out, there isn't a single spark of joy in her eyes."
    window hide
    hide m_performance with dissolve
    window show
    "The song comes to an inevitable end. I stand there in a stupor and, when I finally shake it off, the crowd around me has dispersed."
    "I look around, stunned. {w}People would just {i}leave{/i} after a performance that incredible?"
    "I find myself outraged on the girl's behalf.{w} I don't like being angry, but something about her singing has moved... {i}something{/i} in me.{w}"
    "Something I didn't know existed."
    show m with dissolve

    m "Dammit...!"
    "When I turn back to the stage, the girl is glaring at her feet, shoulders hunched. I didn't think of her as scary before, but when her face is scrunched up like that, I can't help but feel that way." 
    "But people can't choose their faces, and I would be frowning too if I performed like that and nobody cared."
    m "Huh?"
    "I clap furiously, and I'm proud when I don't falter, even when she turns that glare on me."
    s "That was amazing!"
    m "Tch.{w} I don't need your pity."
    s "Huh?! I meant that! I would never…" 
    "Okay, I guess if I really didn't like something I wouldn't tell that to someone, but I really, really meant it that time!"
    "Doesn't she know how incredible her performance was? How incredible {i}she{/i} is?"
    menu:
        "Tell her how you really feel":
            pass
    s "It's... It's not pity! I really thought it was an amazing performance!"
    show seika sad at left
    with moveinbottom
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
    "I'm a little taken aback by her aggression."
    "I open my mouth to… I don't know, apologize again, maybe, because I've clearly upset her." 
    "... But before I can, I hear footsteps behind me, followed by a familiar voice."
    show natsuha with moveinleft
    n "Hey! There's no reason for you to be that rude!"
    m "Who the hell are you?"
    n "That doesn't matter. You owe my friend an apology."
    m "Like hell I do. She can shove her pity where the sun doesn't shine."
    "The girl, having finished packing up her equipment, slings her bag over her shoulder and stalks off."
    hide m with moveoutright
    show natsuha at right
    with move
    n "If you keep throwing pity parties you need to stop being surprised when people show up to them!"
    s "N-Natsuha, it's okay, really…!"
    "Natsuha shakes her head and sighs, touching a hand to her temple." 
    "I've never heard her raise her voice like that in a while. She's usually so gentle, but I know she's been busy with work the past few months."
    "She must be stressed."
    n "Sorry, Seika. Are you okay?"
    s "Huh? Me? Yeah, I'm fine. She didn't really say anything hurtful."
    n "..."
    s "Don't look at me like that! It's true! She's like… a big scary dog, but it didn't feel like she was saying all that to me, you know?"
    s "Like, sure, what she said made me sad, but it wasn't because my feelings were hurt."
    "I look down the sidewalk she's long since disappeared down."
    "I can't help but feel a trickle of the pity she accused me of, though it's for a different reason than she probably thought."
    n "Seika..."
    s "Never mind that, though! Did you hear her performance? It was incredible, wasn't it?"
    n "Yes, I suppose. That doesn't mean she can say all that to you and get away with it."
    s "I'm telling you, Natsuha, it's fine! Really, she was so dazzling…"
    scene black
    "We head home together after that.{w} The girl's song plays on repeat in my head, the visage of her on that stage burned into my eyes."
    s "Hm? What's that?"
    n "What's what?"
    show flier
    # flyer.png
    n "This is…"
    s "\"Open auditions to be an idol\"?"
    s "Is that what that girl is? {w}An idol...?"
    "My fingers tremble around the edges of the flyer.{w} Could I… Could I be like that too?"
    return
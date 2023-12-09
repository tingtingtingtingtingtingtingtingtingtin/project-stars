label s0s45:
    scene bg residential
    "The farther we move away from the building, the more intense the butterflies in my stomach feel."
    "A part of me wants to hear the results right now, but another wants the announcement to be delayed."
    "I look at Natsuha and want to say something to her, but she's walking at a faster pace than me."
    "She's probably nervous too. I should check on how she's doing–"
    
    show natsuha concern at center
    with dissolve
    n "Hey, you alright? That one lady really tried to tear into you…"
    s "Huh? A-Ah yeah! I'm just looking forward to hearing the results."
    s "What about you?"
    n neutral "I'm perfectly fine. Just wanted to make sure her words didn't get to ya."
    n happy "Like I said, you did great. If you didn't get it then they're clearly pickin' the wrong talent."
    s "... Yeah. Thanks Natsuha."
    n neutral "No problem."
    hide natsuha with dissolve
    
    scene bg shrine with Dissolve(2)
    "I notice we've stopped in front of the stony gates to the local shrine."

    s "Wait, Natsuha, how about we pray for our success? It's worth a shot, don't you think?"
    show natsuha happy at center
    n "Pray? Ah, I don't really believe in that kind of stuff. You go on ahead."
    s "You sure? What if it doesn't work without you?"
    n happy "Go on! It'll be fine."
    n neutral "Besides, I need a minute. I'll catch up with you as soon as I'm ready."
    s "Alright, then I'll pray for both of us!"
    n happy "Haha, 'ppreciate it. Have fun!"
    hide natsuha happy with dissolve

    "I walk past the gate and move further into the shrine."
    "Admiring the building, I can't help but notice how well kept the place is."
    "A gentle breeze flows by, and the boughs of the maple trees sway back and forth."
    "Although it's only August, their leaves are already changing into that beautiful autumn orange."
    "It must have been years ago when I last visited with mom to watch fireworks during the spring festival."
    "I couldn't find Mom either, so the only thing I could do was kneel down and cry."
    "An old lady tapped my shoulder, and I told her I lost my mom."
    "Everyone came together to help me find her. They all stayed with me until Mom picked me up."
    "I end up at the foot of a stone staircase, where the donation box is."
    
    s "How do I do this again...?"
    "I dig a 100 yen coin from my bag and toss it in."
    "Ring the bell."
    "Clap. Clap."
    "For Natsuha and I… Our success."

    show akina neutral at right
    with moveinright
    define a_name = "Shrine Maiden"
    a "Ah, you forgot to bow..."
    show akina fear
    with vpunch
    s "Wah!"
    a "A-Ah!"

    show natsuha concern at l
    with moveinleft
    hide akina fear with moveoutright
    n "Is everything okay over here? I heard a scream. Are you hurt?"
    s "N-No, I'm alright, I uh..."
    "..."
    "Where'd she go?"
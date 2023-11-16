# Season 0 Scene 1: Waking Up

label s0s1:
    play music "cicada.mp3" volume 0.5
    unknown "..."
    scene bg cafe with fade
    unknown "Summer, just as I remember."
    unknown "The singing of the cicadas, the rustling of the trees, the bustling of the afternoon rush..."
    unknown "It's peaceful. I really missed moments like these."
    pause 0.2
    unknown "All these people passing by… Faces I'll never see again, voices I’ll never hear."
    unknown "I wonder what’s going on in their heads? Everyone has their dreams, aspirations, and names."
    unknown "Names… our keystones to identity. Names are always important! My name is…"

    pause 0.5
    $ name_choice = renpy.input("What is my name?")

    $ player_name = "Seika"
    if name_choice != "Seika":
        s "Perhaps that could’ve been my name in another life."

    s "Seika… “Song of stars”… the first gift from my parents."
    stop music fadeout 1.0
    scene bg crowd with fade

    # s is seika n is natsuha
    s "i want to be an idol"
    n "well dont!"

    s "some quick blurb about family"

    s "Mom wanted me to be the guiding star for others… But how do I do that?"

    scene bg school with fade

    s "Should I become a teacher? {w} No, going back to education is…"
    s "Maybe my volunteering at the hospital is the path I could keep going. I could become a nurse! {w} No, even if I'm appreciated there, it's not really what I want to do with my life…"

    scene bg cafe with fade

    s "What am I doing with myself..."

    show natsuha at right with moveinbottom 
        
    play music "cafe.mp3"
    
    n "Seika! Earth to Seika! Have you even been listening?"

    show haruka happy at left with moveinbottom
    s "Wha- what!? Of course, I have… I just uh-"

    n "Oh really~? What was the last thing I was talking about, huh?"

    s "Uhhh… How absolutely amazing of a friend you are, and all of the fun we have together!"

    n "Hehe. Close enough, Seika~"
    return
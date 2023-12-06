image logo = "gui/gamespawn.png"

label splashscreen:
    play music "title16.wav"
    scene black
    with Pause(1)

    show logo:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    with dissolve
    with Pause(3)

    hide logo with dissolve
    with Pause(1)

    return

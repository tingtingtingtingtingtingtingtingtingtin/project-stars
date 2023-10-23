# Season 0 Scene 1: Waking Up

label s0s1:
    mc "The night sky."
    mc "The giant expanse of the concert hall, a ceiling that stretches on for eternity."
    mc "A never ending void. {w} A maze without walls."
    scene bg stars with fade

    mc "A sea of bright lights suddenly fills my view."
    mc "Like the stars, dazzling but unreachable."
    pause 0.2
    mc "This feeling... is this the adrenaline of performance?"
    mc "I feel as if I'm rising, yet my body refuses to move."
    mc "Thousands of voices cut clearly through the noise, all crying out one name."
    mc "Unmistakably, it's my own."
    pause 0.5
    mc "..."
    mc "Hm."
    mc "... That's weird, what was my name again?"

    pause 0.5
    $ default_name = "Natsuha"
    $ player_name = renpy.input("What is my name? (Enter a blank for '[default_name]'.)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = default_name

    mc "That's right, my name is [player_name]... and I've always longed of becoming an idol."

    "\"[player_name]!\" {w} \"[player_name]!\" {w} \"[player_name]!\""

    mc "..."

    "\"[player_name]...!\" {w} \"[player_name]...!\""

    mc "Huh...?"

    scene bg black with fade

    mom "{size=+15}\"[player_name]!!!\"{/size} {w} Don't you have your audition to go to!?"

    scene bg dundee with vpunch
    show haruka happy with dissolve

    mc "{size=+5} UWAH! Crap, I'm gonna be late for my train! {/size}"

    mc "Coming, Mom...!"

    hide haruka happy with moveoutright
    return
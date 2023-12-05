define base_char = Character(color="#FFFFFF")
define narrator = Character(kind=base_char)

define unknown = Character("???", kind=base_char)

## Named
define s = Character("Seika", image="seika", kind=base_char, color="fcd544")
define n = DynamicCharacter('n_name', image="natsuha", kind=base_char, color="#f55c7a")
define m = DynamicCharacter('m_name', image="miyuki", kind=base_char, color="#b6c6e6")
define a = DynamicCharacter("a_name", image="akina", kind=base_char, color="#e74d4a")
define t = DynamicCharacter("t_name", image="tsuki", kind=base_char, color="#8b84a5")
define t_name = "Scary-Looking Woman"

## Other
define mom = Character("Mom", kind=base_char)
define phone = Character("Seika's Phone")
define kaori = Character("Kaori")
define ygp = Character("Young Girl Patient")

## Sprite Positions
transform l:
    xalign 0.1
    yanchor 1.0
    ypos 1.0
transform r:
    xalign 0.9
    yanchor 1.0
    ypos 1.0

## BGs
image black = "#000000"
image bg crowd = "bg/crowd.png"
image bg stage = "bg/stage.png"
image bg cafe = "bg/cafe.png"
image bg citycrossing = "bg/citycrossing.png"
image bg shrine = "bg/shrine.png"
image bg school = "bg/school.png"

## Sprites
image seika happy = "seika/happy.png"
image seika neutral = "seika/neutral.png"
image seika sad = "seika/sad.png"
image seika shock = "seika/shock.png"
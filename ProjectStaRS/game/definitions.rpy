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
image white = "#ffffff"
image bg stage = "bg/stage.png"
image bg cafe = "bg/cafe.png"
image bg citycrossing = "bg/citycrossing.png"
image bg residential = "bg/residential.png"
image bg shrine = "bg/shrine.png"
image bg school = "bg/school.png"
image bg room = "bg/room.png"
image bg room noon = "bg/room noon.png"
image bg room night = "bg/room night.png"
image bg shop district = "bg/shop district.png"
image bg sky noon = "bg/sky noon.png"
image bg star river 1 = "bg/star river/1.png"
image bg star river 2 = "bg/star river/2.png"
image bg star river 3 = "bg/star river/3.png"
image bg star river 4 = "bg/star river/4.png"
image bg star river 5 = "bg/star river/5.png"
image bg spotlight = "bg/spotlight.png"
image bg citycenter = "bg/citycenter.png"

## Sprites
image seika happy = "sprites/seika/happy.png"
image seika neutral = "sprites/seika/neutral.png"
image seika sad = "sprites/seika/sad.png"
image seika shock = "sprites/seika/shock.png"
image akina neutral = "sprites/akina/neutral.png"
image akina happy = "sprites/akina/happy.png"
image akina fear = "sprites/akina/fear.png"
image natsuha neutral: 
    "sprites/natsuha/neutral.png"
    zoom 0.52
image natsuha concern:
    "sprites/natsuha/concern.png"
    zoom 0.52
image natsuha happy:
    "sprites/natsuha/happy.png"
    zoom 0.52
image natsuha shock:
    "sprites/natsuha/shock.png"
    zoom 0.52
image natsuha pout:
    "sprites/natsuha/pout.png"
    zoom 0.52

## Props
image phone = "props/phone/off.png"
image phone broke = "props/phone/broke.png"
image phone hp = "props/phone/hp.png"
image phone hp_hang = "props/phone/hp hang.png"
image phone hp_call = "props/phone/hp call.png"
image phone unknown = "props/phone/unknown.png"
image phone unknown_call = "props/phone/unknown call.png"
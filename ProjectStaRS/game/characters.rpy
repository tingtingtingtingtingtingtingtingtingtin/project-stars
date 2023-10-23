define base_char = Character(color="#FFFFFF")
define narrator = Character(kind=base_char)

define unknown_name = "???"
default player_name = unknown_name

## Named
define mc = Character("player_name", dynamic=True, image="haruka", kind=base_char)

## Other
define mom = Character("Mom", kind=base_char)
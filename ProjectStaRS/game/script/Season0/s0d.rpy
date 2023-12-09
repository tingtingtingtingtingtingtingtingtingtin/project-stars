label s0d:
    scene bg spotlight
    centered "Awoken by birds chirping, I open my eyes, greeted by the sun burning into my retinas."
    centered "I instinctively hold up my hand, but the blinding light dances between my fingers and blurs my vision."
    centered "Looking down, I see I've woken up in a small bed, but it isn't my own."
    centered "Likewise, my environment doesn't resemble my room."
    centered "Instead of the posters I'm familiar with, my surroundings consist of walls— blurs of black lines that converge above me."
    centered "Beyond them lies the trunk of a giant tree stretching beyond the sky, a dissonance amidst the symphony of red and orange hues."
    centered "I wobble to the black lines and reach out to grasp metal bars."
    centered "They're cold, yet burn my palms to the touch."
    centered "They push me away."
    centered "I try to cry out for help, but I'm drowned out by the deafening silence."
    centered "My breathing skips to the rhythm of my heart, an instrument playing to a metronome."
    centered "Tick. Tick. Tick."
    centered "With each beat, the leaves all around me make their leap of faith, dropping one by one."
    centered "Before they reach the ground, a gust of wind blows past and lifts them \ntowards the skies, with the birds."
    centered "The wind creaks the rusty bars, signaling an open door, just barely ajar."
    centered "Hesitantly, I inch toward the gap that would grant me my freedom."
    centered "Near the roots of the tree, the leaves that made their way down safely \nlook like tiny dots below my feet."
    menu dreamMenu:
        "Should I leave?"
        "Stay put":
            centered "I reach towards the gate, but when my fingers graze the iron, I pull back."
            centered "I can't bring myself to leave, but I also can't help but look past the bars, beyond what lies here."
            centered "The wind blows past and some more leaves fall, some finding their way into my enclosure."
            centered "When I hear the birds sing their freedom song in unison, my eyes are drawn back to the gap between the door and its latches."
            jump dreamMenu
        "Go out":
            pass
    centered "I reach my hand towards the gate."
    centered "When my feet do not follow, vines wrap around my legs, preventing me from leaving."
    centered "Twisting and turning my body does nothing against its grasp."
    centered "Exhausted, my body goes limp."
    menu dreamMenu2:
        "It's safe in here. Don't go."
        "...":
            centered "I tell myself it's safe here. The outside world is scary, after all."
            centered "Even still, my eyes are drawn back to the gap between the door and its latches."
            centered "Do I crave freedom?"
            jump dreamMenu2
        "I can't be stuck here forever!":
            centered "I twist and turn my body, fighting against the pull of the vines."
            centered "When I move my feet, I feel a semblance of looseness."
            centered "I fight once more. I fall, but I try again."
        
    centered "When I finally manage to escape the grasp of the vines, I push the door out."
    centered "I close my eyes and take a deep breath, ready to take the leap of faith."
    scene white with Dissolve(2)
    centered "{color=#000000}{i}I’ll grow my wings too, just like the other birds.{/i}{/color}"
return
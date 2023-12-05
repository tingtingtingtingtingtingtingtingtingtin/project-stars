label s0s5: 

    "These last few days, the audition was the only thing on my mind. The day immediately after, I could hardly catch a wink of sleep waiting for that phone call."

    "And yet, a week had passed with no sign of a response. Had I been rejected already? Even worse, what if they forgot about me? Was my performance just that unmemorable?"

    "No, that can't be it. Natsuha said it was superb. Her opinion is invaluable to me, so I have to trust her judgment. Ah, but the other girls did so well too…"

    "Speaking of Natsuha, did she get a response yet? Should I call her?"

    "No, she should be at work right now. I know she'd pick up anyways, but I really shouldn't."

    "In the meantime, I've been rehearsing my responses to any outcome, whether I'm accepted or not."

    "Mom said she'd be proud of me regardless. I'm happy to have her support. Even if I don't make it, I…"

    "Nonono, you can't give up already! Everything will work out, Seika, I'm sure of it."

    "I slap my hands to my cheeks, pepping myself up. Maybe I should rehearse one more time to be safe."

    #[Seika]
    s "That's great news! I look forward to working with you! When do I start?"

    s "That's alright, thank you for the opportunity!"

    #[Seika's Phone] #[Ringing SFX] #[Phone sprite] #[Music stops, silence]
    phone "Bzz! Bzz! Bzz!"

    #[Seika]
    s "Is this…!?"

    #[-]
    "I jump out of bed to get my phone. A few of my plushies roll off the bed amidst my scrambling, but I can pick those up later."

    "I answer my phone and press it to my ear, too afraid to look at it. I hear a dull beep as I pick up."

    #[Seika]
    s "H-Hello? This is Seika, from the audition…"

    #[-]
    "My heart is hammering in my chest. Time slows to a crawl, and it feels like forever before I finally hear a voice. The voice that will determine my fate."

    "..."

    #[???]
    unknown "Hello there! Congratulations, you've been selected as the winner for our free uPhone 23 giveaway!"
    unknown "You have only 2 hours, and time is ticking, so hurry! To claim your prize, simply tell us your name and credit card information after the beep! Terms and conditions apply!"

    #[Seika]
    s "I-I'm not interested, sorry!"

    #[-] #[Night theme resumes]
    "I quickly hang up and breathe a heavy sigh. Another scam call, huh?"

    "I remember almost falling for one of those once. Luckily, Natsuha was nearby to stop me from doing anything reckless, but I got a big scolding about security and anti-phishing protection after that."

    "Thinking about it, I really do owe a lot to her. She's supported me all this way, even as I dragged her along on my whims."

    "I want to be an idol, but I don't know if she feels the same way. She's always looking out for me, so I have to step it up as her best friend."

    "... I've got it! I'll treat her to a meal with my allowance and ask her about her results there."

    "\"Natsu! When… are… you… free?\""
    
    #[Seika's Phone] #[Buzzing SFX] #[Music stops again]
    phone "Bzz! Bzz! Bzz!"

    #[Seika] #[Screen shaking, dropping SFX] #[Phone sprite disappears]
    s "AH!!!!"

    #[-]
    "As I'm about to hit 'send', my phone vibrates aggressively in my hands. I drop it in shock."

    #[Seika]
    s "!!!!!"

    #[-] #[Phone sprite reappears, this time cracked]
    "I pick up my phone again to see a large crack in it."

    "But that isn't what surprises me, it's the name on the caller screen – Horizon Productions."

    "I answer without hesitation."

    "Before I can speak, the voice on the other side starts."

    #[???] #[Phone sprite and BG disappear, black BG] #[Music stops]
    $ t_name = "Serious Voice"
    t "Is this Seika?"

    #[Seika]
    s "Y… Yes! That's me."

    $ t_name = "Tsuki"
    #[Tsuki]
    t "This is Tsuki."

    t "I'm calling on behalf of Horizon Productions to inform you that you passed the auditions, and have been selected to be a part of our trainee program."

    #[-]
    "My voice catches in my throat. I've been preparing nonstop for this moment, yet I still can't believe it." 
    
    "I did it! I really did it! I'm going to be an idol!"

    #[Seika]
    s "T-T-That's great news! I look forward to getting started, um…! Thank you so so much! When do I… do we work?"

    #[Tsuki]
    t "Don't thank me yet. Your audition showed us your potential, but that doesn't guarantee your debut. The rest is still up to you." 
    
    t "Our training regimen is strict. Will you be able to keep up?"

    #[Seika]
    s "Y-Yes! If that's what it takes, then I’ll do anything!"

    #[-]
    "Her voice was firm and honestly a little intimidating, but I managed to stand my ground. These terms were no stranger to me, all thanks to my preparations."

    "But then she says something that strikes me off guard."

    #[Tsuki]
    t "You'll be expected to work like you've never worked before, to show up to practice rain or shine."
    
    t "You'll have to endure at all costs, to keep smiling in the face of hardship."

    t "If you falter for even a moment, then you can kiss your career – your entire life – goodbye."

    t "That is what it means to be an idol."
    
    t "Horizon Production shares little sympathy to those who don’t give it their all, even if it saps everything from you."
    
    t "Take it from my experience."

    #[Seika]
    s "I…"

    #[-]
    "Her words shake me to my very core."

    "For a moment, it's like I've caught a glimpse of something darker, something that makes me question: What am I getting myself into?"

    "I don't understand why, but she's giving me a chance to back out while I still can."

    #[Player choice:]
    menu:
        "I need to choose wisely."
        "Accept her terms":
            pass
        "Back out":
            call s0end
            return

    #[-]
    "As nervous as I was, I couldn't back out now and let my efforts go to waste. Gather yourself, Seika!"

    #[Seika]
    s "... I understand. I'll do it."

    s "I'll show up to practice, I'll meet your expectations, and… I'll endure, and keep smiling, no matter what!"

    #[Tsuki]
    t "Very well then. Orientation will begin on Monday the 22nd at 9 AM sharp, followed immediately by practice."

    #[Seika]
    s "Got it! I promise you won't regret accepting me!"

    #[Tsuki]
    t "Hmph. I hope not. See you there."

    #[Seika]
    s "Goodbye, Producer!"

    #[Tsuki]
    t "Tsuki is fine. We'll be working closely from here on out."
    
    t "I'm expecting nothing but the best from you, so show up for orientation on time and prepared."

    t "... Oh, and one more thing."

    s "Hm?"

    t "You did well, Seika."

    t "She must be proud of you."

    t "... Goodbye."

    #[Beeping noise]
    "Tsuki hangs up."
    
    "I'm confused by her parting words, but I think I made a strong impression, at least."

    "I lay back in bed, recounting our conversation." 

    "There's a fuzzy feeling in my chest, a mix of excitement and… warmth. The kind of warmth I feel when Mom praises me."

    "... That's right. From here on out, I'll be in her care. My soon-to-be producer…"

    "The lights on my ceiling turn into the spotlights of the auditorium stage where I auditioned. I reach my hand out towards the bright lights, blocking them out with the shadow of my outstretched palm."

    "I recall her face in the back of my hand, the way she looked at me as I sang my heart out. Her eyes were wide, filled with an emotion I couldn't describe."

    "Was it admiration? Or something… deeper?"

    "Tsuki… Did she see something in me there?"

    "I close my fingers into a fist, eclipsing that sphere of light completely."

    "..."

    "But…"

    "\"She must be proud of you.\""

    "What did she mean by that?"

    #[END SCENE. GO TO SEASON 1 SCENE 1.]
    return
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alistair White")

define d = Character("Don Dalli")

define c = Character ("Crowe")

define r = Character ("The Rose")

default preferences.text_cps = 45
default preferences.afm_enable = False

transform shake:
    linear 0.175 xoffset -2
    linear 0.175 xoffset +0
    linear 0.175 yoffset -2
    linear 0.175 yoffset +0
    repeat

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "Airegin.mp3"

    window hide
    
    scene bg_eyedoor

    pause 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    window show

    # These display lines of dialogue.

    a "It was September, 1939. The outbreak of the Second World War. America wasn't involved that much yet. We were somewhat at peace."

    a "It was more peaceful than Europe at least. Life was somewhat the same in my city, Hanear."

    a "I am Alistair White, Private Investigator. The day started like any other..." 

    window hide
    scene mirrorshot
    with fade

    pause 
    window show
    a " \"God, I am looking older by the day...\" I say to myself in the mirror... Like an absolute nut!"

    window hide
    scene bg_office

    pause

    window show
    a "My lovely office. How nice this place is..."
    
    stop music fadeout 1.0
    "KNOCK KNOCK!"
    
    a "Who the Hell is that?"
    
    menu:
        
        "Who the Hell are you?":    
            a "Who the Hell are you? Knocking on my door at 10 pm!"
            a "Office hours, ever heard of them?"
            d "It is the Don... Don Dalli. Learn to show respect and open this door, you {i}cazzo{/i}!"
            jump after_menu
        
        "Who knocks?":  
            a "Who knocks on my door at this hour?"
            d "It is I, the head of the Dalli Family. Your services are needed."
            jump after_menu
    
    label after_menu:   

    window hide
    pause
    show dondilla
    with fade
    play music "<from 4>Agua De Beber (Water To Drink).mp3"   

    a "Hello Don Dalli... Have we met?"
    d "We have not. I work in risky business Mr White..."
    a "You're an italian man, in a nice suite..."
    a "Going by Don and is here late at night. I can only assume you're a mob boss."
    show dondillaannoy
    d "Just because I'm italian?"
    d "My nonna would be rolling in her grave right now..."
    show dondilla
    hide dondillaannoy
    d "But yes, I am... I'm the head for the Dalli Crime Family." 
    d "I need your help with a few things"
    a "Very well, I'm going to charge you big time though."
    show dondillasmoke
    hide dondilla
    d "That is fine. Two of my men have been killed, P.I.!" 
    d "Stuffed with flowers of all things."
    a "Murder? Sounds like a case for the police-"
    d "I'm a criminal, Mr White. The authorities are useless anyways." 
    d "Figure out who did this to them."
    d "These were important Dalli family members. My zio Leo and my cugino Giovanni."
    a "Fine. 1000 dollars. This is a dangerous case."
    d "Fine, very well. I'm looking forward to you catching whichever parasite did this to the familia."
    hide dondillasmoke
    show dondillasmile
    d "I left some papers on your table. Locations. Get to it."
    d "The Dalli family knows that you can work."
    d "You took down a fellow Hanear gang, a Soviet mob boss, Nazis... Make good work of this murderer."
    a "How did you know about my past cases? Doesn't matter anyways. I will get to it."
    d "I shall leave you to it."
    hide dondillasmile
    with dissolve
    a "Time to check those papers I suppose."

    scene bg_addresses
    window hide
    pause

    a "Papers?!? These are just addresses... Jaysus"
    a "Is that blood? Eugh, anyways, I guess this is a start." 
    a "I'm going in blind I suppose."
    a "I'm going to make a phone call with my police contact, Crowe. He's a smart guy..."
    a "He'll be able to help."
    stop music fadeout 1.0 

    scene bg_phone1
    window hide
    pause
    "RING RINGGGG"
    a "Pick up man..."
    pause 3.0
    scene bg_phone2
    a "Crowe?"
    c "'Ello Alistair. You call late."
    a "Sorry, are you up?"
    c "Sure. What business do you have this time?"
    a "Mob case. Two murders, apparently \"stuffed with flowers\", whatever that means."
    c "Interesting... The pay?"
    a "1000 dollars. 50/50 cut this time 'round?"
    c "Aye, sounds good Al. I'll meet you outside your building?"
    a "Yes please. Thank you Crowe, as always."
    c "No problem, see ya soon man. "
    play music "<from 2.0>Yesterdays.mp3"
    scene bg_phone1
    a "Time to meet the man himself outside. Hopefully we can finish this case tonight. If we're lucky."
    a "Let's see where these addresses lead us."

    scene bg_street1
    hide window
    pause
    "Outside..."
    a "Where could this man be? I hope I'm not wating in the cold rain for long."
    a "Maybe I should light a smoke."
    a "What the Hell is Schmep's?"
    show crowe
    with fade
    c "Hello there Alistair, cold night, ain't it?"
    a "Crowe! Good to see you."
    c "What do we have to work with?"
    c "Gimme a run down, spare some details. We don't have all night, yeah?"
    a "Mob killings, two victims stuffed with flowers, like I mentioned earlier on the phone."
    hide crowe
    show croweinterest
    c "Yeah, that's right. The murderer might be going with some sort of calling card."
    c "Their own \"shtick\" I suppose."
    a "I can only assume so. I was provided two addresses for each murder."
    a "56 Angie Way and 81 Drumond Drive."
    c "No further details? I guess the mobs around here like to keep their secrets."
    a "I have no idea where these addresses lead." 
    a "Where do you want to check out first?"
    hide croweinterest
    show crowesmile
    c "Alistair, you're the lead investigator here. I trust your judgement more than my own."
    a "Sure. Let's see..."

    menu:
        "Let's try Angie Way":
            a "Let's go to Angie Way first. Nicer name. Hopefully a less bloody crime scene"
            c "We can only hope, eh?"
            a "Let's get going..."
            stop music
            hide crowesmile
            scene angie
            window hide
            play music "<from 4>My Funny Valentine.mp3"
            pause
            a "This is it, a garage."
            c "Let me get upfront..."
            show crowe
            with fade
            c "Spooky place, ain't it?"
            a "I've dealt with worse. Prepare yourself."
            hide crowe
            show crowesmile
            c "For a guy stuffed with flowers? I've dealt with worse..."
            a "Funny guy, you are. Let's head in and see what a man stuffed with flowers looks like."
            hide crowe
            stop music
            scene murder1
            with fade
            window hide
            pause
            
            c "Oh Lord..."
            a "There he is. Stuffed with flowers in the mouth."
            c "Bleeding out his holes too. Eyes, ears, nose..."
            a "I notice some marks, from blunt force. You can see around his arms."
            scene garageinside
            show crowescared
            play music "<from 4>My Funny Valentine.mp3"
            c "I wonder what finished him off. Poisoning, judging by the bleeding? Or just smacked to death."
            a "And flowers added just as some sort of garnish?"
            hide crowescared
            show croweinterest
            c "Calling card! I knew it..."
            c "Anyways, what do you think?"
            menu:
                "Blunt force.":
                    a "I think it has to be the hitting..."
                    a "All of the marks..."
                    a "His arms were basically purple. That wouldn't kill him though..."
                    jump murder1
                "Poisoning.":
                    a "I think it has to be poison..."
                    a "The bleeding from the eyes, ears, and nose..."
                    a "But how about all of those marks?"
                    jump murder1
            
            label murder1:  

            a "It must be a combination of both!"
            hide croweinterest
            show crowe 
            c "Is that so?"
            a "I predict a surprise attack, constant hitting. But a prior poisoning to that."
            a "The killer poisoned him, but it must of taken too long." 
            a "The murderer might have hit him to finish him off. Then the poison acted quickly."
            c "And the flowers on top... The calling card."
            a "That's right Crowe."
            a "I see a hammer behind you... Let me see that..."
            scene hammer
            a "Interesting... Leed's Shoppe?"
            c "I swear that's a store here, in Hanear!"
            c "Wait... This doesn't mean this hammer is the killer's."
            c "It could have just been previously owned by the man here."
            scene garageinside
            show crowe
            a "Let's look at the other tools... Hmmmm..."
            a "All different brands. This is the odd one out, this garage already has a hammer."
            c "But why'd they bring a hammer? And leave it?"
            c "It's almost like..."
            hide crowe
            show crowescared
            a "They wanted to be caught. We must proceed with caution from here on out..."
            c "Aye... Let's head back outside"
            jump murders




        "Let's try Drumond Drive":
            a "Let's go to Drumond Drive. I like the alliteration."
            c "Very well, word boy."
            a "Boy? Who are you calling boy?"
            c "Nothing....Let's get going..."
            scene timmys
            with fade
            play music "<from 2>Footprints.mp3"
            c "Timmy's?"
            a "Yeup, a Dalli family front... A Dalli family stronghold."
            show crowe
            with fade
            c "Jeez, this murderer hates the Dallis..."
            a "Let's keep that in mind. Wanna head in?"
            c "Let's get going."
            stop music
            scene murder2
            with fade
            hide window 
            pause
            c "I have no words."
            a "I do. Hung up, and stabbed a bunch of times."
            c "Let's leave this room."
            scene restaurant
            show crowescared
            a "Spooked?"
            hide crowescared
            show crowe
            c "I'm fine..."
            play music "<from 2>Footprints.mp3"
            a "What do you think happened?"
            c "Hung up and stabbed. Wrapped around with vines and flowers."
            a "The calling card. It's almost like whoever's doing this wants to be caught."
            c "What's this... I see something..."
            scene knife
            a "The murder weapon..."
            c "This doesn't help at all!"
            c "We don't have the time for fingerprints."
            a "Yes we do... but we don't need fingerprints anyways"
            scene restaurant
            show crowe
            a "Check this out... A bloodied receipt, beside the knife... Of this knife's purchase?"
            c "We're by a kitchen. Did she really have to buy a knife?"
            a "We've established that the murderer wants to be caught..."
            a "The receipt is for Leed's Shoppe."
            c "Well, might as well get going..."
            a "Let's proceed with caution though."
            a "We don't want to be hung up with flowers next..."
            c "You're right. Let's go."
            jump murders
        
    label murders :
            
    scene bg_street1
    with fade
    show croweinterest
    stop music
    a "Okay, let's think."
    c "This murderer wants to be caught."
    a "Indeed they do. The calling card, leaving around blantant clues..."
    c "So we must proceed with caution."
    c "How though?"
    show crowesmile
    a "With guns. You got yours?"
    c "Of course."
    a "Good. Now, let's head to this \"Leed's Shoppe\", shall we?"
    c "Aye aye, sir."

    scene leeds
    with fade
    window hide
    pause
    play music "<from 4>Juju.mp3"
    show crowe
    with fade
    c "So this is Leed's."
    a "Sketchy part of town..."
    c "This is Hanear! Most of this city is sketchy."
    hide crowe
    show crowesmile
    a "Ha! You make a good point there, Crowe."
    c "Now! Shall we head in?"
    a "Yes. Expect the worse though. Be on high alert."
    c "I always am..."
    
    scene garden1
    with fade
    show croweinterest
    with fade
    c "So this is Leed's. Big selection of flowers and plants..."
    a "The flowers just like our murderer's..."
    a "This is definetely where they got their stuff."
    hide croweinterest
    show crowe
    c "Want to explore? How about we check the garden behind me."
    a "Sure. Ready your gun. The murderer is probably waiting for us."
    a "I don't think they have a gun though."
    a "They probably would have used it on their victims."
    c "Or maybe they're sick and doesn't want to use a gun..."
    a "Fair point..."
    stop music
    "BANG!!!"
    hide crowe
    show crowescared
    c "That was from behind me!!!"
    c "We have to go in!!!"
    a "With caution, Crowe!"
    scene garden2
    with fade
    show crowegun 
    with fade
    c "Let's be slow... I don't want to get spooked or anything..."
    a "This is like a game of cat and mouse!"
    a "I'll watch your back..."
    a "It's real quiet..."
    scene garden2eye
    show crowegun
    a "Wait a second... Crowe... Back there..."
    c "Hm??"
    scene roseeye
    with fade
    window hide
    pause
    a "There's an eye!!!"
    a "It has to be the murderer!!!"
    a "Crowe!! Shoot!!!"
    scene gun
    with fade
    window hide
    pause
    "BANG BANG"
    "BANG"
    c "Do you think I got 'em?"
    scene gunaftermath
    window hide
    pause
    play music "<from 4>Juju.mp3"
    c "Do you think I got 'em?"
    a "I'm afraid not. You shot a whole lot of plants."
    c "Dammit!"

    menu:
        "Let's split up.":
            a "We should split up, cover more ground that way."
            c "What? Hell no! There's a murderer amongst us, remember?"
            a "I think this is the right decision Crowe!"
            a "We have to catch them!"
            c "Fine, you have your gun right?"
            a "Yes, I'll explore the building."
            jump decision1

        "Come with me.":
            a "Come with me Crowe."
            c "We have our own guns, right?"
            c "No need to split up!"
            a "Crowe, are you su-"
            c "Let's split ways."
            a "Okay, yell for help when needed."
            jump decision1
    
    label decision1 :
    scene garden1
    a "Where to look, where to look..."
    a "Hmmmmm...."
    stop music
    show rose
    with fade
    r "Hello. I am The Rose. Your murderer."
    a "Is that a knife pressed against my stomach?"
    r "Yes it is."
    r "Who are you... You don't look like a Dalli."
    a "That's because I am not. I'm Alistair White, private eye."
    r "You're no use to me. But I can't let you leave..."
    a "You have a thing for Dallis, don't you?"
    hide rose
    show rosesmile
    r "Oh yes. I love killing them."
    a "That so? Why?"
    r "They're a plague to this city, you know that right?"
    a "I do."
    r "Then if you know what's good for you, you'll leave me be."
    hide rosesmile
    show rose
    r "Let me continue killing them. Let me lead them here."
    r "What say you?"

    menu:
        "Killing is not the way.":
            a "Killing won't solve shit."
            r "Yes it will."
            a "It leaves a power vacuum. Another horrible gang will take its place."
            r "Then I'll kill them too."
            a "Violence breeds violence."
            r "Better then letting stupid lawyers and cops deal with it."
            a "Rose, I'll let you off the hook if you just stop."
            r "THE Rose to you. And..."
            r "No!"
            jump rose1

        "I get it.":
            a "I get it. I hate the Dallis too."
            r "Then kill them with me."
            a "I have killed gangs in the past..."
            hide rose
            show rosesmile
            r "See? Then you won't have any problem with it!"
            a "No! I am beyond that..."
            hide rosesmile
            show rose
            r "Help me."
            jump rose1
    
    label rose1 :
    c "I got you!"
    hide rose
    show rosefrown at shake
    "BANG BANG"
    show rosefrown at reset
    r "GAH"
    hide rosefrown
    with dissolve
    show crowe
    c "You okay?"
    a "Y-yeah..."
    c "Well, let's go after her!"
    scene leeds
    show crowe
    c "Where could have that women gone..."
    c "What was her deal?"
    a "Hates the Dallis."
    c "Why? Well, I know why... but why?"
    a "We didn't get to it..."
    c "You alright Al?"
    a "Yeah yeah... she made a good point though."
    c "Killing Dallis is good?"
    a "Yes... I've killed in the past... Why shouldn't I stop now?"
    a "The Dallis are horrible."
    a "Murder, robberies, trafficking, extorsion... so much more..."
    c "She's getting into your head!"
    a "I have a license to kill. Shouldn't I use this for good?"
    c "You can't go around killing people."
    c "You're not the law. The law can't even do that."
    a "I..."
    hide crowe
    show crowescared
    c "Are you thinking of joining her?"
    a "No... Maybe..."
    hide crowescared
    show crowe
    c "Enough of this. I'm going to drop this case with you..."
    c "If you continue this behavior."
    a "What? What are you, my mom?"
    hide crowe
    show crowesmile
    c "Maybe..."
    c "I am younger than you however."
    a "Har har."
    c "Listen... I think I'm out. It's all you now..."
    c "I don't care what you do. Just don't get kiled by her..."
    c "Or the Dallis..."
    a "I'll try."
    c "See you, Al."
    c "Call me next time when you have a case without a moral questioning session."
    a "Ha! Bye Crowe... thank you."
    c "Good luck."
    hide crowesmile
    with dissolve
    a "Let me think..."
    
    play music "<from 2.0>Yesterdays.mp3"
    scene bg_street1
    a "Okay... What to think..."
    r "Psst!"
    show rose
    with fade
    r "Hello Al..."
    a "Were you eavesdropping?"
    r "Maybe..."
    a "Listen, I still think you're sick... But maybe we can do something..."
    hide rose
    show rosesmile
    r "About that Dalli problem?"
    a "Yes."
    a "Again, let me think..."
    stop music

    menu:
        "I'm not letting you go.":
            a "I'm not letting you get away."
            hide rosesmile
            show rose
            r "Huh?"
            r "Is that your gun... Pointed to me..."
            a "Yes..."
            r "Al, you can't be real..."
            a "You're acting like you know me! You don't!"
            r "So you're not going to kill them, but me?"
            a "I'm taking you into the station."
            r "On what business? Who do you think you are?"
            a "CITIZENS ARREST!"
            r "CITIZENS ARREST MY ASS!"
            a "Hey, don't reach for my gun!"
            r "Get that outta here!"
            "BANG"
            hide rose
            show roseblood
            r "Gruhugh..."
            r "You just shot... My stomach..."
            r "Asshole..."
            a "Shit."
            a "HELP! SOMEONE CALL AN ABULANCE!"
            r "It's no use. You are a traitor to the people of Hanear..."
            hide roseblood
            with dissolve

            a "Welp..."
            a "I might have to call it a day here..."
            play music "<from 2.0>Yesterdays.mp3"
            a "1000 dollars though, not bad."













    # This ends the game.


    return

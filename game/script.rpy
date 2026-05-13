# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alistair White")

define d = Character("Don Dalli")

define c = Character ("Crowe")

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
            a "Who the Hell are you? Knocking on my door at 10 pm! Office hours, ever heard of them?"
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
    a "You're an italian man, in a nice suite... Goes by Don and is here late at night. I can only assume you're a mob boss."
    show dondillaannoy
    d "Just because I'm italian? My nonna would be rolling in her grave right now..."
    show dondilla
    hide dondillaannoy
    d "But yes, I am... I'm the head for the Dalli Crime Family. I need your help with a few things"
    a "Very well, I'm going to charge you big time though."
    show dondillasmoke
    hide dondilla
    d "That is fine. Two of my men have been killed, P.I.! Stuffed with flowers of all things."
    a "Murder? Sounds like a case for the police-"
    d "I'm a criminal, Mr White. The authorities are useless anyways. Figure out who did this to them."
    d "These were important Dalli family members. My zio Leo and my cugino Giovanni."
    a "Fine. 1000 dollars. This is a dangerous case."
    d "Fine, very well. I'm looking forward to you catching whichever parasite did this to the familia."
    hide dondillasmoke
    show dondillasmile
    d "I left some papers on your table. Locations. Get to it. The Dalli family knows that you can work."
    d "You took down a fellow Hanear gang, a Soviet mob boss, Nazis... Make good work of this murderer."
    a "How did you know about my past casses? Doesn't matter anyways. I will get to it."
    d "I shall leave you to it."
    hide dondillasmile
    with dissolve
    a "Time to check those papers I suppose."

    scene bg_addresses
    window hide
    pause

    a "Papers?!? These are just addresses... Jaysus"
    a "Is that blood? Eugh, anyways, I guess this is a start. I'm going in blind I suppose."
    a "I'm going to make a phone call with my police contact, Crowe. He's a smart guy..."
    a "He'll be able to help"
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






    # This ends the game.


    return

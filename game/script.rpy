# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alistair White")

define d = Character("Don Dalli")

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

    a "Hello Don Dilla... Have we met?"
   








    # This ends the game.


    return

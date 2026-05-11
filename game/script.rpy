# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alistair White")


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

    a "It was September, 1939. The outbreak of the Second World War. An older man like me couldn't fight."

    a "I was left at home. Plus America wasn't involved until later. Life was somewhat the same."

    a "I am Alistair White, Private Investigator. The day started like any other..."

    # This ends the game.

    return

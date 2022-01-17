from Player import Player


def main():
    User.location = "start"

    print("You open your eyes. Your surroundings are blurry.")
    
    eye_decision()

    print("You stand up and survey the room.")
    starting_area()


    if User.location == "start":

        starting_area()
    elif User.location == "mirror":

        print("You walk up to the mirror")
    elif User.location == "window":

        print("You walk over to the window")
    elif User.location == "door":
        
        print("You walk towards the door.")




def starting_area():

    direction = ""

    print("Behind you is a wall. In front of you is a mirror. To the left is a door. To the right is a window.")

    direction = input("Which way will you head? (back/forward/left/right)")

    if direction.lower().strip() == "back":

        print("That's a wall... So, you turn back to find a new path")
        User.location = "start"
        User.action_count += 1
        return
    elif direction.lower().strip() == "forward":

        User.location = "mirror"
        User.action_count += 1
        return
    elif direction.lower().strip() == "left":

        User.location = "door"
        User.action_count += 1
        return
    elif direction.lower().strip() == "right":

        User.location = "window"
        User.action_count += 1
        return


def eye_decision():
    while User.eyesight == None:

        eye_decision = input("Will you blink furiously or rub your eyes? (blink/rub)")

        if eye_decision.lower().strip() == "blink":

            print("It did little to improve your eyesight...")
            User.eyesight = 0
            User.action_count += 1
        elif eye_decision.lower().strip() == "rub":

            print("Your eyesight has improved remarkably!")
            User.eyesight = 1
            User.action_count += 1
        else:

            print("Could you repeat that?")


#==============================================================
play_game = input("Would you like to play? (yes/no)")

if play_game.lower().strip() == "yes":

    name = input("What is your first name?")
    User = Player(name, None, 0, True, [], "Start")

    main()
             
else:
    print("Maybe another time")
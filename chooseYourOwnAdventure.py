from Player import Player


def main():
    User.location = "start"
    items = ["lighter", "knife", "key"]

    print("You open your eyes. Your surroundings are blurry.")
    
    eye_decision()

    print("You stand up and survey the room.")


    while User.location == "start" or User.location == "mirror" or User.location == "window" or User.location == "door":
        if User.location == "start":

            User.action_count += 1
            starting_area()
        elif User.location == "mirror":

            print("You walk up to the mirror")
            User.action_count += 1
            mirror_area(items)
        elif User.location == "window":

            print("You walk over to the window")
            User.action_count += 1
        elif User.location == "door":

            print("You walk towards the door.")
            User.action_count += 1



def mirror_area(items):
    pickup_more = "yes"

    print("You look into the mirror and see your bloodshot eyes staring back at you. You don't make a pretty picture.")
    print("Looking below the mirror you see an odd assortment of items.")

    while pickup_more == "yes":
        print("Which do you pickup?")
        pickup = input(items[0:])


        if pickup.lower().strip() == "lighter":

            print("You check to make sure it has fuel and then pocket the lighter.")
            User.inventory.append("lighter")
            items.remove("lighter")
            User.action_count += 1
        elif pickup.lower().strip() == "knife":

            print("You have picked up the knife. Watch out for those pointy bits!")
            User.inventory.append("knife")
            items.remove("knife")
            User.action_count += 1
        elif pickup.lower().strip() == "key":
        
            print("You think it's for the door. It probably is, so you decide it is best to bring it.")
            User.inventory.append("key")
            items.remove("key")
            User.action_count += 1

        pickup_more = input("Do you want to keep picking up items? (yes/no)").lower().strip()

    print("You finish picking up items and head back out into the room.")
    User.action_count += 1
    User.location = "start"
    



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
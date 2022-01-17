from Player import Player


def main():
    User.location = "start"
    items = ["lighter", "knife", "key"]
    #why does it remain closed
    window = "closed"

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
            window_area(window)
        elif User.location == "door":

            print("You walk towards the door.")
            User.action_count += 1


# def door_area():
#really dark use lighter, good eyesight needed to see wire that goes to outside door, knife cuts wire, key opens door. No knife you explode when you open the door




def window_area(window):

    if window == "closed":
        knife_decision = "no"

        print("You peer out the window. Your eyes straining to see out of the cloudy glass.")
        print("You look at the latch and see it is broken. Maybe you can pry it open.")

        pry_open = input("Would you like to try to pry it open? (yes/no)")


        if pry_open.lower().strip() == "yes" and not "knife" in User.inventory:

            print("You try to open it with your hands to no avail.")
            User.action_count += 1

        if pry_open.lower().strip() == "yes" and "knife" in User.inventory:
            knife_decision = input("Would you like to open the window with your knife? (yes/no)")

            if knife_decision.lower().strip() == "yes":

                print("You wedge the blade in and pop open the window. The knife has broken in two. What a shame.")
                User.action_count += 1
                window = "open"
                User.inventory.remove("knife")

                print("You peer outside and see the thickest fog you have ever seen. As thick as pea soup does not do it justice. You feel even worse for having broken your knife.")
            else:

                print("You decide against it.")

    else:
        print("A slight breeze is blowing in through the window... It taunts you. It's so foggy there is no point in trying to see anything.")



    print("After looking out the window you decided to head back into the room")
    User.location = "start"



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
from Player import Player
from Enviornment import Enviornment


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
            window_area()
        elif User.location == "door":

            print("You walk towards the door.")
            User.action_count += 1
            door_area()


def door_area():

    if Area.light == "dark":

        print("You're now standing in front of the door. It is suspiciously dark over here.")
        lighter_on()
        User.action_count += 1
    else:
        print("The door is well lit now.")


    if User.eyesight == 1 and Area.light == "lit":

        print("Is that a wire hidden by the door frame?")
        print("It appears to go through the wall.")
        print("Something about that doesn't seem right.")
        wire_cut()


    if "key" not in User.inventory:

        print("The door appears to be locked. Maybe there is a key back in the room.")
        User.location = "start"
        User.action_count += 1
    else:

        print("Should I open it with the key?")
        key_decision = input("(yes/no)")

        if key_decision == "yes":

            open_door()
            User.action_count += 1
        else:
            print("I'll go back into the room till I am ready.")
            User.location = "start"



def open_door():

    print(Area.light, Area.wire)
    if Area.light == "lit" and Area.wire == "cut":
        
        print("The door opens with a creak.")
        print("You step through")
        print("You lived!")
        print(User.name + " survived and took " + str(User.action_count) + " actions to make it!")
        User.location = "end"
    
    else: 

        print("The door creaks ominously as it opens.")
        print("You step through")
        print("You see a flash of light for what feels like an eternity before you hear the boom.")
        print("You fall to the ground involuntarily and roll away till the wall halts your progress.")
        print("Is that my body?")
        print("Your last thought before your eyes go dim.")
        print(User.name + " died and took " + str(User.action_count) + " actions to fail...")   
        User.location = "end"

    


def wire_cut():

    if "knife" in User.inventory:
        knife_cut = input("Would you like to sever it with your knife? (yes/no)")

        if knife_cut.lower().strip() == "yes":

            print("I cut the wire and hear a small click on the other side. Good or bad, there's no going back.")
            Area.wire = "cut"
            User.action_count += 1
        else:

            print("Maybe I shouldn't. Who knows what'll happen if I do.")


def lighter_on():

    if "lighter" in User.inventory:
        
        lighter_on = input("Would you like to light it? (yes/no)")

        if lighter_on.lower().strip() == "yes":

            print("There, that's much better.")
            Area.light = "lit"
        else:

            print("Maybe later.")

    else:
        
        print("I guess I can open it in the dark, it's just a door.")


def window_area():

    if Area.window == "closed":

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
                Area.window = "open"
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
    User = Player(name, None, 0, [], "Start")
    Area = Enviornment("closed", "dark", "intact", "closed")

    main()
             
else:
    print("Maybe another time")
#Movement direction is crucial here – you must create walls and set the directions in which the users can move through the rooms, set movement restrictions, 
# and also include a tracker that can track how far a user has walked or moved in the game. Mentioning Python projects can help your resume look much more interesting 
# than others.

play_game = input("Would you like to play? (yes/no)")

if play_game.lower().strip() == "yes":

    eyesight = None
    action_count = 0

    print("You open your eyes. Your surroundings are blurry.")
    
    while eyesight == None:
        eye_decision = input("Will you blink furiously or rub your eyes? (blink/rub)")
        if eye_decision.lower().strip() == "blink":
            print("It did little to improve your eyesight...")
            eyesight = 0
            action_count += 1
        elif eye_decision.lower().strip() == "rub":
            print("Your eyesight has improved remarkably!")
            eyesight = 1
            action_count += 1
        else:
            print("Could you repeat that?")
             

else:
    print("Maybe another time")
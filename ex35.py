from sys import exit


def gold_room():
    """Defines what happens in the gold room"""
    print "This room is full of gold, How much do you take?"

    nextmove = raw_input("> ")
    how_much = 0
    if "0" in nextmove or "1" in nextmove:
        how_much = int(nextmove)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    """Defines what happens in the bear room"""
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        nextmove = raw_input("> ")

        if nextmove == "take honey":
            dead("The bear looks at you then slaps your face off.")

        elif nextmove == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif nextmove == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif nextmove == "open door" and bear_moved:
            gold_room()
        else:
            print "I have no idea what that means."


def cthulhu_room():
    """Defines what happens when visiting Cthulhu"""
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    nextmove = raw_input("> ")

    if "flee" in nextmove:
        start()
    elif "head" in nextmove:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    """Tells you why you died"""
    print why, "Good job!"
    exit(0)


def start():
    """Starts the adventure"""
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    nextmove = raw_input("> ")

    if nextmove == "left":
        bear_room()
    elif nextmove == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

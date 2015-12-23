def north_pole():
    """This is the start of the adventure, The North Pole"""

    visited = 0
    north_pole_places = ["The Gift Shop", "The Reindeer Stables", "The Sleigh Launch Area", "The Base"]

    if visited == 0:
        print "You are at the start of your adventure! \n "
        print "\tYou are Santa Claus, ready to go hand out gifts to the world!"
        print "\tYou are at your base, the North Pole."
        visited += 1
        print "Where do you want to go?"
        print "On the North Pole, you can go to:"
        print place_print(north_pole_places)
        goto_next = raw_input("I'll go to number: ")
        select__north_pole_place(goto_next)
    else:
        print "You are back at the North Pole Base."
        print "On the North Pole, you can go to:"
        print place_print(north_pole_places)
        goto_next = raw_input("I'll go to number: ")
        select__north_pole_place(goto_next)


def place_print(places):
    """Print out the places you can go to on the North Pole"""

    for place in places:
        print (place)


def select__north_pole_place(goto_next):
    """Selects places to go to from the North Pole base"""

    if goto_next == "1":
        gift_shop()

    elif goto_next == "2":
        reindeer_stables()

    elif goto_next == "3":
        sleigh_launch()

    elif goto_next == "4":
        print "You are already there!"
        print "Go where else?"
        goto_next = raw_input("I'll go to number: ")
        select__north_pole_place(goto_next)
    else:
        print "That's not a place on the North Pole!"
        print "Please answer with a number from the list."
        goto_next = raw_input("I'll go to number: ")
        select__north_pole_place(goto_next)


def gift_shop():
    print "Gift shop!"
    # TODO write out gift shop


def reindeer_stables():
    print "Reindeer stables!"
    # TODO write out reindeer stables


def sleigh_launch():
    print "Sleigh Launch!"
    # TODO write out sleigh launch


north_pole()

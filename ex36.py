def north_pole():
    """
    This is the start of the adventure, The North Pole
    """

    visited = 0

    def place_print():
        places = ["The Gift Shop", "The Reindeer Stables", "The Sleigh Launch Area"]
        for place in places:
            number = 1
            print (number, place)

    if visited == 0:
        print "You are at the start of your adventure! \n "
        print "\tYou are Santa Claus, ready to go hand out gifts to the world!"
        print "\tYou are at your base, the North Pole."
        visited += 1

    else:
        print "You are back at the North Pole Base."

    def select_place():

        print "Where do you want to go?"
        print "You can go to:"
        print place_print()
        goto_next = raw_input("I'll go to number: ")

        if goto_next == 1:
            gift_shop()

        elif goto_next == 2:
            reindeer_stables()

        elif goto_next == 3:
            sleigh_launch()

        else:
            select_place()


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

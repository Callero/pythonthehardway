def start():
    print "You are at the start of your adventure! \n " \
          "\tYou are Santa Claus, ready to go hand out gifts to the world!"
    print "Where do you want to go?"
    print "You can go to:"
    place_print()
    goto_next = raw_input("I'll go to number: ")
    print goto_next


def place_print():
    places = ["The Gift Shop", "The Reindeer Stables", "The Landing Strip"]
    for place in places:
        return place


# def north_pole():
#

start()

"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
"""

from sys import exit
visited_north_pole = 0

def north_pole():
    """This is the start of the adventure, The North Pole"""

    global visited_north_pole
    north_pole_places = ["The Gift Shop", "The Reindeer Stables", "The Base"]

    if visited_north_pole == 0:
        print "You are at the start of your adventure! \n "
        print "\tYou are Santa Claus, ready to go hand out gifts to the world!"
        print "\tYou are at your base, the North Pole."
        visited_north_pole += 1
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
        north_pole()

    else:
        print "That's not a place on the North Pole!"
        print "Please answer with a number from the list."
        goto_next = raw_input("I'll go to number: ")
        select__north_pole_place(goto_next)


def gift_shop():
    print "\n\nYou are at the Gift Shop!"
    print "You see thousands of little elves slaving away"
    print "One of them takes a look at you and says:"
    print "\t'Hey Santa!'"
    print "Do you:\n\t1: Slap him\n\t2:Hug him"
    elf_action = raw_input("Select #: ")

    while elf_action == "1" or elf_action == "2":
        if elf_action == "1":
            print "\n\n***************************************************"
            print "***************************************************"
            print "Bad santa!"
            quit("You aren't fit to be santa!")
        elif elf_action == "2":
            print "\nYou hug the little slave and then head back to base"
            print "***************************************************"
            print "***************************************************"
            north_pole()
    gift_shop()



def reindeer_stables():
    print "\n\nYou are at the Reindeer Stables!"
    print "Dasher, Dancer, Prancer, Vix.. ah, fuck it, are waiting for you to take the reigns and go!"
    print "Where do you want to go:"
    print "Do you go to:\n\t1: Sweden\n\t2:Ethiopia"
    action = raw_input("Select #: ")

    while action == "1" or action == "2":
        if action == "2":
            print "\n\n***************************************************"
            print "***************************************************"
            print "Silly santa!"
            quit("Santa doesn't visit poor children!")
        elif action == "1":
            print "\nYou whip the reindeer into a frenzy and go to Sweden!"
            print "***************************************************"
            print "***************************************************"
            sweden()
    sweden()


def sweden():
    print "You are in Sweden!"
    print "You hand out gifts to all the little kids in Sweden and \nreturn home in time for dinner!"
    quit("Enjoy the rest of christmas!")


def quit(why):
    print why, "\nBye!"
    exit(0)

north_pole()

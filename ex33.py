# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is % d" % i
#
# print "The numbers: "
#
# for num in numbers:
#     print(num)

def printstuff(iterations, increments):
    i = 0
    numbers = []
    while i < iterations:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increments

        print "Numbers now: ", numbers
        print "At the bottom i is % d" % i

    for num in numbers:
        print(num)


printstuff(10, 2)

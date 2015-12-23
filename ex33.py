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

def printstuff(start, stop, increments):
    numbers = []
    for i in range(start, stop + 1, increments):
        print "At the top i is %d" % i
        numbers.append(i)

        i += increments

        print "Numbers now: ", numbers
        print "At the bottom i is % d" % i

    for num in numbers:
        print(num)


printstuff(1, 10, 1)

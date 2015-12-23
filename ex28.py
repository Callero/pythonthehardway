def testresult(qnum, qtest, isay):
    compsays = qtest
    if compsays == isay:
        return qnum, "Correct!"
    else:
        return qnum, "Wrong!"


print testresult(1, True and True, True)
print testresult(2, False and True, False)
print testresult(3, 1 == 1 and 2 == 1, False)
print testresult(4, "test" == "test", True)
print testresult(5, 1 == 1 or 2 != 1, True)
print testresult(6, True and 1 == 1, True)
print testresult(7, False and 0 != 0, False)
print testresult(8, True or 1 == 1, True)
print testresult(9, "test" == "testing", False)
print testresult(10, 1 != 0 and 2 == 1, False)
print testresult(11, "test" != "testing", True)
print testresult(12, "test" == 1, False)
print testresult(13, not (True and False), True)
print testresult(14, not (1 == 1 and 0 != 1), False)
print testresult(15, not (10 == 1 or 1000 == 1000), False)
print testresult(16, not (1 != 10 or 3 == 4), False)
print testresult(17, not ("testing" == "testing" and "Zed" == "Cool Guy"), True)
print testresult(18, 1 == 1 and not ("testing" == 1 or 1 == 0), True)
print testresult(19, "chunky" == "bacon" and not (3 == 4 or 3 == 3), False)
print testresult (20, 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"), False)

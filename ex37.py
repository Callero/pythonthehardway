############################################
# print "Try 'del'"
# a = ["first", "second"]
# print "before del"
# print a
# print "del a[0]"
# del a[0]
# print a
#################################################
# print "try 'while'"
# print "while a < 5 print value"
# a = 0
# while a < 5:
#     print a
#     a += 1
###############################################
# import unittest
#
# print "try 'assert'"
#
# def KelvinToFahrenheit(Temperature):
#    assert (Temperature >= 0),"Colder than absolute zero!"
#    return ((Temperature-273)*1.8)+32
#
# print KelvinToFahrenheit(273)
# print int(KelvinToFahrenheit(505.78))
# print KelvinToFahrenheit(-5)
############################################
# g = lambda x: x-2
# print g(8)
###########################################
# print "testing\atesting"
######################################################
# def parent(num):
#     print "Printing from the parent() function"
#
#     def first_child():
#         return  "Printing from the first_child function"
#
#     def second_child():
#         return "Printing from the second_child function"
#
#     try:
#         assert num  == 10
#         return first_child
#     except AssertionError:
#         return second_child
#
# foo = parent(10)
# bar = parent(20)
#
# print foo
# print bar
#
# print foo()
# print bar()
#####################################################
# import time
#
# def timing_function(some_function):
#
#     """
#     Outputs the time a function takes
#     :param some_function:
#     :return:
#     """
#
#     def wrapper():
#         t1 = time.time()
#         some_function()
#         t2 = time.time()
#         return "Time it took to run the function: " + str((t2-t1)) + "\n"
#     return wrapper
#
# @timing_function
# def my_function():
#     num_list = []
#     for x in (range(0,10000)):
#         num_list.append(x)
#     print "\nSum of all the numbers: " +str((sum(num_list)))
#
#
# print(my_function())
#######################################################
# from time import sleep
#
# def sleep_decorator(function):
#
#     """
#     Limits how fast the function is called.
#     :param function: Takes a function as input
#     :return: The function slower
#     """
#
#     def wrapper(*args, **kwargs):
#         sleep(2)
#         return function(*args, **kwargs)
#     return wrapper
#
# @sleep_decorator
# def print_number(num):
#     return num
#
# print print_number(222)
#
# for x in range(1,6):
#     print print_number(x)
#############################################

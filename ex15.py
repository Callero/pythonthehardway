# # Imports module
# from sys import argv
#
# #arguments for command line
# script, filename = argv
#
# #a variable called 'txt' that contains the filename from the command line
# txt = open(filename)
#
# #prints the file name from argv
# print "Here's your file %r:" % filename
# #reads and prints the 'txt' variable
# print txt.read()

print "Type the filename again:"
#fetching the file name
file_again = raw_input("> ")

#a variable that opens the file
txt_again = open(file_again)

#prints the file contents
print txt_again.readline()

txt_again.close()



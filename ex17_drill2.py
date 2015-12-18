from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

if (exists(to_file) == True):
    out_file = open(to_file, 'w')
    out_file.write(indata)
    out_file.close()
    in_file.close()
else:
    print "No such out file"
    exit()

print "Alright, all done."



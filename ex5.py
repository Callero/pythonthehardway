my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 178 # cm
my_weight = 93 # kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'
my_weight_lbs = my_weight * 2.2046
my_height_inch = my_height * 0.3937
print "Let's talk about %s." % my_name
print "He's %d cm's (%d inch) tall" % (my_height, my_height_inch)
print "He's %d kg (%d lbs) heavy" % (my_weight, my_weight_lbs)
print "Actually pretty heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are actually %s depending on the coffee" % my_teeth

#Tricky line
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

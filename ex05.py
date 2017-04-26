# -*- coding: utf-8 -*-
# String var
name = "Zed A. Shaw"
#String int
age = 35 # not a lie
height = 74 # inches
#String float
height_cm = height * 2.54 # cm
weight = 180.0 # lbs
weight_kg = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Inserting a string as a variable into another string, as specified by %s conversion type
print "Let's talk about %s." % name
#Inserting decimal into string, using %d conversion type
print "He's %d inches tall." % height
print "He's %d cm tall." % height_cm
#string variable converted from float to decimal
print "He's %d pounds heavy." % weight
print "He's %d kilograms heavy." % weight_kg
print "Actually that's not too heavy."
# String takes two arguments, so values need to be in a tuple
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (
    age, height, weight, age + height + weight)
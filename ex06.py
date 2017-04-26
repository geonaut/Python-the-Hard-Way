# String variable containing modulo operator (%) with decimal integer conversion type specified (d). If the string requires a single argument, values may be a single non-tuple object.
x = "There are %d types of people." % 10
# A simple string
binary = "binary"
do_not = "don't"
# 2 arguments, so values in a tuple
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
#Using the repr() string conversion type, to insert a printable version of an object (aka with '')
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Indirectly inserting %r conversion type into string. No quotes, as var is bool.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#Using concatenation operator
print w + e
from sys import argv
#argv again
script, user_name = argv
# defining the prompt
prompt = '> '
#Needs args to start
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
#asking for input within the script
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)
#Print it out as a block
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
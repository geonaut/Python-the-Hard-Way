from sys import argv

script, filename = argv

#calling open function
txt = open(filename)

print "Here's your file %r:" % filename
#reading file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
#closing the files
txt.close()
txt_again.close()

#Using tab character
tabby_cat = "\tI'm tabbed in."
#Using newline
persian_cat = "I'm split\non a line."
#escaping backslashes
backslash_cat = "I'm \\ a \\ cat."
#using a block, plus tabs and newline
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Creates a infinite loop spinner
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
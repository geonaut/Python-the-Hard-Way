#Define a var as 4 repr() string formatters
formatter = "%r %r %r %r"

#print var, inserting tuple of integers. No quotes for repr(int)
print formatter % (1, 2, 3, 4)
#print var, inserting tuple of strings. Quotes for repr(str)
print formatter % ("one", "two", "three", "four")
#print var, using tuple of booleans. No quotes for repr(bool)
print formatter % (True, False, False, True)
#print var using tuple of strings, as variables, but not evaluating the variables. Quote, as it effectively repr(str).
print formatter % (formatter, formatter, formatter, formatter)
#printing strings on same line, but still using repr(str)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
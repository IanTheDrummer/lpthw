from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Line 1 imports an argument.
# Line 2 Does nothing.
# Line 3 Has an argument. This argument makes you select a file and write out the filename when you open ex15.py
# Line 4 Opens the file you mentioned in the argument.
# Line 5 Does Nothing.
# Line 6 Prints text and opens your file.
# Line 7 Prints your file text.
# Line 8 Does nothing.
# Line 9 Prints text.
# Line 10 Uses raw_input.
# Line 11 Does Nothing.
# Line 12 Open the file again.
# Line 13 Prints your file text.
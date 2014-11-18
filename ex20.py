from sys import argv

script, input_file = argv

def print_all(f):
	print f.read
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Line 1 import an argument
# Line 2 does nothing
# Line 3 edits the argument
# Line 4 does nothing
# Line 5 defines a function
# Line 6 prints text
# Line 7 does nothing
# Line 8 defines a function
# Line 9 seeks
# Line 10 does nothing
# Line 11 defines a function
# Line 12 prints and reads
# Line 13 does nothing
# Line 14 combines?
# Line 15 does nothing
# Line 16 prints and has a linefeed
# Line 17 does nothing
# Line 18 combines?????????????????????
# Line 19 does nothing
# Line 20 prints
# Line 21 does nothing
# Line 22 combines????????????????????
# Line 23 does nothing
# Line 24 prints
# Line 25 does nothing
# Line 26 through 33 prints 3 lines
# Line 34 does nothing
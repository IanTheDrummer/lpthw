from sys import argv

script, filename = argv

txt = open(filename)

print "Are you ready for your file?"
print "Okay, here's your file %r:" % filename
print txt.read()

answer = raw_input("Are you happy now? ")

print "You said %r about being happy." % (answer)
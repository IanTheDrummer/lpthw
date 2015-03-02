people = 40
ninja = 50
cops = 30

print "The world is at stake! Ninjas are everywhere trying to kill the people!"

if people > cops:
	print "The people join forces with the cops and are prepared to fight the ninjas!"
else:
	print "The people can fight their own battles"
	
if ninja > cops:
	print "Will the people retaliate? Yes or No?"
	
	answer = raw_input("> ")
	
	if answer == "yes":
		print "The people are slaughtered by the ninjas!"
	if answer == "no":
		print "The cops are out skilled and out numbered by the ninjas. They are all killed!"
# This is giving the value of people
people = 30
# This is giving the value of cars
cars = 40
# This is giving the value of buses
buses = 15

# This is saying that if cars > people is true, that it will print something.
if cars > people:
	print "We should take the cars."
# This is saying that if the upper statement isn't true to try this one.
elif cars < people:
	print "We should not take the cars."
# This is saying that if all of the upper statements still aren't true, to try this final one out.
else:
	print "We can't decide."
# This is saying that if buses > cars is true, that it will print something.
if buses > cars:
	print "That's too many buses."
# This is saying that if the upper statement isn't true to try this one.
elif buses < cars:
	print "Maybe we could take the buses."
# This is saying that if all of the upper statements still aren't true, to try this final one out.
else:
	print "We still can't decide."
# This is saying that if people > buses, that it will print something.
if people > buses:
	print "Alright, let's just take the buses."
# This is saying that if the upper statement isn't true, to try this one.
else:
	print "Fine, let's stay home then."
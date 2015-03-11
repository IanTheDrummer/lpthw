print "You enter a dark room with two doors. Do you go through door #1 or #2 or #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
bear = raw_input("> ")

if bear == "1":
	print "The bear eats your face off. Good Job!"
elif bear == "2":
	print "The bear eats your legs off. Good Job!"
else:
	print "Well, doing %s is probably better. Bear runs away." % bear
	
if door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow Jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insantiy == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
else:
	print "You stumble around and fall on a knife and die. Good job!
	
if door == "3":
	print "You've found 100,000,000 dollars! What will you spend it on?"
	print "1. A Ferrari."
	print "2. A Banana."
	print "3. Funding Iona Community."
	
	money = raw_input("> ")
	
	if money == "1":
		print "You end up wrecking the car in the dealership parking lot. Good Job!"
		
	elif money == "2":
		print "A nearby bear finds you and steals you banana. Good Job!"
	else money == "3":
		print "The money turns Iona into a million dollar company and they get robbed causing Father Bob to join Al Queda and suicide bomb everyone in the church."
		
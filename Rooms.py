from sys import exit
from random import randint

class Room(object):

	def enter(self):
		print "Blah blah blah."
		exit(0)

class Startup(Room):

	def enter(self):
		print "Welcome to The Dark Corridor! Would you like instructions? Y or N?"
		
		answer = raw_input("> ").lower()
		
		if answer == "y":
			print "The Dark Corridor is an adventure style game filled with tricks,"
			print "secrets, and lots of fun. Your main objective is to get out of"
			print "this crazy dark corridor. Along the way you will face lots of bad guys"
			print "and other assorted creatures! Now jump on it and have some fun!"
			return 'corridor'
			
		elif answer == "n":
			return 'corridor'
			
		else:
			print "I don't understand that."
			return 'startup'
		
class Death(Room):
	def enter(self):
		print "Wow... you died. I've seen old people do better."
		print "You better have the money for your funeral."
		print "\n-----------"
		exit(0)
		
class Corridor(Room):

	def enter(self):
		print "You stand in a dark corridor filled with endless rows of doors."
		print "To your left sits a door marked KEEP OUT. To your right sits a"
		print "door marked, CAUTION WET INTERIOR. In front of you lies an endless"
		print "corridor with nothing but doors. So... what will you do?"
		
		answer = raw_input("> ").lower()
		
		if answer == "left":
			return 'panda'
			
		elif answer == "right":
			return 'ocean'
			
		elif answer == "forward":
			print "You fall down an endless abyss."
			return 'death'
			
		elif answer == "kill":
			print "You slam your own head in the doorway and fall over whilst foaming"
			print "at the mouth. You then see a bright light and join the angels."
			return 'death'
			
		elif answer == "run":
			print "You run down the corridor and lose 90 lbs. in the process."
			print "After that you join a body building club and live a happy"
			print "life, at least until you take too many steroids and your"
			print "biceps explode."
			print "---------------"
			exit(0)

		elif answer == "yell":
			print "You yell into the darkness and nothing happens."
			return 'corridor'
			
		else:
			print "I don't understand that."
			return 'corridor'
		

class Panda(Room):

	def enter(self):
		print "You slowly open the door and stand frozen in terror."
		print "A gigantic panda sits in a corner in front of you eating"
		print "it's ways through a small child. Behind it sits a door."
		print "as you ponder kissing the panda you realize that the door"
		print "could be your way out. So what will you do?"
		
		answer = raw_input("> ").lower()
		
		if answer == "kill":
			print "You charge at the panda with pure hatred! Sadly, he"
			print "snatches you and rips you in two."
			return 'death'
		
		elif answer == "forward":
			print "You can't move forward you fat dirtbag, there is a"
			print "big bloody panda before you."
			return 'panda'
			
		elif answer == "run":
			print "You turn on a dime and try to escape. The door is locked."
			print "Then the panda grabs you and rips you in two."
			return 'death'
			
		elif answer == "talk":
			print "You scream with all your might at the fat panda and he"
			print "grabs you and rips you in two."
			return 'death'
			
		else:
			print "I don't understand that."
			return 'panda'
			
			
class Ocean(Room):
	
	def enter(self):
		print "As you open the door, you smell the sea and feel mist blow onto"
		print "your ugly mug. Then without warning, the floor beneath you opens"
		print "and you fall into an ocean. You can only last so long in the cold"
		print "water. So, what will you do?"
		
		answer = raw_input("> ").lower()
		
		if answer == "forward":
			print "There's no where to go you fat dirtbag, YOUR IN THE OCEAN!"
			return 'ocean'
			
		elif answer == "kill":
			print "You tie your hands together with your shoelaces and sink"
			print "to the ocean floor. Five seconds later you glance up at"
			print "the golden light seeping through the crystal clear water"
			print "as you slowly drown."
			return 'death'
			
		elif answer == "swim":
			print "You swim for miles and eventually realize that there is no hope."
			print "Will you give up?"
			
			a = raw_input("> ").lower()
			
			if a == "no":
				print "You continue to swim and eventually come across a lonely"
				print "fisherman in his tiny boat. He offers you help and sails"
				print "you to shore where you find a small house."
				return 'ghost'
				
			elif a == "yes":
				print "You tie your hands together with your shoelaces and sink"
				print "to the ocean floor. Five seconds later you glance up at"
				print "the golden light seeping through the crystal clear water"
				print "as you slowly drown."
				return 'death'
				
		elif answer == "yell":
			print "You continue to swim and eventually come across a lonely"
			print "fisherman in his tiny boat. He offers you help and sails"
			print "you to shore where you find a small house."
			return 'ghost'
			
		else:
			print "I don't understand that."
			return 'ocean'
			
	
class Ghost(Room):
	
	def enter(self):
		print "You enter the house and decide to explore for a while."
		print "After your brief exploration, you settle down for a few days."
		print "On the fifth day, you hear a creak in the basement. Will you"
		print "go check it out or stay here?"
		
		answer = raw_input("> ").lower()
		
		if answer == "check":
			return 'minion'
			
		elif answer == "stay":
			print "The creaking sound is growing louder... your really should check."
			
			answer = raw_input("> ")
			
			if answer == "check":
				return 'minion'
			
			elif answer == "stay":
				print "OH NO! That creaking sound was a banshee from the underworld! It"
				print "has come for your soul. The floor beneath you splits open and"
				print "you fall down through the earth's crust into the underworld!"
				return 'death'
				
		else:
			print "I don't understand that."
			return 'ghost'
				
			
class Minion(Room):

	def enter(self):
		print "You walk to the basement entrance as a shiver runs down your spine. As you"
		print "walk down the steps and hear a voice in the darkness beckoning you."
		print "You finally finish your descent down the stairs and see the abomination"
		print "before you. It is a banshee. 'YOU WILL DIE' screams the banshee as it lunges"
		print "towards you. Quickly, what will you do?"
		
		answer = raw_input("> ").lower()
		
		if answer == "kill":
			print "A magic sword appears out of thin air into your hands as you stab the screaming"
			print "banshee directly into the heart. As you see the light fade from his eyes"
			print "he mutters,'FADAFINGLING WILL DESTROY YOU'. Then, the floor beneath you"
			print "splits open and you fall down through the earth's crust into the underworld"
			return 'cell'
			
		elif answer == "talk":
			print "With a sly attitude you yell,'NOT EVEN YOUR MOTHER COULD LOVE THAT FACE'."
			print "Instantly, the banshee flies into your soul and tears it apart! As you die"
			print "you hear the voices of thousands of dead souls laughing at you."
			return 'death'
			
		elif answer == "run":
			print "With haste you try and run back up the stairs but the banshee files into your"
			print "worthless soul and tears it apart! As you die you hear the voices of"
			print "thousands of dead souls laughing at you!"
			return 'death'
			
		elif answer == "forward":
			print "You can't go forward you idiotic dirtbag there is a banshee in front of you!"
			return 'minion'
			
		else:
			print "I don't understand that."
		

class Cell(Room):

	def enter(self):
		print "You wake up in a cold smelly jail cell. The impact must've knocked you out."
		print "You try and peak out the bars of the jail cell and see nothing but a small"
		print "empty hallway. There must be some way out. There is an axe nearby and a keypad"
		print "on the lock."
		
		q = raw_input("> ")
		
		if q == "axe":
			print "You smash the axe at the keypad but nothing happens."
			return 'cell'
			
		elif q == "keypad":
			print "You examine the keypad and see that there are numbers."
			print "This could be your way out, you just need to figure out the stupid code."
			print "So what could that single-digit lucky number be?"
			
			correct_number = randint(1,9)
			guess = raw_input("> ")
			
			if int(guess) != correct_number:
				print "You press the button %s and the keypad explodes instantly kills you." % guess
				return 'death'
				
			else:
				print "You press the button %s and the keypad unlocks opening the cell door." % guess
				return 'fadafingling'
				
			
class Fadafingling(Room):

	def enter(self):
		print "With haste you run out the cell and down the hallway until you come upon strange portal."
		print "It glows purple and looks oddly edible. What will you do?"
		
		answer = raw_input("> ")
		
		if answer == "enter":
			print "You instantly vaporize when you touch the portal."
			return 'death'
			
		elif answer == "stay":
			print "You go mad at the wonderful sight of the portal and eventually eat yourself."
			return 'death'
			
		else:
			print "I don't understand that."
			return 'fadafingling'
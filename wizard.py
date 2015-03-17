from sys import exit

def dead(why):
	print why, "THE END!"
	exit(0)
	
def start():
	print "THE WANDERING WIZARD"
	print "--------------------"
	print "WELCOME! WOULD YOU LIKE INSTRUCTIONS? Y OR N?"
	
	answer = raw_input("> ")
	
	if answer == "y":
		print "THERE ARE MANY DIFFERENT DESTINATIONS AND PLACES YOU WILL GO TO."
		print
		print "YOU CAN SIMPLY TYPE L OR R TO GO EITHER LEFT OR RIGHT."
		print
		print "HOWEVER, YOU WILL NOT KNOW WHICH PATH WILL LEAD TO DECONSTRUCTION AND DEATH!"
		print
		print "HAVE FUN!"
		print
		print "----------------------------------------------------------------------------"
		
		forest_1()

	if answer == "n":
		forest_1()
		
def forest_1():
	print "YOU ARE A WANDERING WIZARD BY THE NAME OF GANDALF!"
	print
	print "YOU DESPERATELY WANT TO GET TO THE SHIRE, BUT YOU ARE LOST. THERE IS A FORK IN THE ROAD YOU ARE TRAVELLING."
	print
	print "WILL YOU GO LEFT OR RIGHT?"
	print
	
	answer = raw_input("> ")
	
	if answer == "l":
		path1()
		
	if answer == "r":
		forest2()
		
def path1():
	print "YOU ARE ON A PATH THAT YOU HAVE NEVER SEEN BEFORE..."
	print
	print "THERE IS A STRANGE GLOW IN THE DISTANCE. WILL YOU CONTINUE ON OR CHECK THE GLOW?"
	print
	
	answer = raw_input("> ")
	
	if answer == "check":
		lava()
		
	if answer == "continue":
		tunnels()
		
def forest2():
	print "OH NO! THERE ARE GOBLINS ON THE PATH! WILL YOU FIGHT THEM?"
	print
	
	answer = raw_input("> ")
	
	if answer == "y":
		print "YOU CLASH SWORDS AND YOU GET THE UPPER HAND BY USING YOUR MAGIC!"
		print
		blackgate()
		
	if answer == "n":
		dead("YOU ARE SLAUGHTERED ON THE SPOT.")

def lava():
	dead("YOU REALIZE THAT THE GLOW WAS LAVA AND ACCIDENTAL SLIP AND FALL IN.")

def tunnels():
	print "YOU TRAVEL LONG AND FAR AND SEE A MASSIVE TUNNEL."
	print
	print "YOU DECIDE TO GO IN AND FIND OUT THAT IT'S A GOBLIN TUNNEL!"
	print
	print "THE PLACE SMELLS AND IS RIDDLED WITH GOBLINS."
	print
	print "WILL YOU TRY AND ESCAPE?"
	print
	
	answer = raw_input("> ")
	
	if answer == "n":
		dead("YOUR AN IDIOT. THE GOBLINS TURN YOU INTO WIZARD JELLY.")
	
	if answer == "y":
		print "YOU USE YOUR POWER OF WITS AND MAGIC TO ESCAPE AND COME UPON ANOTHER PATH."
		print
		path3()
		
def path3():
	print "YOU ARE GREETED BY THE FRIENDLY FACE OF FRODO BAGGINS!"
	print
	print "YOU CAN KILL HIM OR TALK TO HIM OR IGNORE HIM."
	print
	
	answer = raw_input("> ")
	
	if answer == "kill":
		print "YOUR BEST FRIEND IS NOW DEAD ON A DIRT PATH BECAUSE OF YOU. YOU SLIMY DIRTBAG."
		print
		wtop()
	
	elif answer == "talk":
		print "You: HI MY WEE LAD! I WAS JUST ON MY WAY TO THE SHIRE!"
		print
		print "Frodo: AAH! GANDALF, I THINK YOU SHOULD KNOW THAT I AM ON A SIMILAR QUEST OF REACHING THE SHIRE SAFELY!"
		print
		print "You: TELL ME... IS THERE ANYTHING STRANGE NEARBY?"
		print
		print "Frodo: WHY YES! THERE IS A MASSIVE ORC ON WEATHERTOP ROCK NOT A HALF A MILE FROM HERE!"
		print
		print "You: TAKE CAUTION MY BOY. I WILL SEE TO IT THAT THE ORC TAKES IT FINAL BREATH!"
		print
		wtop()
			
	else: 
		if answer == "ignore":
			print "YOU BRUSH PAST FRODO WITH VIGOUR AS HE STARES AT YOU IN SHOCK!"
			print
			wtop()
			
def blackgate():
	print "A DREADFUL SHADOW PASSES OVER YOU AS YOU COME UPON THE BLACK GATE!"
	print
	print "YOU SHOULD PROBABLY CONTINUE ON, BUT IF YOU THINK YOU HAVE THE SKILL SET, YOU CAN ENTER AND FIGHT OFF THOUSANDS OF ORCS!"
	print
	
	answer = raw_input("> ")
	
	if answer == "continue":
		print "YOU TREK DOWN A PATH AND SPOT IN THE DISTANCE THE MYSTERIOUS WEATHERTOP ROCK!"
		wtop()
		
	else: 
		if answer == "enter":
			dead("YOU ARE THE DUMBEST HUMAN IN EXISTENCE. YOU STOOD NO CHANCE AND WERE BEHEADED.")
	
def	wtop():
	print "AS YOU CLIMB UP THE ROCK TO SEEK SHELTER, YOU SEE AZOG THE DEFILER!"
	print
	print "AZOG: MWA HA HA! I'VE BEEN WAITING FOR YOU, WIZARD FILTH!"
	print
	print "TERROR RUNS THROUGH YOUR BONES... WILL YOU FACE HIM?"
	
	answer = raw_input("> ")
	
	if answer == "y":
		battle()
		
	if answer == "n":
		print "AZOG: NOT SO FAST!"
		print
		dead("HE GRABS YOU AND RIPS YOU IN TWO!")

def battle():
	print "YOU STARE WITH IMMENSE HATRED TOWARDS YOUR FOE."
	print
	print "AZOG: YOU WILL MEET YOUR END!"
	print 
	print "YOU: I THINK YOU UNDERESTIMATE MY ABILITIES, ORC!"
	print
	health()
	
def health():
	azog = 10
	you = 10
	
	print "YOU CAN USE MULTIPLE ATTACKS."
	print
	print "THEY EACH DO DIFFERENT DAMAGE LEVELS."
	print
	print "TYPE THE COMMANDS S OR W."
	print
	print "FIGHT!"
	
	attack = raw_input("> ")
	
	if attack == "s":
		print "AZOG NOW ONLY HAS 50 PERCENT HEALTH!"
		print
		azog = 5
	else:
		if attack == "w":
			print "AZOG HAS NOW ONLY 20 PERCENT HEALTH!"
			print
			azog = 2
			
	print "AZOG SLASHES AT YOU AND LEAVES YOU WITH 40 PERCENT HEALTH!"
	print 
	print "BUT YOU GET BACK TO YOUR FEET. KEEP FIGHTING!"
	print
	you = 4
	
	attack = raw_input("> ")
	
	if attack == "w":
		you = 0
		
	if attack == "s":
		azog = 0
		
	if azog == 0:
		win_end()
	
	if you == 0:
		dead("YOUR MAGIC POWERS FADE AS YOU TRY TO ATTACK AND AZOG STABS YOU!")

def win_end():
	print "YOU SLAY AZOG AND RETURN TO THE SHIRE!"
	print
	print "THE END!"
	print 
	print "Creator: Ian Edwards"
	print
	print "Co-Creator: Ian Edwards"
	print
	print "Produced by: Edwards Studios"
	print
	print "Funded by: Some spare change"
	print
	print "Copyright. 2015 Edwards Studios Inc. All Rights Reserved."
	print
	
start()
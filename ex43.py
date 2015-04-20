from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This is a blank scene that needs love..."
		exit(0)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        selected_scene = scene.map.first_scene()
		
	while True:
		print "************"
		next_scene = selected_scene_scene.enter()
		selected_scene = self.scene_map.next_scene

class Death(Scene):

	def enter(self):
		print "You are now dead... you call that effort?"
		exit(0)

class CentralCorridor(Scene):

    def enter(self):
			print "In front of you stands the one Gorthon from Planet Percal #25"
			print "that killed all of your loved ones. You seek revenge but are also"
			print "strongly aware of your current duties. The space station told you"
			print "to find the neutron bomb and blow up the Gorthon's ship and finally"
			print "to leave in the escape pod before time runs out."
			print None
			print "You then realize that the Gorthon in front of you is defending the Weapons Armory."
			print "You could rush the Gorthon and try to slip past him and get to the door, or you could"
			print "just shoot him. As you ponder the two ideas, the Gorthon pulls his laser sword on you!"
			print "Will you shoot him or rush him?"
			print None
		
			answer = raw_input("> ")
		
			if answer == "shoot":
				print "With a Clint Eastwood glint in your eye, you shoot that fat sucker right"
				print "in the heart! You take a quick break and throw back a celebratory shot!"
			
			return 'armory'
			
			elif answer == "rush":
				print "With all your might, you charge straight at the fat Gorthon, only to be"
				print "sliced clean in two by the Gorthon's massive sword."
			
				return 'death'
			
			else:
				print "I do not know what that means..."
				return 'corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "Into the armory you walk and you go search for the neutron bomb."
		print "You find it! But, then you start wondering if you should really blow up"
		print "the ship. I mean c'mon, it's a perfectly good ship, and it shouldn't go"
		print "to waste. Will you blow it up or keep the ship for your self?"
		
		answer = raw_input("> ")
		
		if answer == "keep":
			print "You arrogantly strut about the ship whistling Bad To The Bone."
			print "In the midst of your strutting, a stray Gorthon comes up and stabs"
			print "you. See? Selfishness can get you killed!"
			
			return 'death'
			
		elif answer == "blow up":
			return 'bridge'
			
		else:
			print "I do not know what that means..."
			return 'armory'
			

class TheBridge(Scene):

    def enter(self):
		print "You make quick hast towards the bridge with the bomb in your hand."
		print "On the ground, you place the bomb and prime it to blow. The timer"
		print "reads 1:00. That's all the time you'll need to get off this stinking"
		print "tin can. *BEEP* goes the timer as the countdown starts..."
        
		return 'pod'

class EscapePod(Scene):

    def enter(self):
		print "Your feet smack the cold hard floor as you race to the escape pod."
		print "When you reach the escape pod station, you see that there are multiple"
		print "pods! Sadly, there is a possibility that some of them could be ruined."
		print "There are 10 pods which gives you a 10 to 1 chance of choosing the"
		print "correct pod. So, what pod will you choose?"
		
		safe_pod = randint(1, 10)
		answer = raw_input("[pod #]> ")
		
		if int(answer) != safe_pod:
			print "You climb into pod %s and hope for the best." % answer
			print "You press the eject button and your body is overwhelmed"
			print "with G-force. You pass out almost instantly, and your pod"
			print "is crushed into oblivion."
			
			return 'death'
			
		else:
			print "You climb into pod %s and hope for the best." % answer
			print "You sit back and relax in your luxury pod and smoothly"
			print "drift away from the ship. Champaign suddenly apears out"
			print "of a small port, and you celebrate your success!"
			
			return 'finished'

			
class Map(object):

	scene_order = {
		'corrider': CentralCorridor(),
		'armory': LaserWeaponArmory(),
		'bridge': TheBridge(),
		'pod': EscapePod(),
		'death': Death()
	}

    def __init__(self, start_scene):
		self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
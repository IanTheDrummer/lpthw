import Rooms

class Map(object):

	rooms = {
		'corridor': Rooms.Corridor(),
		'startup': Rooms.Startup(),
		'death': Rooms.Death(),
		'panda': Rooms.Panda(),
		'ocean': Rooms.Ocean(),
		'ghost': Rooms.Ghost(),
		'minion': Rooms.Minion(),
		'cell': Rooms.Cell(),
		'fadafingling': Rooms.Fadafingling()
	}
	
	def __init__(self, start_room):
		self.start_room = start_room
		
	def next_room(self, room_name):
		return Map.rooms[room_name]
		
	def get_start_room(self):
		return self.next_room(self.start_room)
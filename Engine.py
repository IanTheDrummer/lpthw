class engine(object):

	def __init__(self, room_map):
		self.room_map = room_map
		
	def play(self):
		current_room = self.room_map.get_start_room()
		
		while True:
			print "\n-----------"
			next_room_name = current_room.enter()
			
			if next_room_name is None:
				print "I don't understand that..."
				continue
				
			current_room = self.room_map.next_room(next_room_name)
			

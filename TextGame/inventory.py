

class Inventory(object):

	def __init__(self, slots={}):

		self.slots = slots
	
	def bag(self):
	
		self.slots = {
                              'slot 1':0,
                              'slot 2':0,
                              'slot 3':0		      
                     }
		
		sorted = self.slots.items()
		sorted.sort()
		for k, v in sorted:
			print k, v
		
		return ' '
	




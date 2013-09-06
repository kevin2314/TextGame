from collections import OrderedDict

class Inventory(object):

	def __init__(self, slots={}):

		self.slots = slots
	
	def bag(self):
	
		self.slots = {
                              'slot 1':0,
                              'slot 2':0,
                              'slot 3':0		      
                     }
		
		sort = sorted(self.slots.items())
		
		for k, v in sort:
			print(k, v)
		
		return ' '
	




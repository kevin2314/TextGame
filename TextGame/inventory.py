import json

def get_inventory(id):
	ret = None
	with open('TextGame/inventory/1.json', 'r') as f:
		jsontext = f.read()
		d = json.loads(jsontext)
		d['id'] = id
		ret = Inventory(**d)
	return ret

class Inventory():
	
	def __init__(self, id=0, name='Item', description='''An empty 
	slot''', count=[]):
		self.id = id
		self.name = name
		self.description = description
		self.count = count
	
	def inventory(self):
		return self._count('inventory')
	

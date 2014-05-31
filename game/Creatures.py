

class Monster(dict):
		
	def __missing__(self, key):
		return key
		

print('{name}, {level}, {height}, {attack}'.format_map(Monster(name="kevin", level=20, height=45, attack=20)))


import cmd
from room import get_room
import textwrap



class Game(cmd.Cmd):
	def __init__(self):
#-----------------------------------------------------------------------
#Here the game is initialized asking for commands via the Cmd module,
#the variables given are the first room you start in and prints out the
#location
		
		cmd.Cmd.__init__(self)
		
		
		self.loc = get_room(6)
		self.look()
		
#-----------------------------------------------------------------------		
#This checks which room you are in if you can go the way for the command
#given and prints out your location 		
	
	def move(self, dir):
		newroom = self.loc._neighbor(dir)
		if newroom is None:
			print('''You cannot go this away''')
			self.look()
		else:
			self.loc = get_room(newroom)
			self.look()
	def climb(self, dir):
		newroom = self.loc._neighbor(dir)
		if newroom is None:
			print('there is nothing to climb here')
			self.look()
		else:
			self.loc = get_room(newroom)
			self.look()
	def look(self):
		print(self.loc.name)
		print('')
		for line in textwrap.wrap(self.loc.description, 72):
			print(line)
		
	
		
#-----------------------------------------------------------------------		
#commands		
	
	def do_n(self, args):
		'''goes north'''
		self.move('n')
	
	def do_s(self, args):
		'''goes south'''
		self.move('s')	
	
	def do_e(self, args):
		'''goes east'''
		self.move('e')
			
	def do_w(self, args):
		'''goes west'''
		self.move('w')
	
	def do_climb(self, args):
		'''Climbs where possible'''
		self.climb('climb')
	
	def do_enter(self, args):
		'''Enters rooms, Villages, and caves where possible'''
		self.move('enter')
	
	def do_smithy(self, args):
		'''Enters Blacksmith'''
		self.move('blacksmith')
		
	def do_mine(self, args):
		'''COllects items from mineable points'''
		self.action(mine)
	
	def do_forge(self, args):
		'''For forging command at the blacksmith'''
		self.action(forge)
	
	def do_leave(self, args):
		'''Exits the current room'''
		self.move('leave')
		
				
	def do_quit(self, args):
		'''Quits the game'''
		print("thank you for playing")
		return True

			
		



				
if __name__ == '__main__':
	g = Game()
	g.cmdloop()
	

		
	

	
		

from inventory import Inventory


class Player(object):
	
	def __init__(self):
		self.inv = Inventory()

#Naming your player for a nice personal toouch, when saving is implemented
#this will be save as well.
	def player_name(self):
		if self.name == '':
			self.name = input('Would you like to give yourself a name?> ')
			print((self.name))
		else:
			print((('Your name is ' + repr(self.name))))

#The importance what hand you are will be important later on.

	def hand(self, right_hand, left_hand):
		right_hand = " \n"
		left_hand = " \n"	

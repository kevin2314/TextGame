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
            print((('Your name is %s.') % self.name))

#The importance what hand you are will be important later on.

    def right_hand(self, hand):
        self.hand = hand

    def print_hand(self):
        try:
            if self.hand == ' ':
                print('You are not holding anything')
            else:
                print('You are holding %s' % self.hand)
        except:
            return 'There is nothing in hand'
        return ''
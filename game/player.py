from inventory import Inventory


class Player(object):

    def __init__(self, left_hand='', right_hand='', name='', hand=''):
        self.name = name
        self.hand = hand
        self.left_hand = left_hand
        self.right_hand = right_hand

#Naming your player for a nice personal toouch, when saving is implemented
#this will be save as well.
    def player_name(self):
        if self.name == '':
            self.name = input('Would you like to give yourself a name?> ')
            print((self.name))
        else:
            print((('Your name is %s.') % self.name))

#The importance what hand you are will be important later on.
    def hands(self, left_hand='', right_hand=''):
        self.left_hand = ' '
        self.right_hand = ' '
        print(self.left_hand, self.right_hand)


class Actions(Player):

    def __init__(self):
        self.inventory = Inventory()
        self.player = Player()
        #self.hand = self.player.hands()
# for the moment this is disabled, I need to figure a way to check the inventory
# to see if the user inputed item exists and if the quantity > 0 in order to
# set it in the hand function.
    #def get_item(self):
        #while True:
            #src = input('What item would you like to use> ')
            #for i in src:
                #if self.inventory(self.slots[i]):
                    #print('You are now holding %s') % i
                    #self.player.hands(right_hand=i)
                    #return False
                #else:
                    #print('You do not have this item')
                    #return False
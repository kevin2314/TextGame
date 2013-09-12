

class Player(object):

    def __init__(self, left_hand='', right_hand='', name=''):
        self.name = name
        self.left_hand = left_hand
        self.right_hand = right_hand

    def player_name(self):
        if self.name == '':
            self.name = input('Would you like to give yourself a name?> ')
            print((self.name))
        else:
            print((('Your name is %s.') % self.name))

    def hands(self):
        self.left_hand = ' '
        self.right_hand = ' '


class Actions(Player):

    def __init__(self):
        pass
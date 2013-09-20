

from inventory import Inventory
import cmd
from room import get_room
from player import Player
import textwrap
#import time


class Game(cmd.Cmd):
    prompt = '> '

    def __init__(self):
#-----------------------------------------------------------------------
#Here the game is initialized asking for commands via the Cmd module,
#the variables given are the first room you start in and prints out the
#location

        cmd.Cmd.__init__(self)
        self.loc = get_room('intro')
        self.look()
        self.inventory = Inventory()
        self.player = Player()

#------------------------------------------------------------------------
#This checks which room you are in if you can go the way for the command
#given and prints out your location
    def emptyline(self):
        pass

    def objects(self, args):
        objects = self.loc._objects(args)
        if objects is None:
            print(('Ther are no %s in the area' % args))
            self.look()
        else:
            self.look()

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print('''You cannot go this away''')
            self.look()
        else:
            self.loc = get_room(newroom)
            self.look()

    def look(self):
        print((self.loc.name))
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)
        print('')

#-----------------------------------------------------------------------
#commands
#movement

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
        self.move('climb')

    def do_get(self, args):
        '''Gets items from an area or from your bag'''
        if self.inventory.slots[args] > 0:
            self.player.right_hand(args)
        else:
            print('You do not have this item')

    def do_enter(self, args):
        '''Enters rooms, Villages, and caves where possible'''
        self.move('enter')

    def do_leave(self, args):
        '''Exits the current room'''
        self.move('leave')

    def help_get(self):
        for i in (textwrap.wrap('''   If you are trying to grab an item out from
your bag type get followed by the item in your bag, this applys to
items in an area as well''', 72)):
            print(('', i))
#prompts

    def do_chop(self, args):
        self.objects('trees')

    def do_name(self, args):
        '''Prints the users name if there is one'''
        self.player.player_name()

    def do_hand(self, args):
        '''Prints what is in hand'''
        print((self.player.print_hand()))

    def do_next(self, args):
        '''Gets the next event'''
        self.move('next')

    def do_look(self, args):
        '''Prints the current area you are in'''
        self.look()

    def do_inventory(self, args):
        '''Checks Inventory'''
        self.inventory.bag()
        self.look()

    def do_quit(self, args):
        '''Quits the game'''
        print("thank you for playing")
        return True

if __name__ == '__main__':
    g = Game()
    g.cmdloop()
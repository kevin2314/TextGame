

import cmd
from room import get_room
from actions import get_action
import inventory
import textwrap


intro = '''As you come to from a sleep that certaintly didn't feel welcomed,
you notice you are in a strange bed, you think to yourself "This is'nt my bed."
you look around the room and nothing is familiar to you, as you get up the
clothes you wear are not familiar to you eithre, at this point you get up and
stumble out of bed,as you exit the room you notice you are in an inn by the
people around and the obvious clerk at a counter. "Why hello there stranger"
the clerk blurts out in a loud voice, as you look at him he explains "Your
confused look tells me your not from around here... or the fact that the man
who brought you in here said he found you nude beaten and unconcious on the
road... anyways you're welcome to stay here till you think you can find your
way home, the problem is that the nearest town from hereis a journey of about
two months on foot." so will you stay here or find your way home? Will you
simply stay and forge a living? Do you have family? Maybe you can find some
clues that offer an explanation to all of this. you leave the inn and find a
town bustling nows where your adventure starts.'''

controls = '''When you begin playing this game, there are a few commands
available to you, starting with movement, you can move north, south, east, and
west, typing these will move you to next area, when possible you may also climb
up or down simply by typing climb. At any moment in the game you can type help
and a list of all the commands in the game will be shown, as well as when you
type help and an action i.e "help north" a short description of what this
command does will be given.'''

print(intro)
print('')
print(controls)
print('')


class Game(cmd.Cmd):
    prompt = '> '

    def __init__(self):
#-----------------------------------------------------------------------
#Here the game is initialized asking for commands via the Cmd module,
#the variables given are the first room you start in and prints out the
#location

        cmd.Cmd.__init__(self)
        #self.get = get_action(action)
        self.inv = Inventory()
        self.loc = get_room('village')
        self.look()

#------------------------------------------------------------------------
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

    def look(self):
        print((self.loc.name))
        print('')
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

#-----------------------------------------------------------------------
#commands

    def do_inventory(self, args):
        '''Checks Inventory'''
        print(self.inv)

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

    def do_enter(self, args):
        '''Enters rooms, Villages, and caves where possible'''
        self.move('enter')

    def do_smithy(self, args):
        '''Enters Blacksmith'''
        self.move('blacksmith')

    #def do_mine(self, args):
        '''COllects items from mineable points'''
        self.action('mine')

    #def do_forge(self, args):
        '''For forging command at the blacksmith'''
        self.action('forge')

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
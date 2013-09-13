from room import get_room
from inventory import Inventory
import textwrap
from player import Player
from player import Actions


class Command():

    def __init__(self):
        self._exit = False

        self.player = Player()
        self.actions = Actions()
        self.inventory = Inventory()
        self.loc = get_room('intro')

        self._commands = {
            'look': self._look,
            'climb': self._climb,
            'enter': self._enter,
            'n': self._go_north,
            's': self._go_south,
            'e': self._go_east,
            'w': self._go_west,
            'get': self._go,
            'go': self._go,
            'get': self._get,
            'name': self._name,
            'hand': self._hand,
            'inventory': self._inventory,
            'leave': self._leave,
            'next': self._next,
            'quit': self._quit
            }

        self._commands_go = {
            'item': self._get,
            'north': self._go_north,
            'south': self._go_south,
            'east': self._go_east,
            'west': self._go_west
            }

        self.sort1 = sorted(self._commands.keys())
        self.sort2 = sorted(self._commands_go.keys())

    @staticmethod
    def parse_command(string):
        string = str(string)
        index = string.find(' ')
        if index < 0:
            return (string, None)

        return (string[:index], string[index + 1:])

    def run(self):
        self.look()
        while not self._exit:
            src = input('> ')
            (command, args) = Command.parse_command(src)

            if command in self._commands:
                self._commands[command](args)
            else:
                print('''I\'m sorry I dont know that comma\
nd {}, Try one of these: '''.format(command))
                print ('\n'.join(sorted(list(self.sort1))))

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print('''You cannot go this away''')
            self.look()
        else:
            self.loc = get_room(newroom)
            self.look()

    def look(self):
        print(self.loc.name)
        print('')
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def _quit(self, args):
        self._exit = True
        print('Thank You for playing')

    def _go(self, args):
        if args is None:
            print('Go accepts one of these:', ', '.join(
                (list(self.sort2))))
            return False
        (command, args) = Command.parse_command(args)
        if command not in self.sort2:
            print('Go accepts one of these:', ', '.join(
                (list(self.sort2))))
            return False
        if args is not None:
            print('Too many commands for go')
            return False

        self._commands_go[command](args)
        return True

    def _leave(self, args):
        self.move('leave')

    def _hand(self, args):
        self.player.hands()

    def _name(self, args):
        self.player.player_name()

    def _next(self, args):
        self.move('next')

    def _look(self, args):
        self.look()

    def _inventory(self, args):
        self.inventory.bag()
        self.look()

    def _get(self, args):
        self.actions.get_item()

    def _climb(self, args):
        self.move('climb')

    def _enter(self, args):
        self.move('enter')

    def _go_north(self, args):
        self.move('n')

    def _go_south(self, args):
        self.move('s')

    def _go_east(self, args):
        self.move('e')

    def _go_west(self, args):
        self.move('w')

c = Command()
c.run()
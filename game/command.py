from room import get_room
import textwrap



class Command():

    def __init__(self):
        self._exit = False

        self.loc = get_room('intro')

        self._commands = {
            'look': self._look,
            'n': self._go_north,
            's': self._go_south,
            'e': self._go_east,
            'w': self._go_west,
            'go': self._go,
            'next': self._next,
            'quit': self._quit
            }
        self._commands_go = {
            'north': self._go_north,
            'south': self._go_south,
            'east': self._go_east,
            'west': self._go_west
            }

    @staticmethod
    def parse_command(string):
        string = str(string)
        index = string.find(' ')
        if index < 0:
            return (string, None)

        return (string[:index], string[index + 1:])

    def run(self):
        while not self._exit:
            src = input('> ')
            (command, args) = Command.parse_command(src)

            if command in self._commands:
                self._commands[command](args)
            else:
                print(('I\'m sorry I dont know that command {}, Try one of these: '.format(command)))
                print (('\n'.join(list(self._commands.keys()))))

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

    def _quit(self, args):
        self._exit = True
        print('Thank You for playing')

    def _go(self, args):
        if args is None:
            print('Go accepts one of these: ', ': '.join((list(self._commands_go.keys()))))
            return False
        (command, args) = Command.parse_command(args)
        if command not in self._commands_go:
            print('Go accepts one of these: ', ': '.join((list(self._commands_go.keys()))))
            return False
        if args is not None:
            print('Too many commands for go')
            return False

        self._commands_go[command](args)
        return True

    def _next(self, args):
        self.move('next')

    def _look(self, args):
        self.look()

    def _go_north(self, args):
        pass

    def _go_south(self, args):
        pass

    def _go_east(self, args):
        pass

    def _go_west(self, args):
        pass

c = Command()
c.run()
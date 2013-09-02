

class Actions():

    def __init__(self, action):
        self.action = action

    def _actions(self, cmd):
        if cmd in self.action:
            return self.action[cmd]
        else:
            return None




def get_action(action):
    action = Actions()
    return action


class Actions():

    def __init__(self, action):
        super(Actions, self).__init__()
        self.action = action

    def _actions(self, cmd):
        if cmd in self.action:
            return self.action[cmd]
        else:
            return None


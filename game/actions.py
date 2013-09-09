from game import hand


class Actions():

    def __init__(self, action='some action'):
        self.action = action
        self.hand = hand

    def chop_tree(self):
        self.action = 'Chopping Trees'


class Atrributes():

    def __init__(self, get_use, use, durability, tool_yield):
        self.get_use = get_use
        self.use = use
        self.durability = durability
        self.tool_yield

    def wooden_axe(self):
        self.use = 'Chopping Trees'
        self.durability = 5
        self.tool_yield = 4
        #for future refrence I will be needung to
        #remove tool from inventory after durability equals 0

    def wooden_sword(self):
        self.use = self.get_use
        self.durability = 5

        if self.use == 'mining':
            self.tool_yield = 3
        if self.use == 'dirt':
            self.tool_yield = 1
        else:
            self.tool_yield = 0
            return 'Cannot use this item on this ore'

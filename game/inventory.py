import itemlib


class Inventory(object):

    def __init__(self, slots={}):
        self.lib = itemlib.Items()
        self.slots = {
                          'wood': 1,
                          'stone': 0,
                          'dirt': 0,
                          'gravel': 0,
                          'water': 0,
                          'wooden axe': 0,
                          'wooden sword': 0,
                          'stone axe': 0,
                          'stone sword': 0
                     }

    def bag(self):
        for k, v in sorted(self.slots.items()):
            print((k, v))
        return ' '
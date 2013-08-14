

class Inventory(object):

    def __init__(self, slots={}):

        self.slots = slots

    def inventory(self):

        self.slots = {
                    "slot1": 'empty',
                    "slot2": 'empty',
                    "slot3": 'empty',
                    "slot4": 'empty',
                    "slot5": 'empty'
                }

if __name__ == '__main__':
    i = Inventory()
    i
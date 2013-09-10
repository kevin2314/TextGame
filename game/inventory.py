import itemlib


class Inventory(object):

    def __init__(self, slots={}):
        self.call = itemlib.Items()
        self.slots = slots

    def bag(self):

        self.slots = {
                         self.call.item_id(1): 1
                     }

        sort = sorted(self.slots.items())
        for k, v in sort:
            if k == 0:
                if v == 0:
                    print('empty')
                else:
                    print(v)
            if v == 0:
                print('empty')
            else:
                print((k, v))
        return ' '
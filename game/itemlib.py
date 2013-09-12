

class Items(object):

    def __init__(self, item='item type', durability=0, gain=0,
        materials=0, id=0):
        self.item = item
        self.durability = durability
        self.gain = gain
        self.materials = materials
        self.id = id

    def item_id(self, id):

        self.wood = 'wood'
        self.stone = 'stone'
        self.dirt = 'dirt'
        self.gravel = 'gravel'
        self.water = 'water'
        self.wooden_axe = 'wooden axe'
        self.wooden_sword = 'wooden sword'
        self.stone_axe = 'stone axe'
        self.stone_sword = 'stone sword'

        self.id = {
            1: self.wood,
            2: self.stone,
            3: self.dirt,
            4: self.gravel,
            5: self.water,
            6: self.wooden_axe,
            7: self.wooden_sword,
            8: self.stone_axe,
            9: self.stone_sword
            }

        for k, v in sorted(self.id.items()):
            print((v))
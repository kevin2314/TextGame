

class Items(object):

    def __init__(self, item='item type', durability=0, gain=0,
        materials=0, id=0):
        self.item = item
        self.durability = durability
        self.gain = gain
        self.materials = materials
        self.id = id

    def item_id(self, id):

        self.wood = {self.item: 'wood'}
        self.stone = {self.item: 'stone'}
        self.dirt = {self.item: 'dirt'}
        self.gravel = {self.item: 'gravel'}
        self.water = {self.item: 'water'}
        self.wooden_axe = {
            self.item: 'Wooden Axe',
            self.durability: 5,
            self.gain: 3,
            self.materials: self.wood
        }
        self.wooden_sword = {
            self.item: 'Wooden Sword',
            self.durability: 10,
            self.gain: 0,
            self.materials: self.wood
        }
        self.stone_axe = {
            self.item: 'Stone axe',
            self.durability: 10,
            self.gain: 5,
            self.materials: self.stone
        }
        self.stone_sword = {
            self.item: 'stone sword',
            self.durability: 15,
            self.gain: 0,
            self.materials: self.stone
        }
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
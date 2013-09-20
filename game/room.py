import json
import os


def get_room(id):
    ret = None
    with open(os.path.join(
             os.path.dirname(__file__), 'rooms/' + str(id) + '.json'),
          'r') as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
    return ret


def grab_object(objects):
    objects = None
    if objects in Room(objects):
        return objects
    else:
        return 0


class Room():
    def __init__(self, id=0, name='A room', objects={},
        description='An empty room', neighbors={}):
        self.id = id
        self.name = name
        self.objects = objects
        self.description = description
        self.neighbors = neighbors

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def _objects(self, arg):
        if arg in self.objects:
            return self.objects[arg]
        else:
            return None

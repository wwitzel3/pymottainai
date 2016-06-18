class Card(object):
    def __init__(self, name, material=None, effect=None, job=None, owner=None):
        self.name = name
        self.material = material
        self.effect = effect
        self.owner = owner

    def __repr__(self):
        return repr((self.name))

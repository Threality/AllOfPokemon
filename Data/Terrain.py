class Terrain:
    def __init__(self, name):
        self._name = name

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        pass

class ElectricTerrain(Terrain):
    def __init__(self):
        super()._name = "Electric terrain" # incomplete
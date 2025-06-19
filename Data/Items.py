from Battle import GameEvent

class Item:
    def __init__(self, name):
        self._name = name

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        pass

class LucarioniteItem(Item):
    def __init__(self):
        super().__init__("Lucarionite")

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        if event == GameEvent.ON_MEGA_EVOLVE:
            if pokemon._name == "Lucario" and battle.curTeam._megaCount == 0:
                print(f"{pokemon._name} is reacting with the Lucarionite\n{pokemon._name} evolved into Mega Lucario")
                pokemon.MegaEvolve()
                battle.curTeam._megaCount += 1

class LeftoversItem(Item):
    def __init__(self):
        super().__init__("Leftovers")

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        if event == GameEvent.END_TURN:
            pokemon._health += (1/16) * pokemon._maxHealth
            if pokemon._health > pokemon._maxHealth:
                pokemon.health = pokemon._maxHealth
                print(f"{pokemon._name} nibbled on their leftovers...\n{pokemon._name}'s health was regenerated")



def GetSubclasses(cls):
    return cls.__subclasses__()

def GetItem(name):
    abilities = GetSubclasses(Item)
    for cls in abilities:
        if cls.__name__ == name+"Item":
            return cls()
    print("Failed to find item")
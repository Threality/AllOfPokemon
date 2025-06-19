from Battle import GameEvent

class Ability:
    def __init__(self, name):
        self._name = name

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        pass

class JustifiedAbility(Ability):
    def __init__(self):
        super().__init__("Justified")

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        if event == GameEvent.ON_DAMAGE:
            move = EXArgs.get("move")
            if move and move.type == "Dark":
                pokemon.StatChange("Attack", 1)
                print(f"{pokemon._name}'s attack was raised by 1 stage!")

class AdaptabilityAbility(Ability):
    def __init__(self):
        super().__init__("Adaptability")

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        if event == GameEvent.ON_STAT_CALC:
            pokemon._stab = 2
            print(f"{pokemon._name}'s stab moves have been boosted!")

class PressureAbility(Ability):
    def __init__(self):
        super().__init__("Pressure")

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        if event == GameEvent.BEFORE_TURN:
            battle._enemyTeam._PPUsage += 1
            print(f"{pokemon._name} is exerting its pressure!")



def GetSubclasses(cls):
    return cls.__subclasses__()

def GetAbility(name):
    abilities = GetSubclasses(Ability)
    print(abilities)
    for cls in abilities:
        if cls.__name__ == name+"Ability":
            print(cls)
            return cls()
    print("Failed to find ability")

if __name__ == "__main__":
    print(GetAbility("Pressure"))
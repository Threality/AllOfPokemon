import math
import json

# IVs/EVs = [Health, Attack, SpecialAttack, Defense, SpecialDefense, Speed]

class Pokemon:
    def __init__(self, name, level, nature, ability, item, baseTypes, baseStats, IVs, EVs, moves, **EXArgs):
        self._name = name
        self._curName = name
        self._level = level
        self._nature = nature
        self._ability = ability
        self._curAbility = ability
        self._item = item
        self._baseTypes = baseTypes
        self._curTypes = baseTypes
        self._baseStats = baseStats
        self._IVs = IVs
        self._EVs = EVs
        self._accuracy = 100
        self._evasion = 0
        self._stab = 1.5
        self._moves = moves
        self._curMoves = moves
        self._statChanges = [0, 0, 0, 0, 0, 0, 0]
        self._baseForm = self
        self._canMega = EXArgs.get("canMega")
        if self._canMega:
            self._isMega = False
            self._megaStats = EXArgs.get("megaStats")
            self._megaTyping = EXArgs.get("megaTyping")
            self._megaAbility = EXArgs.get('megaAbility')
            self._megaName = EXArgs.get('megaName')
        self._health = math.floor(0.01 * (2 * baseStats[0] + IVs[0] + math.floor(0.25 * EVs[0])) * self._level) + self._level + 10
        self._maxHealth = self._health
        self._attack = math.floor(((0.01 * (2 * baseStats[1] + IVs[1] + math.floor(0.25 * EVs[1])) * self._level) + 5) * self._nature._multipliers[0])
        self._specialAttack = math.floor(((0.01 * (2 * baseStats[2] + IVs[2] + math.floor(0.25 * EVs[2])) * self._level) + 5) * self._nature._multipliers[1])
        self._defense = math.floor(((0.01 * (2 * baseStats[3] + IVs[3] + math.floor(0.25 * EVs[3])) * self._level) + 5) * self._nature._multipliers[2])
        self._specialDefense = math.floor(((0.01 * (2 * baseStats[4] + IVs[4] + math.floor(0.25 * EVs[4])) * self._level) + 5) * self._nature._multipliers[3])
        self._speed = math.floor(((0.01 * (2 * baseStats[5] + IVs[5] + math.floor(0.25 * EVs[5])) * self._level) + 5) * self._nature._multipliers[4])

    def StatChange(self, type, change):
        match type:
            case "Attack":
                self._statChanges[0] += change
            case "Special Attack":
                self._statChanges[1] += change
            case "Defense":
                self._statChanges[2] += change
            case "Special Defense":
                self._statChanges[3] += change
            case "Speed":
                self._statChanges[4] += change

    def MegaEvolve(self):
        self._isMega = True
        self._curAbility = self._megaAbility
        self.StatUpdate(self._megaStats)
        self._curTypes = self._megaTyping
        self._curName = self._megaName

    def StatUpdate(self, stats):
        self._health = math.floor(0.01 * (2 * stats[0] + self._IVs[0] + math.floor(0.25 * self._EVs[0])) * self._level) + self._level + 10
        self._maxHealth = self._health
        self._attack = math.floor(((0.01 * (2 * stats[1] + self._IVs[1] + math.floor(0.25 * self._EVs[1])) * self._level) + 5) * self._nature._multipliers[0])
        self._specialAttack = math.floor(((0.01 * (2 * stats[2] + self._IVs[2] + math.floor(0.25 * self._EVs[2])) * self._level) + 5) * self._nature._multipliers[1])
        self._defense = math.floor(((0.01 * (2 * stats[3] + self._IVs[3] + math.floor(0.25 * self._EVs[3])) * self._level) + 5) * self._nature._multipliers[2])
        self._specialDefense = math.floor(((0.01 * (2 * stats[4] + self._IVs[4] + math.floor(0.25 * self._EVs[4])) * self._level) + 5) * self._nature._multipliers[3])
        self._speed = math.floor(((0.01 * (2 * stats[5] + self._IVs[5] + math.floor(0.25 * self._EVs[5])) * self._level) + 5) * self._nature._multipliers[4])





    def __str__(self):
        return (f'Name: {self._curName}\nType: {self._curTypes}\nLevel: {self._level}\nNature: {self._nature._name}\nAbility: {self._curAbility._name}\nItem: {self._item._name}\nHealth: {self._health}\nAttack: {self._attack}\nSpecial Attack: {self._specialAttack}\nDefense: {self._defense}\nSpecial Defense: {self._specialDefense}\nSpeed: {self._speed}\nAccuracy: {self._accuracy}\nEvasion: {self._evasion}\nMoves: {self._curMoves}')

class Lucario(Pokemon):
    def __init__(self, level, nature, ability, item, IVs, EVs, moves):
        super().__init__("Lucario", level, nature, ability, item, ["Fighting", "Steel"], [70, 110, 115, 70, 70, 90], IVs, EVs, moves, canMega=True, megaStats=[70, 145, 140, 88, 70, 112], megaTyping=["Fighting", "Steel"], megaAbility=AdaptabilityAbility(), megaName="Mega Lucario")

class Giratina(Pokemon):
    def __init__(self, level, nature, ability, item, IVs, EVs, moves):
        super().__init__("Giratina", level, nature, ability, item, ["Ghost", "Dragon"], [150, 100, 100, 120, 120, 90], IVs, EVs, moves)





class GameEvent:
    ON_SWITCH_IN = "onSwitchIn"
    BEFORE_TURN = "beforeTurn"
    ON_MOVE_USE = "onMoveUse"
    ON_MOVE_HIT = "onMoveHit"
    ON_DAMAGE = "onDamage"
    ON_KO = "onKO"
    END_TURN = "endTurn"
    TERRAIN_CHANGE = "terrainChange"
    WEATHER_CHANGE = "weatherChange"
    STATUS_GAINED = "statusGained"
    ON_STAT_CALC = "onStatCalc"
    ON_MEGA_EVOLVE = "onMegaEvolve"





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
                




class Nature:
    def __init__(self, name, multipliers):
        self._name = name
        self._multipliers = multipliers

class ModestNature(Nature):
    def __init__(self):
        super().__init__("Modest", [0.9, 1.1, 1, 1, 1])

class AdamantNature(Nature):
    def __init__(self):
        super().__init__("Adamant", [1.1, 0.9, 1, 1, 1])

class RelaxedNature(Nature):
    def __init__(self):
        super().__init__("Relaxed", [1, 1, 1.1, 1, 0.9])



class Terrain:
    def __init__(self, name):
        self._name = name

    def HandleEvent(self, event, pokemon, battle, **EXArgs):
        pass

class ElectricTerrain(Terrain):
    def __init__(self):
        super()._name = "Electric terrain"





class Battle:
    def __init__(self, team1, team2, battleType):
        self._team1 = team1
        self._team2 = team2
        self._battleType = battleType
        self._weather = None
        self._weatherDuration = 0
        self._terrain = None
        self._terrainDuration = 0

    def SetTerrain(self, terrain, pokemon):
        self._terrain = terrain
        self._terrainDuration = 5
        pokemon._item.HandleEvent("terrainChange", pokemon, self, terrain=terrain) # checks if extra duration needs to be added

    def SetWeather(self, weather, pokemon):
        self._weather = weather
        self._weatherDuration = weather._duration
        pokemon._item.HandleEvent("weatherChange", pokemon, self, weather=weather) # checks if extra duration needs to be added

    class Turn:
        pass





def GetSubclasses(cls, **EXArgs):
    pokemon = EXArgs.get("pokemon")
    if not pokemon:
        return cls.__subclasses__()
    
    classes = cls.__subclasses__()
    arr = []
    for i in range(len(classes)):
        if pokemon in classes[len(classes) - 1 - i]._availablePokemon == pokemon:
            arr.append(pokemon)
    return arr





def CreateTeams(POKEDEX):
    print("Here is a list of all available pokemon:")
    for dexNum, mon in POKEDEX.items():
        print(f'{dexNum}) {mon["name"]}')
    pokemonChoice = str(input(f'Pick a pokemon (num): '))
    pokemonChoice = POKEDEX[str(pokemonChoice)]

    if True: # filter for level editing
        level = int(input("Level: "))

    print("Here is a list of all available abilities:")
    availableAbilities = pokemonChoice["abilities"]
    if True: # can be replaced by filters later
        for hiddenAbility in pokemonChoice["hiddenAbilities"]:
            availableAbilities.append(hiddenAbility)
    i = 0
    for ability in availableAbilities:
        print(f'{i}) {ability}')
        i += 1
    abilityChoice = int(input(f'Pick an ability (num): '))
    abilityChoice = availableAbilities[int(abilityChoice)]
    
    moves = []
    print("Here is a list of all available moves:")
    availableMoves = pokemonChoice["levelMoves"]
    if True: # can be replaced by filters later
        for TMMove in pokemonChoice["TMMoves"]:
            availableMoves.append(TMMove)
    for j in range(0, 4):
        i = 0
        for move in availableMoves:
            print(f'{i}) {move}')
            i += 1
        moveChoice = int(input(f'Pick a move (num): '))
        moves.append(availableMoves[moveChoice])
        availableMoves.pop(moveChoice)
        




def Main():
    with open("Pokedex.json","r") as f:
        POKEDEX = json.load(f)

    while True:
        choice = str(input('What would you like to do?\n1) Battle\n2) Swap Teams\n3) Create Teams\nChoice (num): '))
        match choice:
            case "1":
                print("Battling")
            case "2":
                print("Swapping teams")
            case "3":
                print("Creating teams")
                CreateTeams(POKEDEX)
            case _:
                print("Please pick a valid option")





if __name__ == '__main__':
    Main()
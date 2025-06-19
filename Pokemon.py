import math
from Data import Natures
from Data import Abilities
from Data import Items

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

def CreatePokemon(PokedexEntry, level, ability, item, moves): #IVs and EVs presumed max and none respectively for now. Nature presumed adamant
    return Pokemon(PokedexEntry["name"], level, Natures.AdamantNature(), Abilities.GetAbility(ability), Items.GetItem(item), PokedexEntry["types"], PokedexEntry["baseStats"], [31, 31, 31, 31, 31, 31], [0, 0, 0, 0, 0, 0], moves) # moves is incomplete
    
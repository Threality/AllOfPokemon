import json
import Pokemon

def CreateTeams():
    with open("Data/Pokedex.json","r") as f:
        POKEDEX = json.load(f)

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

    with open("Data/Items.json","r") as f:
        Items = json.load(f)
    for itemNum, item in Items.items():
        print(f'{itemNum}) {item["name"]}')
    itemChoice = int(input(f'Pick an item (num): '))
    itemChoice = Items[str(itemChoice)]["name"]

    pokemon1 = Pokemon.CreatePokemon(pokemonChoice, level, abilityChoice, itemChoice, moves)
    print(pokemon1)
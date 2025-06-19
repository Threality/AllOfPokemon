import TeamCreater

class Player:
    def __init__(self, name):
        self._name = name
        self._team = []

    def GetName(self):
        return self._name
    
    def SetTeam(self, mon, **EXArgs): #add support for varied size teams
        self._team = mon
    
    def __str__(self):
        print(f"{self._name}'s team is {self._team}")

def Main():
    player1 = Player(str(input("First player's name: ")))
    player2 = Player(str(input("Second player's name: ")))
    while True:
        choice = str(input('What would you like to do?\n1) Battle\n2) Swap Teams\n3) Create Teams\nChoice (num): '))
        match choice:
            case "1":
                print("Battling")
            case "2":
                print("Swapping teams")
            case "3":
                print(f"Creating {player1.GetName()}'s team")
                player1.SetTeam(TeamCreater.CreateTeams())
                print(f"Creating {player2.GetName()}'s team")
                player2.SetTeam(TeamCreater.CreateTeams())
                
            case _:
                print("Please pick a valid option")





if __name__ == '__main__':
    Main()
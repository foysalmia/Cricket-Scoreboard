import random


class T2Cup:
    allTeams = []

    def entry_team(self, teamObj):
        self.allTeams.append(teamObj)


class Team(T2Cup):
    def __init__(self, name) -> None:
        self.teamName = name
        self.playersListObj = []
        super().entry_team(self)

    def entry_player(self, player):
        self.playersListObj.append(player)

    def __repr__(self) -> str:
        return f"{self.teamName}"


class Player:
    def __init__(self, name, teamObj) -> None:
        self.playerName = name
        self.strikeRate = 0.0
        self.runBat = 0
        self.sixes = 0
        self.fours = 0
        self.ballUsed = 0
        self.runBowl = 0
        self.wicketTaken = 0
        self.ballsBowled = 0
        teamObj.entry_player(self)

    def __repr__(self) -> str:
        return f"Name : {self.playerName}"


class Inings:
    def __init__(self, team1, team2, battingTeam, bowlingTeam) -> None:
        self.team1obj = team1
        self.team2obj = team2
        self.battingTeam = battingTeam
        self.bowlingTeam = bowlingTeam
        self.totalRun = 0
        self.totalWicket = 0
        self.totalOver = 0
        self.currentBall = 0
        self.currentBattingList = [
            battingTeam.playersListObj[0], battingTeam.playersListObj[1]]
        self.striker = battingTeam.playersListObj[0]
        self.currentBowler = None
        self.currentOverStatus = []
        self.allOverStatus = []

    def set_bowler(self, bowlerObj):
        self.currentBowler = bowlerObj

    def bowl(self, status):
        self.totalRun += status
        self.striker.runBat += status
        self.striker.ballUsed += 1
        self.currentBowler.runBowl += status
        self.currentBowler.ballsBowled += 1
        self.currentBall += 1

    def show_score_board(self):
        print(
            f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat}({self.currentBattingList[0].ballUsed})", end="\t")
        print(
            f"{self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat}({self.currentBattingList[1].ballUsed})")
        print(
            f"{battingTeam.teamName[:3].upper()}  {self.totalRun} - {self.totalWicket}")
        print(f"Overs : {self.totalOver}.{self.currentBall}")
        if self.currentBowler is not None:
            print(
                f"{self.currentBowler.playerName} - {self.currentBowler.runBowl}/{self.currentBowler.wicketTaken}")


cup = T2Cup()
bangladesh = Team("Bangladesh")
india = Team("India")
tamim = Player("Tamim Iqbal", bangladesh)
sakib = Player("Shakib Al Hasan", bangladesh)
kohli = Player("Virat Kohli", india)
rohit = Player("Rohit Sharma", india)
mustafiz = Player("Mustafizur Rahman", bangladesh)
bumrah = Player("Jasprith Bumrah", india)


while True:
    print("SELECT TEAMS TO BE PLAYED")
    for i, team in enumerate(cup.allTeams):
        print(f"{i+1}. {team.teamName.upper()}")
    team1Idx, team2Idx = map(int, input("Enter two teams index : ").split(" "))
    team1Idx -= 1
    team2Idx -= 1
    teamOne = cup.allTeams[team1Idx]
    teamTwo = cup.allTeams[team2Idx]

    # Tossing
    tossWin = random.choice([team1Idx, team2Idx])
    if tossWin == team1Idx:
        tossLost = team2Idx
    else:
        tossLost = team1Idx
    # Selcting batting or bowling
    rand = random.choice([0, 1])
    if rand == 0:
        battingTeam = cup.allTeams[tossLost]
        bowlingTeam = cup.allTeams[tossWin]
    else:
        battingTeam = cup.allTeams[tossWin]
        bowlingTeam = cup.allTeams[tossLost]

    firstInings = Inings(teamOne, teamTwo, battingTeam, bowlingTeam)
    firstInings.show_score_board()
    print("Choose Bowler ")
    for i, bowler in enumerate(bowlingTeam.playersListObj):
        print(f"{i+1} {bowler.playerName}")
    bowlerIdx = int(input("Enter Bowler Index : "))
    bowlerIdx -= 1
    bowlerObj = bowlingTeam.playersListObj[bowlerIdx]
    firstInings.set_bowler(bowlerObj)
    firstInings.show_score_board()

    print()
    firstInings.bowl(6)
    firstInings.show_score_board()
    break

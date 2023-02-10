from random import randint

MAX_RATING = 100


class Team:
    def __init__(self, rating: int, pts: int, name: str):
        self.rating = rating
        self.pts = pts
        self.name = name


file_names = ["ARS.txt", "ASTON.txt", "BOR.txt"]


def init_team(filename):
    fd = open(filename, "r")
    return Team(int(fd.read()), 0, filename.split(".")[0])


def play(team1, team2):
    ratingSum = team1.rating + team2.rating
    ratingDiff = abs(team1.rating - team2.rating)

    drawProbability = (
        MAX_RATING - ratingDiff
    ) / 3  # max draw propability is 33% in case ratings are equal. min is 0 in case one team has max rating and another has 0
    team1WinProb = (100 - drawProbability) * team1.rating / ratingSum
    team2WinThreshold = drawProbability + team1WinProb

    randNum = randint(0, 100)

    if randNum < drawProbability:
        team1.pts = team1.pts + 1
        team2.pts = team2.pts + 1
        print("000")
    elif randNum < team2WinThreshold:
        team1.pts = team1.pts + 3
        print("111")
    else:
        team2.pts = team2.pts + 3
        print("222")


teams = []
for filename in file_names:
    teams.append(init_team(filename))

for i in range(len(teams)):
    for j in range(len(teams)):
        if i != j:
            play(teams[i], teams[j])

for team in teams:
    print(team.name + " - " + str(team.pts))

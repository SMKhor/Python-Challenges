#This is following the Rugby Union scoring system
team1 = input("What is the name of the first team?")
team2 = input("What is the name of the second team?")
team1score = []
team2score = []
totalteam1 = 0
totalteam2 = 0
sort = ""

while sort != "end":
    sort = input("Which team scored? 1, 2 or end (use this at the end of the game)")
    if sort == "1":
        point1 = input("How did they score? T for try, C for conversion, P for penalty and D for drop goal")
        if "T" in point1:
            team1score.append("try")
            totalteam1 += 5
        elif "C" in point1:
            team1score.append("conversion")
            totalteam1 += 2
        elif "P" in point1:
            team1score.append("penalty")
            totalteam1 += 3
        elif "D" in point1:
            team1score.append("drop goal")
            totalteam1 += 3

    if sort == "2":
        point2 = input("How did they score? T for try, C for conversion, P for penalty and D for drop goal")
        if "T" in point2:
            team2score.append("try")
            totalteam2 += 5
        elif "C" in point2:
            team2score.append("conversion")
            totalteam2 += 2
        elif "P" in point2:
            team2score.append("penalty")
            totalteam2 += 3
        elif "D" in point2:
            team2score.append("drop goal")
            totalteam2 += 3

print("Team",team1, "scored:", totalteam1, "points through", team1score)
print("Team",team2, "scored:", totalteam2, "points through", team2score)

if totalteam1 > totalteam2:
    print("Team", team1, "wins!")

if totalteam2 > totalteam1:
    print("Team", team2, "wins!")

if totalteam1 == totalteam2:
    print("It is a draw!")

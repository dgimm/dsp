# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('desktop/metis/prework/dsp/python/football.csv', 'r') as csvfile:
    epl = []
    goal = []
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        epl.append(row)
    for i in epl:
        goal.append(abs(int(i[5]) - int(i[6])))
    team = goal.index(min(goal))
    print(epl[team][0])

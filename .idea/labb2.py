import numpy as np
import random as rm
import math


States = ["Tv", "President", "University", "Oil"]

TransitionNames =[
            ["TT", "TP", "TU", "TO"],
            ["PT", "PP", "PU", "PO"],
            ["UT", "UP", "UU", "UO"],
            ["OT", "OP", "OU", "OO"]
            ]

TransitionMatrix = [
            [0, 1/3, 1/3, 1/3],
            [0,  0,  1/2, 1/2],
            [1,  0,   0,   0],
            [1/2, 0,  1/2, 0]
]
def sami (repository):
    x=y


#probability distribution [1/4, 1/4, 1/4, 1/4] uppgift h)


def pageRank (clicks):
    starting_page = "Tv"
    current_page = starting_page
    page_order = [starting_page]

    i = 0
    prob = 1

    while i != clicks:
        if current_page  == "Tv":
            change_page = 1


            """
            if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
        i += 1  
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

# Function that forecasts the possible state for the next 2 days
activity_forecast(2)
"""
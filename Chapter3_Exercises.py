import os
from typing import List

def EndOfExerciseContinue():
    input("Press the <ENTER> key to continue...")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        

#Exercise 3-1
# Store names in a list called name. Print each person's name by accessing each eleement in the list
print("\tExercise 3-1")

names : List[str] = ["Gideon", "Harrowhark", "Ianthe", "Coronabeth", "Palamedes", "Camilla",
                     "Pyrhha", "Nona", "Alecto"]

for i in range(len(names)):
    print(names[i])


EndOfExerciseContinue()

#Exercise 3-2
# Start with the list used in Exercise 3-1. Print out a repeated message to each person but include their name
print("\tExercise 3-2")

message : str = "I hope you have a good day, "

for i in range(len(names)):
    print(message + names[i] + ".")

EndOfExerciseContinue()

#Exercise 3-3
# Make a list. Use the list to print a series of statements about the items of the list. 
print("\tExercise 3-3")

breakfastFoods : List[str] = ["Eggs", "Fruit", "Toast", "Waffles" ]


for i in range(len(breakfastFoods)):
    print(f"I'd like {breakfastFoods[i]} for breakfast, please.")
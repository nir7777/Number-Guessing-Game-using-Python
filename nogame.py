


print(str("******************Welcome to Number Guessing Game*****************"))

import random
random_num = random.randrange(1,10)
guess = int(input("Please choose a number betweeen 1 to 10\n"))
correct = False
print(random_num)

while not correct:
    if guess==random_num:
        print("Congrats You guess the correct number")
        correct = True
    elif guess>random_num:
        print("Your Guess is Too High")
        break
    elif guess<random_num:
        print("Your Guess is Too Low")
        break
    else:
        print("Try Something Else")
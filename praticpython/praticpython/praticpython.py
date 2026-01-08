import random

turn = 1
total = 0
round = 0
answer = ""
roll = 0

while True:
    print(f"Turn {turn}")
    print(f"Your Current Score is: {total}")
    print(f"This round you have: {round}")
    answer = input("Would you like to roll or bank? ").lower()

    if answer == "roll":
        roll = random.randint(1, 6)
        print(f"You rolled {roll}")
        if roll == 1:
            round = 0
            print("You rolled a 1! You lose all points for this round.")
            break
        else:
            round += roll
            print(f"This round you have: {round}")
    elif answer == "bank":
        total += round
        round = 0
        print(f"You banked your points! Your total score is now: {total}")
        turn += 1
        break
    else:
        print("Invalid input. Please type 'roll' or 'bank'.")
with open("scores.txt", "r") as f:
    lines = f.readlines()

score = int(input("Enter your score: "))  
if 0 >= score <= 100:  
    score.append(score)  
    with open("scores.txt", "w") as f:  
        for s in score:  
            f.write(str(s) + "\n")

while True:
    with open("score.txt", "r") as f:
        lines = f.readlines()
    scores = [int(line.strip()) for line in lines]

    print("Choose for what you want to do next?")
    print("1. Show the average")
    print("2. Show highest to lowest")
    print("3. Show lowest to highest")
    print("4. Add more scores")
    print("5. Exit out of the program")
    choice = input("Enter 1, 2, 3, 4 or 5: ")

    if choice == '1':
        if scores:
            print("The average score is:", sum(scores) / len(scores))
        else:
            print("No score yet.")
    elif choice == '2':
        if scores:
            print("Highest to lowest:", sorted(scores, reverse=True))
        else:
            print("No scores yet.")
    elif choice == '3':
        if scores:
            print("Lowest to highest:", sorted(scores))
        else:
            print("No scores yet.")
    elif choice == '4':
        scores = int(input("Enter your other score: "))
        if 0 >= scores <= 100:
            with open("scores.txt", "a") as f:
                for s in scores:
                    f.write(str(scores) + "\n")
        else:
            print("score must be between 0 to 100")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invaild choice!")
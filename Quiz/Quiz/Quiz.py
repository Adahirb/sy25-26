Score = 0
print("Question 1. What is 8 x 9 + 32?")
print("1-104")
print("2-105")
answer=input()
if answer == "1":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Question 2. What is (4 x 2 + 4) - 4?")
print("1-8")
print("2-4")
answer=input()
if answer == "2":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Question 3. What is the color of a red apple?")
print("1-Red")
print("2-Green")
print("3-Yellow")
answer=input()
if answer == "1":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Question 4. What color is the sky?")
print("1-Red")
print("2-Green")
print("3-Blue")
answer=input()
if answer == "3":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Question 5. What is the largest country?")
print("1-China")
print("2-Russia")
print("3-Germany")
answer=input()
if answer == "2":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
print("Question 6. What is the country with the most lakes?")
print("1-Norway")
print("2-Russia")
print("3-Canada")
answer=input()
if answer == "3":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Quesion 7. What is the capital of France?")
print("1-Berlin")
print("2-Vichy")
print("3-Paris")
answer=input()
if answer == "3":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Question 8. What is the capital of Germany?")
print("1-Frankfurt")
print("2-Berlin")
print("3-Munich")
answer=input()
if answer == "2":
    print("Right answer")
    Score = Score + 2
else:
    print("wrong answer")
    Score = Score + 0
print("Question 9. What is the capital of Russia?")
print("1-Moscow")
print("2-Saint Petersburg")
print("3-Kazan")
answer=input()
if answer == "1":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("Question 10. What is the capital of Norway?")
print("1-Oslo")
print("2-Bergen")
print("3-Trondheim")
answer=input()
if answer == "1":
    print("Right answer")
    Score = Score + 2
else:
    print("Wrong answer")
    Score = Score + 0
print("You finished the quiz! Your score is " + str(Score) + " out of 20")
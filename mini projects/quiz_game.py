print("Welcome to the game")

playing = input("Do you wanna play?: ")

if playing.lower() != "yes":
    quit()

print("okay! let's play")
score = 0

answer = input("Q1. What is the Capital of India?: ")
if answer.lower() == "delhi":
    print("Correct!!")
    score +=1
else:
    print("Sorry but wrong answer!")

answer = input("Q2. What is the finance capital of India?: ")
if answer.lower() == "mumbai":
    print("Correct!!")
    score +=1
else:
    print("Sorry but wrong answer!")

answer = input("Q3. Where is Pune?: ")
if answer.lower() == "maharastra":
    print("Correct!!")
    score +=1
else:
    print("Sorry but wrong answer!")

answer = input("Q4. What does IPL stands for: ")
if answer.lower() == "indian premier league":
    print("Correct!!")
    score +=1
else:
    print("Sorry but wrong answer!")

answer = input("Q5. full form of SRK?: ")
if answer.lower() == "sharukh khan":
    print("Correct!!")
    score +=1
else:
    print("Sorry but wrong answer!")

if score >= 3:
    print("Congrats your Score is:" + str(score))
else:
    print("Practice more buddy, here's your Score:" + str(score))
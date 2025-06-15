import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Enter a positive number plz")
        quit()
else:
    print("Enter a positive number plz")
    quit()

random_num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    
    user_guess = input("now guess a number in between: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("try again")
        continue

    if user_guess == random_num:
        print("that's great you got it right in", guesses, "guess")
        break
    else:
        if user_guess > random_num:
            print("Nope.....it's a small number")
        else:
            print("Nope....it's a bigger number")



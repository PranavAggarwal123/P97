import random
print("Number Guessing Game")
number = random.randint(1, 9)
chances = 0
print("Guess A Number Between 1 - 9")
while chances<5:
    guess = int(input("Enter Your Guess"))
    if guess == number:
        print("Congratulations You Won!")
        break
    elif guess<number:
        print("Your Guess Was Low, Guess A Higher Number", guess)
    else:
        print("Your Guess Was Too High, Guess A Lower Number", guess)
    chances+=1
if not chances<5:
    print("You Lose! The Number Is ", number)
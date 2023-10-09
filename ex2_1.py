import random
hiddenNumber = random.randint(1, 50)

print(" Welcome to The Guess Number Game")
max_attempts = 10
attempts = 0

while attempts < max_attempts:
        
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < hiddenNumber:
            print("go up!!")
        elif guess > hiddenNumber:
            print("come down!!")
        else:
            print("congratulations you found the secret   ",hiddenNumber,"in   ",attempts,"  attemps")
            break

if attempts >= max_attempts:
    print("you lost! end of the game the hiddenNumber was    ", hiddenNumber)
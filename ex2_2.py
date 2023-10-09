import random
user_score = 0
computer_score = 0

while user_score<3 and computer_score<3 :
    
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        user_choice = input("Invalid choice. Please enter Rock, Paper, or Scissors: ")
    
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice=random.choice(choices)

    print("You chose:",user_choice)
    print("Computer chose ",computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    print("Your score:   " ,user_score)
    print("Computer's score:   ",computer_choice)
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break
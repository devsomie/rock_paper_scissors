
import random

done = False
choices = ["rock", "paper", "scissors"]

#Check if user input is valid
while not done:
    choices_made = None
    CPU_input = random.choice(choices)
    user_input = input("Enter r for Rock, p for Paper or s for Scissors: ")

    if user_input == "r":
        user_option = "rock"
        choices_made = "valid"

    elif user_input == "p":
        user_option = "paper"
        choices_made = "valid"
    
    elif user_input == "s":
        user_option = "scissors"
        choices_made = "valid"
    
    else:
        print("invalid iput. Please try again!")

#game play
    if choices_made == "valid":
        print(f"player ({user_option}) : CPU ({CPU_input})")

        if user_option == CPU_input:
            print("Its a tie!. Play again!")
            continue
        else:
            if user_option == "rock":
                if CPU_input == "paper":
                    print("Computer wins!")
                else:
                    print("user wins")
                    
            if user_option == "paper":
                if CPU_input == "scissors":
                    print("Computer wins!")
                else:
                    print("user wins")
                    
            if user_option == "scissors":
                if CPU_input == "rock":
                    print("Computer wins!")
                else:
                    print("user wins")
            break
  

import random

while 1:
    options = ["rock", "paper", "scissors"]

     

    user_choice = (input("Choose Rock, Paper, or Scissors: ")).lower()

    computer_choice = random.choice(options)

     

    print("You choose: ", user_choice)

    print("Computer choose: ", computer_choice)

     
    #print("you select",type(user_choice))
    #print("computer select",type(computer_choice))
    if user_choice != computer_choice:
        if user_choice == "rock" and computer_choice == "scissors":
            print(" Hurray! You win!")

        elif user_choice == "paper" and computer_choice == "rock":

            print("Hurray! You win!")

        elif user_choice == "scissors" and computer_choice == "paper":

            print("Hurray! You win!")
        else:
            print("Computer wins!")

    else:
        print("match draw")
    if input("Do you want play again")!='yes':
        break
    



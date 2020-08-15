import random


no_of_choice = 10
choice = 0
human_point = 0
computer_point = 0

lst = ["r","p","s"]



if __name__ == "__main__":
    print(".......................WelCome to ROCK-PAPER-SCISSOR game.......................\n\n")
    print("r for rock \np for paper \ns for scissor\n")

    while choice < no_of_choice :
        human_guess = input("rock,paper,scissor : ")
        computer_guess = random.choice(lst).lower()

        if human_guess == 'r' or human_guess == 'p' or human_guess == 's':
            print(f"human guess is {human_guess} and computer guess is {computer_guess}\n")

            # user input is "R"
            if human_guess == 'r' and computer_guess == 'p':
                print("computer wins 1 point\n")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            elif human_guess == 'r' and computer_guess == 's':
                print("human wins 1 point")
                human_point = human_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            # user input is "P"
            elif human_guess == 'p' and computer_guess == 'r':
                print("human wins 1 point")
                human_point = human_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            elif human_guess == 'p' and computer_guess == 's':
                print("computer wins 1 point")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            # user input is "S"
            elif human_guess == 's' and computer_guess == 'p':
                print("human wins 1 point")
                human_point = human_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")

            elif human_guess == 's' and computer_guess == 'r':
                print("computer wins 1 point")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            elif human_guess == computer_guess:
                print("Tie both 0 point to each")
            
            choice = choice + 1

            print(f"{no_of_choice - choice} is left out of {no_of_choice}")
            print("-----------------------------------------------------------------------------")

        else:
            print("Wrong input")
            print("-----------------------------------------------------------------------------")
        

        print("------Game Over------")
        


    if human_point > computer_point:
        print("---> You wins and Computer lose")
    elif computer_point > human_point :
        print("---> Computer wins and You lose")
    else:
        print("---> Tie both point are eual")
    
    print(f"===>>  Human point is {human_point} and Computer point is {computer_point}  <<===")

        


    
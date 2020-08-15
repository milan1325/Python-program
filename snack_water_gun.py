import random

Total_try = 10
Try = 0
human_point = 0
computer_point = 0
computer_choice = ["w","s","g"]


if __name__ == "__main__":
    print("\t\t\t\t Welcome to SANCK,WATER,GUN game.... \n\n")
    print("press s for snack\npress w for water\npress g for gun\n\n")
    
    
    while Try < Total_try: 
        human_guess = input("Snack,Water,Gun : ").lower()
        computer_guess = random.choice(computer_choice)
        
        
        
        if human_guess == 's' or human_guess == 'w' or human_guess == 'g':
            
            print(f"Your guess is {human_guess} and computer guess is {computer_guess}\n")
            #user input s
            if computer_guess == 'w' and human_guess == 's':
                print("human wins 1 point \n")
                human_point = human_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            elif computer_guess == 'g' and human_guess == 's':
                print("computer wins 1 point \n")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            # user input g
            elif computer_guess == 'w' and human_guess == 'g':
                print("computer wins 1 point \n")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            elif computer_guess == 's' and human_guess == 'g':
                print("human wins 1 point \n")
                human_point = human_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            
            # user input w
            elif computer_guess == 's' and human_guess == 'w':
                print("computer wins 1 point \n")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            elif computer_guess == 'g' and human_guess == 'w':
                print("human wins 1 point \n")
                computer_point = computer_point + 1
                print(f"computer point is {computer_point} and human point is {human_point}\n")
            
            
            elif human_guess == computer_guess:
                print("Tie Both 0 point to each")

            
            Try = Try + 1
            print(f"{Total_try - Try} is left out of {Total_try}\n")
            print("--------------------------------------------------")


        else:
            print("wrong input")
            print("--------------------------------------------------")


        
    
    
    print("Game Over\n")


if human_point > computer_point :
    print("-->  human win and you lose")

elif computer_point > human_point :
    print("-->  computer win and you lose")

else:
    print("Tie both point are queal")

print(f"===>> human point is {human_point} and computr point is {computer_point} <<===")

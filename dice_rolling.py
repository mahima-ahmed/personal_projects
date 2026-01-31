import random # we import the random module to generate random numbers
while True: # infinite loop to keep asking the user
    choice = input('Do you want to roll a dice? (yes/no): ').strip().lower() #ask the user
    if choice == 'yes':
        dice_roll_1 = random.randint(1,6) # (first number) generate numbers between 1 and 6
        dice_roll_2 = random.randint(1,6) # (second number) generate numbers between 1 and 6
        print (dice_roll_1, dice_roll_2)
    elif choice == 'no':
        print('Thanks for playing!')
        break # we exit from the loop if the user says no
    else:
        print('Invalid choice! Please enter yes or no.')
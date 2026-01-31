import random
number = random.randint(1,100) # generate a random number between 1 and 100
while True: # infinite loop
    try: # we use try and except to handle invalid inputs
        guess_number = int(input('Guess a number between 1 and 100: ')) # ask user a number

        if guess_number < number:
            print('Too low! Try again please.')
        elif guess_number > number:
            print('Too high! Nice try, try again please.')
        else:
            print('Congratulations! You guessed the number', number)
            break # exit the loop if the user guesses the correct number
    except ValueError:
        print('Invalid input! Please enter a valid number.') # if not equal to the random number, we print an invalid input message.
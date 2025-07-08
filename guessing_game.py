import random
secret_number = random.randint(1,100)
attempts = 0
while True:
    guess_number = int(input("Enter a number from 1 to 100: "))
    attempts += 1
    if guess_number <secret_number:
        print('Too low! Try again')
    elif guess_number>secret_number:
        print('Too high! Try again')
    else:
        print('Congratulations You Predicted the Correct number in '+str(attempts) +' tries')
        break

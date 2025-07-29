import random
name = input('Enter your name : ')

print('All the best',name)
print(' The Game is about Guessing the names of Animals')
print('Lets Start')
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra", "Rhinoceros", "Hippopotamus", "Leopard", "Cheetah", "Gorilla", "Chimpanzee", "Orangutan", "Panda", "Koala", "Kangaroo", "Sloth", "Armadillo", "Anteater", "Crocodile", "Alligator", "Komodo Dragon", "Iguana", "Chameleon", "Tortoise", "Sea Turtle", "Dolphin", "Whale", "Shark", "Octopus", "Squid", "Jellyfish", "Starfish", "Seahorse", "Penguin", "Ostrich", "Eagle", "Falcon", "Owl", "Peacock", "Parrot", "Flamingo", "Swan", "Duck", "Goose", "Wolf", "Fox", "Bear", "Deer", "Moose", "Bison"]

random_choice = random.choice(animals)
print('Guess the Charecter')
guesses = ''
choice = 10
while choice>0:
    failed = 0
    for char in random_choice:
        if char in guesses:
            print(char,end = '')
        else:
            print('_')
            failed += 1
    if failed == 0:
          print('You Nailed it')
          print('The word is :',random_choice)
          break
    guess = input("Enter your Guess")
    guesses += guess
    if guess not in animals:
         choice -= 1
         print('Wrong')
         print("You have", choice,'chance to guess')
    if choice == 0:
        print('You Fail')
        print('The corrct word was',random_choice)
        print('Better Luck Next Time')


import random

# Words list
The_words = ''' 
apple, banana, orange, grapes, mango, cherry, kiwi, papaya, lemon, peach,
school, pencil, eraser, teacher, student, marker, blackboard, homework, desk, chair,
planet, galaxy, rocket, comet, orbit, space, astronaut, telescope, universe, moon,
guitar, piano, violin, trumpet, drums, music, singer, melody, rhythm, concert,
ocean, island, desert, forest, mountain, valley, river, waterfall, beach, glacier,
winter, summer, spring, autumn, season, cloudy, thunder, lightning, rainbow, storm,
animal, monkey, tiger, elephant, leopard, jaguar, dolphin, penguin, rabbit, zebra,
castle, dragon, knight, wizard, magic, sword, shield, crown, kingdom, prince,
friend, family, mother, father, sister, brother, cousin, uncle, aunt, niece,
coding, python, laptop, window, browser, server, client, script, hacker, logic
'''
The_words = The_words.replace('\n', '').split(',')

# Clean up extra spaces
The_words = [word.strip() for word in The_words if word.strip() != '']

# Randomly choose a word
Word = random.choice(The_words).lower()

if __name__ == '__main__':
    print("Guess the Word:")

    display_word = ['_' for _ in Word]
    guessed_letters = []
    chances = len(Word) + 2

    while chances > 0 and '_' in display_word:
        print("\nWord: ", ' '.join(display_word))
        print("Guessed Letters:", ', '.join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print(" You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in Word:
            print(" Correct!")
            for idx, char in enumerate(Word):
                if char == guess:
                    display_word[idx] = guess
        else:
            print(" Incorrect!")
            chances -= 1
            print(f"Chances left: {chances}")

    if '_' not in display_word:
        print("\n Congratulations! You guessed the word:", Word)
    else:
        print("\n You lost! The word was:", Word)

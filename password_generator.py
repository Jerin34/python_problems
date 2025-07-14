import random
import string
length = int(input("Enter the length of the password: "))
all_characters = string.ascii_letters+string.digits+string.punctuation
password = ''
for i in range(length):
    password += random.choice(all_characters)
print("Generated Password:", password)
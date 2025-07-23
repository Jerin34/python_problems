W = input('Enter a Word : ')  #takes input from the user

words = ''     #variable to store the hyphenated word
for char in W:
    
    words += char + '-'
# Remove the last hyphen
print(words[:-1])
# Print the hyphenated word
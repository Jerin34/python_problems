#  input from the user
N = input()

# Initialized an empty string 
new_string = ''

# Spliting the input into list
split = N.split()

# Reverse each word and append it to new_string
for char in split:
    new_list = char[::-1]   # reverse the current word
    new_string += new_list + " "

# Strip trailing spaces, reverse the full string, and print result
print(new_string.strip()[::-1])

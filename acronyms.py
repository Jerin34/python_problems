# input from the user
N = input()

# Initialize an empty string to collect first letters
r = ''

# Split the input into words
split_N = N.split()

# Extract the first letter of each word and append to r
for char in split_N:
    first_letter = char[0]   # get first character of the word
    r += first_letter

# Join the collected letters with dots between them
dots = '.'.join(r)

# Print the final dotted string
print(dots)

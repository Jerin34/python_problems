# Read input string from user
S = input("Enter a sentence: ")

# Split the input string into a list of words
splited = S.split()

# Initialize an empty list to store characters
lists = []

# Loop through each word in the list
for word in splited:
    # Check if the word length is greater than 2
    if len(word) > 2:
        # Append the 3rd character (index 2) of the word to the list
        lists += word[2]

# Join the collected characters with commas
charecter_seprated_by_coma = ','.join(lists)

# Print the final result
print(charecter_seprated_by_coma)

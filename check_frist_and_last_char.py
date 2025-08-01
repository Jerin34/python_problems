N = input("Enter a sentence: ")

# Split the input  into a list 
spliting_N_into_list = N.split()

# Looping through each word in the list
for char in spliting_N_into_list:
    # Compare the first and last character of the word
    if char[0].lower() == char[-1:].lower():
        print('True')   # Print True if they are the same
    else:
        print('False')  # Print False if they are different

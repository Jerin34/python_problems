# Define a list with mixed data types (integers, strings, floats)
L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

# Take two indices as input from the user
L1 = int(input("Enter the first index: "))
L2 = int(input("Enter the second index: "))

# Store the elements at the given indices (optional — not strictly needed for swapping)
frist = L[L1]
second = L[L2]

# Swap the two elements in the list
L[L1], L[L2] = L[L2], L[L1]

# Print the updated list after swapping
print("List after swapping:", L)

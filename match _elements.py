# Take first input 
list_a = input("Enter first list (comma-separated): ").split(",")

# Take second input 
list_b = input("Enter second list (comma-separated): ").split(",")

# Find the length of the first list
len_of_list_a = len(list_a)

# Reversed the second list
n = list_b[::-1]

# Iterate through the elements of the first list
for i in range(len_of_list_a):
    num_1 = list_a[i]   # Get the i-th element from list_a
    num_2 = n[i]        # Get the i-th element from the reversed list_b
    result = str(num_1) + " " + str(num_2)  # Combine both values with a space
    print(result)       # Print the result

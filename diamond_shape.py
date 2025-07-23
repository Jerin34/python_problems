
N = int(input('Enter a Number: '))

# --------- Top Half of the Diamond ---------
for i in range(1, N + 1):
    # Calculate spaces on the left to center the slashes
    left_spaces = ' ' * (N - i)
    
    if i == 1:
        # First line: just a narrow peak (no hollow space)
        print(left_spaces + '/' + '\\')
    else:
        # Hollow space between the slashes
        hollow_spaces = ' ' * (2 * i - 2)
        # Print the slashes with hollow space in between
        print(left_spaces + '/' + hollow_spaces + '\\')

# --------- Bottom Half of the Diamond ---------
for i in range(N, 0, -1):
    # Calculate spaces on the left to center the slashes
    left_spaces = ' ' * (N - i)
    
    if i == 1:
        # Last line: just a narrow bottom tip
        print(left_spaces + '\\' + '/')
    else:
        # Hollow space between the slashes
        hollow_spaces = ' ' * (2 * i - 2)
        # Print the inverted slashes with hollow space in between
        print(left_spaces + '\\' + hollow_spaces + '/')

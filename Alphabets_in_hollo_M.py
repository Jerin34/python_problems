N = int(input())

for i in range(1, N + 1):
    space = ' ' * (N - i)

    if i == 1:
        row = space + chr(64 + i) + ' ' * (2 * (N - i)) + chr(64 + i)
    else:
        inner_space = ' ' * (2 * i - 3)
        left_part = space + chr(64 + i) + inner_space + chr(64 + i)
        middle_space = ' ' * (2 * (N - i))
        right_part = chr(64 + i) + inner_space + chr(64 + i)
        row = left_part + middle_space + right_part

    print(row)  

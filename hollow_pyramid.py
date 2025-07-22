N = int(input('Enter the Number: '))
for i in range( 1,N+1): # for upper part
    if i == 1:
        print('|')
    else:
        hollow_spaces = ' '*(i-2) #calculating hollwo spaces
        print("|",hollow_spaces + "\\")
for i in range(N,0,-1): # for lower part
    if i == 1:
        print('|')
    else:
        hollow_spaces = ' '*(i-2)
        print("|",hollow_spaces + "/")
    
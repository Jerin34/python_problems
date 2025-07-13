user_input = int(input('Enter a Number:')) #here the user can input any number
for i in range(1,user_input+1):
    if i ==1 or i ==user_input: #if i is or user_input then print N satrs according to input
        print( "* "*(user_input))
    else:
        hollow_space = '  '*(user_input-2) ## calculate the amoun tspace needed
        print("* "+hollow_space+"*") 

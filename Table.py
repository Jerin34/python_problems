n = int(input('Enter a number to generate its multiplication table: '))
N = int(input('Enter the range for the multiplication table: '))
for i in range(1,N+1):
    print(str(i)+' * '+str(n) +' = '+str(i*n))
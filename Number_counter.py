N = input('Enter a Sentence: ')
count = 0
for char in N:
    if char.isdigit():
        count += 1
print('Number of digits in the sentence:', count)
if count == 0:
    print('No digits found in the sentence.')

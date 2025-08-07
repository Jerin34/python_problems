import random
nums = random.randrange(1000,10000)
guess = int(input('Enter a Random 4 digit Number: '))
if guess == nums:
    print('Wow you are MasterMind. You guesses the number in one try')
else:
    counter = 0
    while(guess!=nums):
       counter += 1
       count = 0
       guess = str(guess)
       nums = str(nums)
       correct =  ['X']*4
       for i in range(0,4):
        if guess[i] == nums[i]:
             count += 1
             correct[i] = nums[i]
        else:
            continue
        print('Not quite the Number.But you did get \n',count,'digit(s)  are correct')
        print('\n')
        print('\n')
        nums = int(input('Enter your next choice of Numbers'))
       if count>0:
            print('Not quite the Number. But you did get', count, 'digit(s) correct')
            print("Correct digits so far:", ''.join(correct))
       elif(count == 0):
        print('None of your inputs Match')
        guess = int(input('Enter your next number of Choice'))
    if guess ==nums:
        counter +=1
        print('You become the master mind')
        print('It took only',counter,'times')


     




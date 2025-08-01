word = input()
frist_num = int(input())
last_num = int(input())

s = ''
for char in word:
    s = ord(char)
    # print(s)
    for i in range(frist_num,last_num+1):
        if i == s:
            print(chr(i),end=' ')

import time
import random
     

a = [int(input()) for i in range(9)]
b = [None]*9
print(a)
window = 2
c = 0
d = 0
for i in range(int(len(a)/window)):
    for j in range(window):
        b[j] = a[j]
        print(c,'th frame sent',)
        c+=1
        c1 = [d+i for i in range(3)]
    print('\n')
    for j in range(window):
        print(c1[j],'th frame recieved')
        d+=1
        print('\n')

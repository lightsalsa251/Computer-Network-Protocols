import time
import random
a = [i for i in range(9)]
b = [None]*9
c = []
d = 0
for j in range(3):
    for i in range(d,d+3):
        c.append(i)
    rem = random.randint(c[0],c[2])
    c.remove(rem)
    for i in range(rem):
        print('sending',d)
        d+=1
    time.sleep(2)
    for i in range(rem):
        print('recieving',d)
        d+=1
    print('\n')
    print('lost ',rem)
    print('\n')
    for i in range(rem,c[2]+1):
        print('sending',d)
        d+=1
    time.sleep(2)
    for i in range(rem,c[2]+1):
        print('recieving',d)
        d+=1

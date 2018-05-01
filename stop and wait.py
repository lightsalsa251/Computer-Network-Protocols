import time
a = [i for i in range(10)]
print(a)
b = [None]*10

for i in range(10):
    b[i] = a[i]
    print('packet',i,'sent')
    time.sleep(2)
    print('packet',i,'recieved')

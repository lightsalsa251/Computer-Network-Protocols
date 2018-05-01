def binary(n,m):
    p = 0
    d = []
    for i in range(m-1,-1,-1):
        d.append(int(n[i])*pow(2,p))
        p+=1
    c = sum(d)
    return c



k = int(input('enter number of segments'))
m = int(input('enter size of each segment'))
a = []


for i in range(k):
    item = input()
    a.append(item)
b = []



for i in range(k):
    b.append(binary(a[i],m))
print(b)


w = sum(b)

def ones_complement(x):
    return x ^ ((1 << x.bit_length()) - 1)
w1 = ones_complement(w)
print(w1)

print('At reciever side')
e = sum(b) + k
q = ones_complement(e)

print(q)

print('introducing error')

e = b[0]%m
print(e)
item = list(a[0])

p = 0
for i in item:
    if p==e and i=='0':
        i='1'
    elif p==e and i=='1':
        item[e]='0'
        print('changed')
    p+=1
j = ''
for i in range(m):
    j+=item[i]
a[0] = j

b = []
for i in range(k):
    print(a[i])
    b.append(binary(a[i],m))
print(b)

w = sum(b)
print('At reciever side')
e = sum(b) + w1
q = ones_complement(e)

print(q if q==0 else 'error')
#FTP and telnet

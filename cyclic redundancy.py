def binary_to_decimal(n,m):
    p = 0
    d = []
    for i in range(m-1,-1,-1):
        d.append(int(n[i])*pow(2,p))
        p+=1
    c = sum(d)
    return c

m = int(input('enter length of dividend'))
c = int(input('enter length of divisor'))
a = []
b = []
for i in range(m):
    item = int(input())
    a.append(item)
for i in range(c):
    item = int(input())
    b.append(item)
for i in range(c-1):
    a.append(0)

q = binary_to_decimal(a,m)
p1 = binary_to_decimal(b,c)

n = q%p1

q = n//2

p = n
d = []
for i in range(c-1):
    d.append(p%2)
    p = p//2
print(a)
for i in range(1,c):
    a[m+c-1-i] = d[i-1]

print('sending to sender   ',a)

a = binary_to_decimal(a,m+c-1)
a = a%p1
if a==0:
    print('no error')
else:
    print('error')

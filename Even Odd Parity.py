e = 0
for i in range(10000):
    a = [i%2,0,0,i%2,1,1,0,i%2]
    ones = a.count(1)
    if ones%2==1:
        e+=1
print(e/100,'\t error rate')

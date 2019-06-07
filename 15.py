k1=input()
l1=k1.lower()
m1=0
n1=0
for i in range(len(k1)):
    if l1.count(l1[i])>m1:
        m1=l.count(l1[i])
        n1=i
print(k1[n1])

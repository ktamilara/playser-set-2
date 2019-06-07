a5,b5=map(int,input().split())
d5=[]
for i in range (1,b5+1):
    if a5%i==0 and b5%i==0:
        d5.append(i)
print(d5[-1])

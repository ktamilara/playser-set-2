v1,w1=map(int,input().split())
x3=v*w
b1=[]
for i in range(1,x3+1):
    if i%v1==0 and i%w1==0:
        b1.append(i)
print(min(b1))

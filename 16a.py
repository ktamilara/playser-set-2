x=int(input())
y=[]
y=input().split()
for i1 in range(len(y)):
    if y.count(y[i1])==1:
        print(y[i1])
        break

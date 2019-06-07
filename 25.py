r5=int(input())
l5=list(map(str,input().split()))
q5=sorted(l5,key=len)
for i in range(len(q5)-1):
    if len(q5[i])==len(q5[i+1]) and q5[i]>q5[i+1]:
        q5[i],q5[i+1]=q5[i+1],q5[i]
print(*q5)

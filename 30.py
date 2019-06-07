n5,m5,l=input().split()
c5=0
for i5,j5 in zip (n5,m5):
    if(i5!=j5):
        c5+=1
if(c5==int(l)):
    print("yes")
else:
    print("no")

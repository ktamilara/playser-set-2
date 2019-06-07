d1=int(input())
e2=2
l1=[]
v1=[]
for e2 in range(e2,d1+1):
  i=2
  while i<e2:
    if e2%i==0:
      break
    i=i+1
  if e2==i:
    l.append(e2)
for i in l1:
  if d1%i==0:
    v.append(i)
for i in range(0,len(v1)-1):
  print(v1[i],end=" ")
print(v1[len(v1)-1])

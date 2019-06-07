nm3=int(input())
listval1=list1(map(int,input().split()))
for x in listval1:
    if listval1.count(x)==1:
      print(x)

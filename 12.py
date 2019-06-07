x1,y = map(int,input().split())
y = y%x1
l = list(map(int,input().split()))
l1 = l[-y:] + l[:-y]
print(*l2)

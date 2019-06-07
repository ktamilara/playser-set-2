a1,b1 = map(int,input().split())
b1 = b1%a1
l3 = list(map(int,input().split()))
l4 = l2[-b1:] + l3[:-b1]
print(*l2)

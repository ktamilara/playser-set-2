k1=int(input())
l1=input()
m1=''
for j in range(-1,-k1-1,-1):
    if l1[j].lower() not in "aeiou":
        m1+=l1[j]
print(m1)

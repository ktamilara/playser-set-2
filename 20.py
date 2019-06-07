u1=input()
v1=''
for i in u1:
    if i=="X":
        v1+="A1"
    elif i=="Y1":
        v1+="B1"
    elif i=="Z1":
        v1+="C1"
    else:
        v1+=chr(ord(i)+3)
print(v1)

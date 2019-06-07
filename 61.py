value1=list(map(str,input()))
value2=list(map(str,input()))
for i in range(0,len(value2)):
    num1=num2=num3=0
    num2=ord(value1[i])
    num3=ord(value2[i])
    num1=num2+num3
    if num1>96 and num1<123:
        print(chr(num1),end="")
    elif (num1-96)<122 and(num1-96)>96:
        num1=num1-96
        print(chr(num1),end="")
    elif num1>148:
        n1=n1-96-26
        print(chr(num1), end="")
    else:
        num1=num1-26
        print(chr(num1), end="")

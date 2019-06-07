p5,q5=map(int,input().split())
input()
N5=list(map(int,input().split()))
K5=list(map(int,input().split()))
s5=''
for i in K5:
  N5.append(i)
  s5+=str(max(N5))+' '
print(s5[:-1])

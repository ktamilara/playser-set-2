s3=input()
m1=list(s3)
dict = {j:m1.count(j) for j in m1}
maxim = max(dict, key=dict.get)  
print(maxim)

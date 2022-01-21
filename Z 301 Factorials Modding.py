a,b,m=map(int,input().split())
prod=1
for i in range(a,b,-1):
    prod*=i
x=prod%m
print(x)

s=str(input())
n=len(s)
ans=(n)*(n-1)//2
 
l='abcdefghijklmnopqrstuvwxyz'
#print(ans)
for j in range(26):
    cnt=s.count(str(l[j]))
    ans-=cnt*(cnt-1)//2
print(ans+1)

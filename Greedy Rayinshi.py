n = int(input())
arr = list(map(int, input().split()))
begin = 0 
end = n-1
itr = 0
play1=0
play2=0
while(begin<=end):
    if(arr[begin]>=arr[end]):
        max = arr[begin]
        begin+=1
    else:
        max=arr[end]
        end-=1
    if(itr%2==0):
        play1 = play1+max
    else:
        play2 = play2+max
    itr+=1

print(play1, play2)

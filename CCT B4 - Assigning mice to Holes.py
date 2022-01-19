def assignHole(mices, holes, n, m):
    if (n != m):
        return -1
    mices.sort()
    holes.sort()
    
    Max = 0 
    
    for i in range(n):
        if (Max < abs(mices[i] - holes[i])):
            Max = abs(mices[i] - holes[i])
    
    return Max

if __name__=="__main__":
    n = int(input())
    mices = list(map(int, input().split()))
    holes = list(map(int, input().split()))
    x = len(mices)
    y = len(holes)
    minTime = assignHole(mices, holes, x,y)
    print(minTime)

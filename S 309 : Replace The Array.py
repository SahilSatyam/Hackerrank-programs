def next_g(arr):
    size = len(arr)
    max_from_right = arr[size-1]
    arr[size-1] = 0
    for i in range(size-2,-1,-1):
        temp = arr[i]
        arr[i]=max_from_right
        if max_from_right< temp:
            max_from_right=temp
def printArray(arr):
    for i in range(0,len(arr)):
        print (arr[i],end=" ")

n = int(input())
arr = list(map(int, input().split()))
next_g(arr)
printArray(arr)

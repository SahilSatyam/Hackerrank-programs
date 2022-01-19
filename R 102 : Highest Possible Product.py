n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(max(arr[0] * arr[1] * arr[n - 1], arr[n - 1] * arr[n - 2] * arr[n - 3]))

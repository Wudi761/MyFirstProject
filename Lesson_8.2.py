n = int(input())
arr = list(map(int, input().split()))

if n > 1:
    last = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

print(' '.join(map(str, arr)))
        
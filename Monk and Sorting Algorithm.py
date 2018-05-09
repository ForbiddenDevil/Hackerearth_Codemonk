n = int(input())
arr = list(map(int, input().strip().split(" ")))
max_arr = max(arr)
mul = 1
r = 10**5
while max_arr:
    arr.sort(key = lambda x: (x/mul)%r)
    print(' '.join(map(str, arr)))
    mul *= r
    max_arr //= r

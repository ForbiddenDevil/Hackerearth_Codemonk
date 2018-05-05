for _ in range(int(input())):
    n, k = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    k = k%n
    arr = arr[n-k:] + arr[:n-k]
    print(*arr)

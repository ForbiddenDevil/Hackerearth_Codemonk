n, k = map(int, input().strip().split(" "))
arr = list(map(int, input().strip().split(" ")))
a = []
for i, j in enumerate(arr):
    #print(i, j)
    mod = j % k
    a.append((i, j, mod))
a.sort(key = lambda x: x[2])
for i in a:
    print(i[1], end = ' ')

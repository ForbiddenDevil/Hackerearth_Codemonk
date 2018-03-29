n = int(input())
A = list(map(int, input().strip().split(" ")))
B = list(map(int, input().strip().split(" ")))
C = []
for i in range(n):
    C.append(A[i] + B[i])
print(*C)

import sys
input = sys.stdin.readline

n = int(input())
ans = [1 for _ in range(n+1)]
check = [False for _ in range(n+1)]

cur =2
for i in range(2,n+1):
    if check[i]:
        continue
    kk = False
    for j in range(i, n+1, i):
        if not check[j]:
            kk = True
            ans[j] = cur
            check[j] = True
    if kk:
        cur += 1
print(cur-1)
print(*ans[1:])
import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

val = sys.maxsize
ans = []


for i in range(n-2):
    fixed = a[i]
    st, end = i+1, n-1
    while st < end:
        cur = fixed + a[st] + a[end]
        if abs(cur) < abs(val):
            ans = [fixed,a[st],a[end]]
            val = cur
            if cur == 0:
                print(*ans)
                exit()

        if cur > 0:
            end -= 1
        else:
            st += 1
print(*ans)
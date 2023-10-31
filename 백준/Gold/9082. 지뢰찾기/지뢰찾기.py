import sys
from heapq import heappop,heappush
input = sys.stdin.readline

T = int(input())
for __ in range(T):
    n = int(input())
    Q = []
    cnt = [int(i) for i in input().strip()]
    a = list(str(input().strip()))
    ans = 0
    for i in range(n):
        if a[i] == "*":
            for idx in (i-1,i,i+1):
                if 0 <= idx < n:
                    cnt[idx] -= 1
            ans += 1
    #
    for i in range(n):
        if a[i] == "#":
            key = False
            for idx in (i,i+1,i-1):
                if 0 <= idx < n:
                    if cnt[idx] <= 0:
                        key = True
            if key:
                continue
            for idx in (i,i+1,i-1):
                if 0 <= idx < n:
                    cnt[idx] -= 1
            ans +=1
            a[i] = "*"
            
    ans += sum(cnt)//2
    print(ans)


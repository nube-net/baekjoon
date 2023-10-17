import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
case = set()
for i in range(m):
    case.add(a[i])
    for j in range(i+1,m):
        case.add(a[i]+a[j])

dp = [10001 for _ in range(n+1)]
dp[0] = 0

for _ in range(n):

    for i in range(n,-1,-1):
        if dp[i] != 10001:
            for c in case:
                if i+c > n:
                    continue
                dp[i+c] = min(dp[i+c],dp[i]+1)
    if dp[-1] != 10001:
        break
if dp[-1] != 10001:
    print(dp[-1])
else:
    print(-1)
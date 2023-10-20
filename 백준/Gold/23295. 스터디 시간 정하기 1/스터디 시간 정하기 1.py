import sys
input = sys.stdin.readline

n, T = map(int, input().split())

dp = [0 for _ in range(100001)]

for _ in range(n):
    k = int(input())
    for __ in range(k):
        a, b = map(int, input().split())
        dp[a] += 1
        dp[b] -= 1
for i in range(1,100001):
    dp[i] = dp[i-1]+dp[i]
ans = -1
ans2 = [0,T]
for i in range(100001-T):
    if i == 0:
        ans = sum(dp[:T])
        tmp = ans
    else:
        tmp -= dp[i-1]
        tmp += dp[i+T-1]
        if ans < tmp:
            ans = tmp
            ans2[0] = i
            ans2[-1] = i+T
print(*ans2)

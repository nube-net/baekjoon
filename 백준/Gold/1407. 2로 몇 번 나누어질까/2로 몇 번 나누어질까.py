import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num[0] -= 1
ans = []
for a in num:
    tmp, tmp2, d = 0, 0, 1
    while a > 0: # 2로 나눈 후 남은 홀수 처리 
        tmp = a//2 + a%2
        tmp2 += tmp * d
        a -= tmp
        d *= 2
    ans.append(tmp2)
print(ans[1]-ans[0])
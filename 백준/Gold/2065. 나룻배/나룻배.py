import sys
from collections import deque
input = sys.stdin.readline

m, T, n = map(int, input().split())

a = [deque(),deque()]
for i in range(n):
    t, loc = map(str, input().split())
    loc = loc.strip()

    if loc == "right":
        a[1].append([int(t),i])  # 도착 시간, 입력 순서
    else:
        a[0].append([int(t), i])

idx = 0  # 0 = left, 1 = right
cur = 0  # 현재 시간
boat = []
ans = [0 for _ in range(n)]

while a[0] or a[1]:
    # 1.위치 및 시간 조정
    if a[0] and a[1]:
        if cur < a[0][0][0] and cur < a[1][0][0]:  # 가능한 손님이 없을 경우
            if a[idx][0][0] > a[abs(idx-1)][0][0]:
                cur = a[abs(idx-1)][0][0]+T
                idx = abs(idx-1)
            else:
                cur = a[idx][0][0]
    else:
        if a[idx]:
            cur = max(a[idx][0][0],cur)
        else:
            cur = max(a[abs(idx - 1)][0][0] + T,cur+T)
            idx = abs(idx - 1)

    # print(f"cur = {cur}, idx = {idx}")
    # 2. 현재 위치 손님 수용
    while a[idx] and len(boat) < m:
        if a[idx][0][0] <= cur:
            boat.append(a[idx].popleft())
        else:
            break

    # 3. 이동 및 손님 하차
    cur += T
    idx = abs(idx - 1)
    while boat:
        _, i = boat.pop()
        ans[i] = cur
    # print(ans, idx)

for i in ans:
    print(i)
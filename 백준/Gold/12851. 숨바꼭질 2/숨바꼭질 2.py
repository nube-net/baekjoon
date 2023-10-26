import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [sys.maxsize for _ in range(100001)]
visited[N] = 0
Q = deque()
Q.append(N)
cnt = 0

while Q:
    a = Q.popleft()
    if a == K:
        cnt += 1
    if 0 <= a+1 <= 100000:
        if visited[a+1] > visited[a] or visited[a+1] == sys.maxsize :
            visited[a+1] = visited[a] + 1
            Q.append(a+1)
    if 0 <= a-1 <= 100000:
        if visited[a-1] > visited[a] or visited[a-1] == sys.maxsize :
            visited[a-1] = visited[a] + 1
            Q.append(a-1)

    if 0 <= a*2 <= 100000:
        if visited[a*2] > visited[a] or visited[a*2] == sys.maxsize :
            visited[a*2] = visited[a] + 1
            Q.append(a*2)


print(visited[K])
print(cnt)
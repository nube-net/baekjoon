import sys
from collections import deque
input = sys.stdin.readline

n, k = map(str, input().rstrip().split())
k = int(k)

q = deque()
l = len(n)
if l == 1:
    print(-1)
    exit()
q.append(n)
for _ in range(k):
    if q:
        visited = set()

        for __ in range(len(q)):
            tmp = q.popleft()
            for i in range(l-1):
                for j in range(i+1,l):
                    cur = list(tmp)
                    cur[i],cur[j] = cur[j],cur[i]
                    s = "".join(cur)
                    if s[0] == "0":
                        continue
                    if s in visited:
                        continue
                    else:
                        visited.add(s)
                        q.append(s)
    else:
        print(-1)
        exit()
if q:
    ans = max(q)
    if len(ans) == l:
        print(ans)
    else:
        print(-1)
else:
    print(-1)

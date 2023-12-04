import heapq
import sys
input = sys.stdin.readline
# 우사코가이드 코드로 공부중
def prim(n, G):
    used = [False for _ in range(n)]
    pq = [(0, 0)]
    total_weight = 0
    count = 0
    while pq:
        weight, node = heapq.heappop(pq)
        if used[node]:
            continue
        used[node] = True
        total_weight += weight
        count += 1
        for (neigh_weight, neigh_node) in G[node]:
            if not used[neigh_node]:
                heapq.heappush(pq, (neigh_weight, neigh_node))
    return total_weight if count == n else -1

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((c, b))
    G[b].append((c, a))

ans = prim(n, G)
print(ans)

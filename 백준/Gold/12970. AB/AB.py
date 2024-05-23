import  sys
input = sys.stdin.readline

n, k = map(int,input().split())
d = n//2
r = d
if n%2:
    d +=1

# 가능한 최대 경우의 수 보다 큰 경우
if d*r < k:
    print(-1)
    exit()

l = (k//r)+r
a = k%r
if a:
    l += 1
# len(tmp) + len(Q) + len(R) = n
Q = ['A' for _ in range(k//r)]  # 몫
R = []  # 나머지
tmp = ['B' for _ in range(n-l)]  # 쓰지 않는 공간
if a:
    for _ in range(a):
        R.append('B')
    R.append('A')
for _ in range(n-(len(Q)+len(R)+len(tmp))):
    R.append('B')
for i in tmp:
    print(i, end="")
for i in Q:
    print(i,end="")
for i in range(len(R)-1,-1,-1):
    print(R[i],end="")






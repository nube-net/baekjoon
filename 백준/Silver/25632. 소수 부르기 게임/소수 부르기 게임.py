a, b = map(int, input().split())
tmp = [1] * (b + 1)
tmp[0] = 0
tmp[1] = 0
for k in range(2, int(b ** 0.5) + 1):
    if tmp[k] == 1:
        for i in range(k * 2, b + 1, k):
            tmp[i] = 0
A = set()
for p in range(a, b + 1):
    if tmp[p] == 1:
        A.add(p)
a, b = map(int, input().split())
tmp = [1] * (b + 1)
tmp[0] = 0
tmp[1] = 0
for k in range(2, int(b ** 0.5) + 1):
    if tmp[k] == 1:
        for i in range(k * 2, b + 1, k):
            tmp[i] = 0
B = set()
for p in range(a, b + 1):
    if tmp[p] == 1:
        B.add(p)
C = A & B

a = len(A) + len(C)%2 -len(C)
b = len(B) -len(C)
if a> b:
    print('yt')
else:
    print('yj')


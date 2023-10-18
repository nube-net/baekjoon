import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

st = 1
end = n*n
for i in range(31622):
    st += 1
    if st**2 > k:
        st -=1
        break
while True:
    if st > end:
        break
        
    mid = (st + end) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid//i, n)

    if cnt < k:
        st = mid + 1
    else:
        end = mid - 1
print(st)
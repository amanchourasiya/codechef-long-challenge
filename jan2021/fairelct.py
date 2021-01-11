t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    swap = 0
    s1 = sum(A)
    s2 = sum(B)

    if s1 > s2:
        print(0)
        continue
    
    A.sort()
    B.sort()

    i = n if n<m else m

    for j in range(i):
        s1 = s1 - A[j] + B[m-1-j]
        s2 = s2 - B[m-1-j] + A[j]
        swap+=1
        if s1 > s2:
            break
    
    if s1 > s2:
        print(swap)
    else:
        print(-1)
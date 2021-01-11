t = int(input())

for _ in range(t):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    total_problems = sum(a)
    res = total_problems // k

    if res > d:
        res = d

    print(res)
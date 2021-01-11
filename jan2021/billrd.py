t = int(input())

for _ in range(t):
    n,k,x,y = list(map(int, input().split()))
     
    # Handle corners
    if x == y:
        print(n,n)
        continue

    # Handle cases for boundary starting point

    # Handle Normal case
    k = k % 4
    # Search for all possible points
    impacts = []
    if x>y:  # it will hit right edge first
        impacts.append([n,y + n-x]) # right
        impacts.append([y +n-x,n])  # top
        impacts.append([0, x-y])    # left
        impacts.append([x-y,0])     # bottom
    else:
        impacts.append([x +n-y,n])
        impacts.append([n,x + n-y])
        impacts.append([y-x,0])
        impacts.append([0, y-x])
    
    print(impacts[k-1][0], impacts[k-1][1])

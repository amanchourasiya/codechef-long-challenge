db = {}
k = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o', 'p']

def getKey(encodedStr, k, start, end):
    #print('start end', start, end)
    if len(encodedStr) == 1:
        return k[start] if encodedStr == '0' else k[end]
    
    mid = (end+start) //2
    if encodedStr[0] == '0':
        end = mid
    else:
        start = mid +1

    return getKey(encodedStr[1:],k ,start, end)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    n = n // 4
    start = 0
    end = 4
    #global db 
    for i in range(n):
        st = s[start:end]
        c = db.get(st, -1) 
        if  c == -1:
            c = getKey(st, k, 0, 15)
            db[st] = c
        print(c, end = '')
        start = start +4
        end = end +4
        
            
    print()
        


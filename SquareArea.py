n = int(input())
 
for i in range(n):
    pointsx = []
    pointsy = []
    for l in range(4):
        
        x,y = map(int, input().split())
        pointsx.append(x)
        pointsy.append(y)
    xdis = max(pointsx)-min(pointsx)
    ydis = max(pointsy)-min(pointsy)
    print(xdis * ydis)
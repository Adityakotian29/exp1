INF = float('inf')

def floyd(lmao):
    x=len(lmao)
    dist=[[0]*x for i in range(x)]
    for i in range(x):
        for j in range(x):
            dist[i][j]=lmao[i][j]
            
            
    for k in range(x):
        for i in range (x):
            for j in range (x):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    return dist                     
            


lmao = [
        [0, 2, INF, 4],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [5, INF, INF, 0]
    ]
print(floyd(lmao))
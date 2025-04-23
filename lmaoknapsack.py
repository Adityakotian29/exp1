def Knapsack(b,w,W,n):
    S=set()
    for i in range(n):
        S.add((b[i],w[i]))
    
    M=[[0 for j in range(W+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            if w[i-1]>j:
                M[i][j]=M[i-1][j]
            else:
                M[i][j]=max(M[i-1][j],M[i-1][j-w[i-1]]+b[i-1])    
    
    I=set()
    k=W
    for i in range(n,0,-1):
        if M[i-1][k]==M[i][k]:
            continue            
        else:
            I.add(i)
            k=k-w[i-1]
    
    print("Max Profit =",M[n][W])         
    print("Items picked =",I)
    
Knapsack([1,2,4,2,5],[1,2,3,3,5],10,5)
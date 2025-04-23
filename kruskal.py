def kruskal(edges, vertices):
    edges.sort(key=lambda x: x[2])
    parent = {i: i for i in vertices}
    print(parent)

    mst = []
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    def union(u, v):
        parent[find(v)] = find(u)
    for u, v, w in edges:
        if find(u) != find(v):
            mst.append((u, v, w))
            union(u, v)
    
    return mst
lmao = [(0, 1, 3), (0, 2, 2), (0, 3, 5), (1, 3, 1), (1, 4, 4), (2, 3, 2), (5, 6, 6)]
# Set of vertices
ded= {0, 1, 2, 3, 4, 5, 6}

mst = kruskal(lmao,ded)
print("Edges of Minimum Spanning Tree:")
for i in mst:
    print(i)

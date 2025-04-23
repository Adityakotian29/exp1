def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [float('infinity')] * num_nodes
    distances[start] = 0
    visited = [False] * num_nodes
    
    for _ in range(num_nodes):
        min_distance = float('infinity')
        min_index = -1
        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i
        
        visited[min_index] = True
        for i in range(num_nodes):
            if graph[min_index][i] > 0 and not visited[i]:
                distance = distances[min_index] + graph[min_index][i]
                if distance < distances[i]:
                    distances[i] = distance
    
    return distances


lmao = [
    [0, 3, 2, 0],
    [3, 0, 1, 7],
    [2, 1, 0, 5],
    [0, 7, 5, 0]
]

start_node = 0  
distances = dijkstra(lmao, start_node)

print("Shortest distances from node", start_node)
for node, distance in enumerate(distances):
    print("To node", node, ":", distance)

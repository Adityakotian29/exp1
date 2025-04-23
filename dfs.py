def dfs(graph, start, goal):

    if start == goal:
        return [start]
    
   
    for neighbor in graph.get(start, []):
        path = dfs(graph, neighbor, goal)
        
    
        if path:
            return [start] + path
    

    return None


graph = {
        'A': ['M', 'B', 'C'],
        'B': ['D'],
        'C': [],
        'D': ['X', 'Y'],
        'Y': ['G']
    }
    
result = dfs(graph, 'A', 'G')
print("Path to goal:", result if result else "Goal not found")

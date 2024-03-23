import sys
from collections import deque

# Define the graph as an adjacency list
graph = {
    'SFO': ['CDG','TYO','EZE','MEX'],
    'TOR': ['YYZ','BOS','JFK'],
    'TYO': ['SFO', 'MEL'],
    'MEX': ['SFO','MTY','TOR','ACA','BOS'],
    'MTY': ['MEX'],
    'MEL': ['MEL','TYO', 'MEX'],
    'ACA': ['SLP','TYO','MEX'],
    'SLP': ['MEX'],
    'YYZ': ['MEX']
}
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# Example usage
start_state = sys.argv[1]
#start_state = 'ACA'
goal_state = sys.argv[2]
#goal_state = 'CDG'
path = bfs(graph, start_state, goal_state)

if path:
    print("Path found:", ' -> '.join(path))
else:
    print("No path found from", start_state, "to", goal_state)

import random
from collections import deque

def generate_random_graph(n, p):
    """
    Generates a random graph with 'n' nodes.
    Each potential edge between nodes has a 'p' probability of being present.
    """
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def spawn_cat_mouse(graph):
    """Spawns the cat on a random node and the mouse on one of its neighbors."""
    cat = random.choice(list(graph.keys()))
    mouse = random.choice(graph[cat])
    return cat, mouse

def bfs_shortest_path(graph, start, end):
    """Finds the shortest path from 'start' to 'end' using BFS."""
    visited = {node: False for node in graph}
    prev_nodes = {node: None for node in graph}
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                prev_nodes[neighbor] = node
                
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev_nodes[at]
    return path[::-1]

def cat_strategy(cat, mouse, graph):
    """Determines the next move for the cat using BFS to move closer to the mouse."""
    path = bfs_shortest_path(graph, cat, mouse)
    return path[1]

import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(n, p):
    """
    Generate a random graph using the Erdős-Rényi G(n, p) model.
    n: Number of nodes
    p: Probability of creating an edge between any two nodes
    """
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):  # Avoid loops and double-counting edges
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)  # Since it's an undirected graph
    
    return graph

def visualize_graph(graph):
    """
    Visualize the generated graph using networkx.
    graph: Graph as adjacency list
    """
    G = nx.Graph(graph)
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500)
    plt.show()

# Example usage:
n = 15  # 10 nodes
p = 0.4  # 50% probability of creating an edge
graph_structure = generate_random_graph(n, p)
visualize_graph(graph_structure)

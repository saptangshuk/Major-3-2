import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import erdos_renyi_graph
class GraphVisualization:

	def __init__(self):
		self.visual = []

	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
		
	def visualize(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()

G = GraphVisualization()
n = 6
p = 0.5
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()

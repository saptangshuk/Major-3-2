import networkx as nx
import tkinter as tk
import matplotlib.pyplot as plt

n=10
p=0.4
G= nx.erdos_renyi_graph(n,p)
nx.draw(G, with_labels=True)
plt.show()

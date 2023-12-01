import random
import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_random_graph(n, p):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def spawn_cat_mouse(graph):
    cat = random.choice(list(graph.keys()))
    mouse = random.choice([node for node in graph[cat] if node != cat])
    return cat, mouse

def cat_strategy(cat, mouse, graph):
    if mouse in graph[cat]:
        return mouse
    mouse_neighbors = set(graph[mouse])
    cat_neighbors = set(graph[cat])
    closer_nodes = mouse_neighbors.intersection(cat_neighbors)
    if closer_nodes:
        return random.choice(list(closer_nodes))
    return random.choice(list(graph[cat]))

def visualize_game_state(graph, cat, mouse, pos):
    G = nx.Graph(graph)
    fig, ax = plt.subplots(figsize=(6, 4))
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=500, nodelist=[cat], node_color='lightblue')
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=500, nodelist=[mouse], node_color='brown')
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=500, nodelist=set(graph.keys()) - {cat, mouse}, node_color='gray')
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')
    nx.draw_networkx_labels(G, pos, ax=ax)
    plt.axis('off')
    return fig

class GameApp(tk.Tk):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.cat, self.mouse = spawn_cat_mouse(graph)
        self.mouse_prev = None
        G = nx.Graph(graph)
        self.pos = nx.spring_layout(G)
        self.title("Cat & Mouse Game")
        
        self.attributes('-fullscreen', True)  # Making it fullscreen
        
        tk.Label(self, text="Cat & Mouse Game", font=("Arial", 24)).pack(pady=20)
        
        self.status_frame = tk.Frame(self)
        self.status_frame.pack(pady=10)
        tk.Label(self.status_frame, text="Cat:").grid(row=0, column=0, padx=10)
        self.cat_label = tk.Label(self.status_frame, text=self.cat)
        self.cat_label.grid(row=0, column=1, padx=10)
        
        tk.Label(self.status_frame, text="Mouse:").grid(row=1, column=0, padx=10)
        self.mouse_label = tk.Label(self.status_frame, text=self.mouse)
        self.mouse_label.grid(row=1, column=1, padx=10)

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(pady=20, fill=tk.BOTH, expand=1)
        self.fig = visualize_game_state(self.graph, self.cat, self.mouse, self.pos)
        self.canvas = FigureCanvasTkAgg(self.fig, self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10, fill=tk.X)
        self.update_buttons()

    def generate_button_command(self, move):
        return lambda: self.move_mouse(move)

    def update_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        valid_moves = [move for move in self.graph[self.mouse] if move != self.mouse_prev and move != self.cat]
        for move in valid_moves:
            btn = tk.Button(self.button_frame, text=f"Move to {move}", font=("Arial", 18), command=self.generate_button_command(move))
            btn.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=1)

    def move_mouse(self, move):
        self.mouse_prev = self.mouse
        self.mouse = move
        self.update_game_state()
        self.after(1000, self.move_cat)

    def move_cat(self):
        self.cat = cat_strategy(self.cat, self.mouse, self.graph)
        self.update_game_state()
        if self.cat == self.mouse:
            messagebox.showinfo("Game Over", "Cat caught the Mouse!")
            self.quit()

    def update_game_state(self):
        self.cat_label.config(text=self.cat)
        self.mouse_label.config(text=self.mouse)
        
        self.fig = visualize_game_state(self.graph, self.cat, self.mouse, self.pos)
        self.canvas.figure = self.fig
        self.canvas.draw()
        self.update_buttons()

if __name__ == "__main__":
    n = 10
    p = 0.5
    game_graph = generate_random_graph(n, p)
    app = GameApp(game_graph)
    app.mainloop()

import matplotlib.pyplot as plt
import networkx as nx

# Create a new directed graph
G = nx.DiGraph()

# Add nodes with their roles as labels
nodes = {
    "Medical Staff": {"type": "person"},
    "Patient": {"type": "person"},
    "Logistics Staff": {"type": "person"},
    "Sanitation Staff": {"type": "person"},
    "Hospital Management": {"type": "person"},
    "Administrative Staff": {"type": "person"},
    "Electronic Medical Record System": {"type": "system"},
    "Hospital Management System": {"type": "system"},
    "Insurance and Billing Systems": {"type": "system"}
}

for node, attr in nodes.items():
    G.add_node(node, **attr)

# Define the connections between nodes
edges = [
    ("Medical Staff", "Electronic Medical Record System"),
    ("Patient", "Electronic Medical Record System"),
    ("Patient", "Hospital Management System"),
    ("Logistics Staff", "Hospital Management System"),
    ("Sanitation Staff", "Hospital Management System"),
    ("Hospital Management", "Hospital Management System"),
    ("Administrative Staff", "Hospital Management System"),
    ("Hospital Management System", "Insurance and Billing Systems"),
    ("Electronic Medical Record System", "Hospital Management System"),
]

G.add_edges_from(edges)

# Define node colors based on type
node_colors = ["blue" if G.nodes[node]["type"] == "person" else "red" for node in G.nodes]

# Draw the network
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3500, font_size=10, font_weight='bold', edge_color="black")

# Show the plot
plt.show()

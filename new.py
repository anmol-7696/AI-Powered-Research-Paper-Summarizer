import pandas as pd
import matplotlib.pyplot as plt

# Sample Data (Replace with your CSV file)
data = {
    "Source": ["A", "A", "B", "C", "D", "E", "E"],
    "Target": ["Bat", "C", "D", "E", "E", "F", "G"]
}

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Extract unique nodes
nodes = pd.concat([df["Source"], df["Target"]]).unique()

# Create a position mapping for visualization
node_positions = {node: (i, len(nodes) - i) for i, node in enumerate(nodes)}

# Plot the Graph
plt.figure(figsize=(10, 10))

for _, row in df.iterrows():
    source, target = row["Source"], row["Target"]
    x_values = [node_positions[source][0], node_positions[target][0]]
    y_values = [node_positions[source][1], node_positions[target][1]]
    plt.plot(x_values, y_values, 'k-', alpha=0.5)  # Edges

# Plot Nodes
for node, (x, y) in node_positions.items():
    plt.scatter(x, y, s=200, c='lightblue', edgecolors='black', zorder=3)
    plt.text(x, y, node, fontsize=12, ha='center', va='center', fontweight='bold')

plt.title("Graph Representation Using Pandas")
plt.axis("off")
plt.show()


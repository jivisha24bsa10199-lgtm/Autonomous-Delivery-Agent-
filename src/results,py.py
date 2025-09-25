import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to metrics file
csv_file = os.path.join("results", "plots", "metrics.csv")

# Add column names explicitly (since your file has no header row)
columns = ["Algorithm", "Map", "PathLength", "Cost", "NodesExpanded", "Runtime"]

df = pd.read_csv(csv_file, names=columns)

# Ensure plots directory exists
os.makedirs("results/plots", exist_ok=True)

# --- Runtime Comparison ---
plt.figure()
for algo in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algo]
    plt.plot(subset["Map"], subset["Runtime"], marker="o", label=algo)
plt.x_label("Map")
plt.y_label("Runtime (s)")
plt.title("Runtime Comparison")
plt.legend()
plt.savefig("results/plots/runtime_comparison.png")

# --- Nodes Expanded ---
plt.figure()
for algo in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algo]
    plt.plot(subset["Map"], subset["NodesExpanded"], marker="o", label=algo)
plt.x_label("Map")
plt.y_label("Nodes Expanded")
plt.title("Comparison")
plt.legend()
plt.savefig("results/plots/nodes_expanded.png")

# --- Path Cost ---
plt.figure()
for algo in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algo]
    plt.plot(subset["Map"], subset["Cost"], marker="o", label=algo)
plt.xlabel("Map")
plt.ylabel("Path Cost")
plt.title("Path Cost Comparison")
plt.legend()
plt.savefig("results/plots/path_cost.png")

print("✅ Plots generated in results/plots/")

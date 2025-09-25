Autonomous-Delivery-Agent

Autonomous Delivery Agent Simulation

This work includes a simulation of an independent delivery agent in the grid world. There is a dynamic world, and an agent that needs to navigate the world efficiently, collect packages and deliver them to their destinations. This simulation can be used to compare different path finding algorithms by tuning the environmental conditions.

Features

Grid Environnment- customable grid with different types of terrains (Asphalt, Field, Sludge, River), each have a cost in movement.

Static and Dynamic Obstacles: The environment model has static obstacles that prevent agent from passing through and dynamic obstacles, which moves along respect to particular predefined trajectories.

Pathfinding Algorithms: Implementations of multiple searching algorithms for finding the best path between two points.

Breadth-First Search (BFS)

Uniform Cost Search (UCS)

A* Search (A_Star)

Simulated Annealing (SA)

Hill Climbing

Agent simulation: An agent having only limited fuel, which can pick up and drop off packages as well as adjust to unpredictable context changes (e.g., moving obstacles).

Performance: Utility scripts to run experiments and output plots that compare the performance of different algorithms on a range of metrics including runtime, path cost, and nodes expanded.

CLI interface: Easy CLI to do experiments, do maps and show the behaviour of the agent.

Project Structure

I have organized the project into a src directory to make it a Python package.

/AIML VITHYARTHI

├── src/

│ ├── init. py # 'src' becomes a Python package (so that it is importable)

│ ├── Agent. py # Delivery Agent definition

│ ├── ALGO. py # has routing alg implementations

│ ├── API. py # High-level interface for the simulation

│ ├── CLI. py # Console interface to run experiments

│ ├── environment. py # Grid/terrain and obstacles, etc.

│ └── UTILITY. py # Functions that aid in creating maps, and managing results

└── results/

├── plots/ # Directory where the generated plots will be saved.

└── metrics. csv # Experimental results data

Getting Started

Prerequisites

Python 3.6 or higher

pandas

matplotlib

numpy
You can install necessary packages via pip:

pip install pandas matplotlib numpy

Running the Simulation

To run the simulation, go to the root directory of the project (AIML VITHYARTHI) and use CLI. py script as a Python module.

Run a single experiment:

python -m src. CLI run --map medium --algorithm a_star

Run all experiments:

This will execute all algorithms on all pre-defined map sizes and save the results to a metrics. csv file.

python -m src. CLI run-all --output results/metrics. csv

Generate plots:

To use the results of your experiments after running them:results,py. py for visualizing plots of the performance. Note: Make sure you fix the case-sensitive import in that file first (like from. Algo import...).

python -m src.results,py

"""
Utility functions for the autonomous delivery agent project.
"""

import time
import json
import random
from typing import Dict, Any, List
from .environment import Grid, GroundType, Moving_Obstacle
from .AGENT import Delivery_Agent

def create_test_map(size: str) -> Grid:
    """
    Create a test map of the specified size.
    
    Args:
        size: Size of the map ("small", "medium", "large", or "dynamic")
        
    Returns:
        Grid object with the test map
    """
    if size == "small":
        grid = Grid(15, 15)
        # Add some obstacles
        for i in range(5, 9):
            grid.add_obstacle(i, 7)
        # Add different terrain
        for i in range(15):
            for j in range(5):
                grid.set_ground(i, j, GroundType.ASPHALT)
        for i in range(15):
            for j in range(9, 15):
                grid.set_ground(i, j, GroundType.SLUDGE)
                
    elif size == "medium":
        grid = Grid(22, 22)
        # Add obstacles in a cross pattern
        for i in range(6, 12):
            grid.add_obstacle(i, 9)
        for j in range(6, 12):
            grid.add_obstacle(9, j)
        # Add different terrain
        for i in range(22):
            for j in range(6):
                grid.set_ground(i, j, GroundType.ASPHALT)
        for i in range(22):
            for j in range(13, 22):
                grid.set_ground(i, j, GroundType.SLUDGE)
        for i in range(6):
            for j in range(22):
                grid.set_ground(i, j, GroundType.RIVER)
            
    elif size == "large":
        grid = Grid(55, 55)
        # Add random obstacles
        for _ in range(120):
            x = random.randint(0, 66)
            y = random.randint(0, 66)
            grid.add_obstacle(x, y)
        # Add different terrain in regions
        for i in range(66):
            for j in range(12):
                grid.set_ground(i, j, GroundType.ASPHALT)
        for i in range(55):
            for j in range(35, 66):
                grid.set_ground(i, j, GroundType.SLUDGE)
        for i in range(12):
            for j in range(66):
                grid.set_ground(i, j, GroundType.RIVER)
                
    elif size == "dynamic":
        grid = Grid(25, 25)
        # Add static obstacles
        for i in range(12, 18):
            grid.add_obstacle(i, 15)
        # Add a moving obstacle
        moving_path = [ (4,4) ,(4, 5), (4,6) , (5, 5), (6,5) , (5,6), (5, 4),(6,4) , (6,6)]
        moving_obstacle = Moving_Obstacle(3, 3, moving_path, speed=2)
        grid.add_moving_obstacle(moving_obstacle)
        # Add different terrain
        for i in range(25):
            for j in range(12):
                grid.set_terrain(i, j, GroundType.FIELD)
        
    else:
        raise ValueError(f"Unknown map size: {size}")
        
    return grid

def run_experiment(map_size: str, algorithm: str) -> Dict[str, Any]:
    """
    Run a delivery experiment with the specified map and algorithm.
    
    Args:
        map_size: Size of the map ("small", "medium", "large", or "dynamic")
        algorithm: Planning algorithm to use ("bfs", "ucs", "a_star", "sa")
        
    Returns:
        Dictionary with experiment results
    """
    grid = create_test_map(map_size)
    agent = Delivery_Agent(grid, 0, 0, fuel=10000)
    
    # Add package and destination based on map size
    if map_size == "small":
        agent.add_package(8, 7)
        agent.add_destination(3, 5)
    elif map_size == "medium":
        agent.add_package(15, 15)
        agent.add_destination(8, 6)
    elif map_size == "large":
        agent.add_package(35, 35)
        agent.add_destination(12, 12)
    elif map_size == "dynamic":
        agent.add_package(18, 18)
        agent.add_destination(9, 4)
    
    start_time = time.time()
    success = agent.deliver_packages(algorithm)
    end_time = time.time()
    
    return {
        "success": success,
        "path_cost": agent.path[-1].cost if success and hasattr(agent, 'path') and agent.path else float('inf'),
        "fuel_remaining": agent.fuel,
        "time_taken": end_time - start_time,
        "path_length": len(agent.path) if success and hasattr(agent, 'path') and agent.path else 0,
        "algorithm": algorithm,
        "map_size": map_size
    }

def save_results(results: List[Dict[str, Any]], filename: str):
    """
    Save experiment results to a JSON file.
    
    Args:
        results: List of experiment results
        filename: Output filename
    """
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

def load_results(filename: str) -> List[Dict[str, Any]]:
    """
    Load experiment results from a JSON file.
    
    Args:
        filename: Input filename
        
    Returns:
        List of experiment results
    """
    with open(filename, 'r') as f:
        return json.load(f)
"""
Tests for the planners module.
"""

import unittest
from src.environment import Grid, TerrainType
from src.Algo import BFS, UCS, A_Star, Simulated_Annealing , Hill_Climbing

class TestPathfinders(unittest.TestCase):
    """Test cases for path planning algorithms."""
    
    def setUp(self):
        """Set up a test grid."""
        self.grid = Grid(6, 6)
        # Add a simple obstacle
        self.grid.add_obstacle(3, 3)
        
    def test_bfs_pathfinder(self):
        """Test BFS path planning."""
        planner = BFS(self.grid)
        result = planner.plan(0, 0, 4, 4)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 2)
        
        # Check path length (should be 8 moves for a 5x5 grid with one obstacle)
        path = result.get_path()
        self.assertEqual(len(path), 9)  # Includes start position
        
    def test_ucs_pathfinder(self):
        """Test UCS path planning."""
        planner = UCS(self.grid)
        result = planner.plan(1, 1, 5, 5)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 4)
        
    def test_A_star_pathfinder(self):
        """Test A* path planning."""
        planner = A_Star(self.grid)
        result = planner.plan(0, 0, 4, 4)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 4)
        
    def test_simulated_annealing_pathfinder(self):
        """Test Simulated Annealing path planning."""
        planner = Simulated_Annealing(self.grid, max_iterations=100)
        result = planner.plan(1, 1, 3, 3)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 4)

    def test_Hill_Climbing_pathfinder(self):
        """Test Simulated Annealing path planning."""
        planner = Hill_Climbing(self.grid, max_iterations=100)
        result = planner.plan(1, 1, 5, 5)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 4)

if __name__ == "__main__":
    unittest.main()
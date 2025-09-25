"""
Command-line interface for the autonomous delivery agent.
"""
import json
from .api import system_api
import argparse
import sys
from .utils import run_experiment, save_results
from .environment import Grid
from .AGENT import DeliveryAgent

def api_command(args):
    """Handle API commands."""
    if args.api_command == "create-grid":
        result = system_api.create_grid(args.width, args.height)
    elif args.api_command == "load-grid":
        result = system_api.load_grid(args.filename)
    elif args.api_command == "add-obstacle":
        result = system_api.add_obstacle(args.x, args.y)
    # Add more commands as needed
    
    print(json.dumps(result, indent=2))

# Add API subparser to your main CLI

def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(description="Autonomous Delivery Agent")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Run experiment command
    experiment_parser = subparsers.add_parser("run", help="Run an experiment")
    experiment_parser.add_argument("--map", choices=["small", "medium", "large", "dynamic"], 
                                  required=True, help="Map size")
    experiment_parser.add_argument("--algorithm", choices=["bfs", "ucs", "a_star", "sa"],
                                  required=True, help="Planning algorithm")
    experiment_parser.add_argument("--output", help="Output file for results")
    
    # Run all experiments command
    all_parser = subparsers.add_parser("run-all", help="Run all experiments")
    all_parser.add_argument("--output", required=True, help="Output file for results")
    
    # Demo command
    demo_parser = subparsers.add_parser("demo", help="Run a demo with visualization")
    demo_parser.add_argument("--map", choices=["small", "medium", "large", "dynamic"],
                            default="dynamic", help="Map size")
    demo_parser.add_argument("--algorithm", choices=["bfs", "ucs", "a_star", "sa"],
                            default="a_star", help="Planning algorithm")
    
    args = parser.parse_args()
    
    if args.command == "run":
        result = run_experiment(args.map, args.algorithm)
        print(f"Experiment completed: {result}")
        
        if args.output:
            save_results([result], args.output)
            
    elif args.command == "run-all":
        results = []
        map_sizes = ["small", "medium", "large", "dynamic"]
        algorithms = ["bfs", "ucs", "a_star", "sa" , "hill"]
        
        for map_size in map_sizes:
            for algorithm in algorithms:
                print(f"Running {algorithm} on {map_size} map...")
                result = run_experiment(map_size, algorithm)
                results.append(result)
                print(f"Result: {result}")
                
        save_results(results, args.output)
        print(f"All experiments completed. Results saved to {args.output}")
        
    elif args.command == "demo":
        print("Running demo...")
        # This would typically include visualization
        # For now, we'll just run the experiment and print results
        result = run_experiment(args.map, args.algorithm)
        print(f"Demo completed: {result}")
        
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
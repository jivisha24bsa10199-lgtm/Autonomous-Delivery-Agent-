from collections import deque
import heapq
import math
import random


# ---------- BFS ----------
def BFS_path_finder(grid, origin, destination):
    queue = deque([origin])
    visited = set([origin])
    parent = {origin: None}
    nodes_expanded = 0

    while queue:
        x, y = queue.popleft()
        nodes_expanded += 1
        if (x, y) == destination:
            path = reconstruct_path(parent, destination)
            return path, len(path) - 1, nodes_expanded  # cost = steps

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + dx, y + dy
            if grid.is_valid(next_x, next_y, time=0) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                parent[(next_x, next_y)] = (x, y)
                queue.append((next_x, next_y))
    return None, float("inf"), nodes_expanded


# ---------- UCS ----------
def ucs(grid, origin, destination):
    priority_queue = [(0, origin)]
    visited = set()
    parent = {origin: None}
    cost_so_far = {origin: 0}
    nodes_expanded = 0

    while priority_queue:
        cost, (x, y) = heapq.heappop(priority_queue)
        nodes_expanded += 1
        if (x, y) == destination:
            path = reconstruct_path(parent, destination)
            return path, cost, nodes_expanded

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + dx, y + dy
            if grid.is_valid(next_x, next_y, time=0):
                new_cost = cost_so_far[(x, y)] + grid.get_cost(next_x, next_y)
                if (next_x, next_y) not in cost_so_far or new_cost < cost_so_far[(next_x, next_y)]:
                    cost_so_far[(next_x, next_y)] = new_cost
                    parent[(next_x, next_y)] = (x, y)
                    heapq.heappush(priority_queue, (new_cost, (next_x, next_y)))
    return None, float("inf"), nodes_expanded


# ---------- A* ----------
def a_star(grid, origin, destination):
    priority_queue = [(0, origin)]
    cost_so_far = {origin: 0}
    parent = {origin: None}
    visited = set()
    nodes_expanded = 0

    while priority_queue:
        f_score, (x, y) = heapq.heappop(priority_queue)
        nodes_expanded += 1
        if (x, y) == destination:
            path = reconstruct_path(parent, destination)
            return path, cost_so_far[(x, y)], nodes_expanded

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + dx, y + dy
            if grid.is_valid(next_x, next_y, time=0):
                new_cost = cost_so_far[(x, y)] + grid.get_cost(next_x, next_y)
                if (next_x, next_y) not in cost_so_far or new_cost < cost_so_far[(next_x, next_y)]:
                    cost_so_far[(next_x, next_y)] = new_cost
                    parent[(next_x, next_y)] = (x, y)
                    h = abs(destination[0] - next_x) + abs(destination[1] - next_y)
                    f_score = new_cost + h
                    heapq.heappush(priority_queue, (f_score, (next_x, next_y)))
    return None, float("inf"), nodes_expanded


# ---------- Local Search: Hill Climbing ----------
def hill_climbing(grid, origin, destination, max_restarts=5):
    best_path = None
    for _ in range(max_restarts):
        current = origin
        path = [current]
        visited = set([current])

        while current != destination:
            neighbors = [
                (current[0] + dx, current[1] + dy)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                if grid.is_valid(current[0] + dx, current[1] + dy)
            ]
            neighbors = [n for n in neighbors if n not in visited]
            if not neighbors:
                break

            current = min(
                neighbors, key=lambda x: abs(x[0] - destination[0]) + abs(x[1] - destination[1])
            )
            path.append(current)
            visited.add(current)

        if path[-1] == destination:
            if best_path is None or len(path) < len(best_path):
                best_path = path
    return best_path


# ---------- Local Search: Simulated Annealing ----------
def simulated_annealing(
    grid, origin, destination, max_iterations=200, temperature=98.0, cooling_rate=0.95
):
    current = origin
    path = [current]

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for _ in range(max_iterations):
        if current == destination:
            return path

        neighbors = [
            (current[0] + dx, current[1] + dy)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if grid.is_valid(current[0] + dx, current[1] + dy)
        ]

        if not neighbors:
            break

        next_node = random.choice(neighbors)
        delta_e = heuristic(current, destination) - heuristic(next_node, destination)

        if delta_e > 0 or math.exp(delta_e / temperature) > random.random():
            current = next_node
            path.append(current)

        temperature *= cooling_rate

    return path if path[-1] == destination else None


# ---------- Helper ----------
def reconstruct_path(parent, goal):
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

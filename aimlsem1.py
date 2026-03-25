import numpy as np
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(grid, start, end):
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = heuristic(start, end)
    start_node.f = start_node.h

    open_list = []
    heapq.heappush(open_list, start_node)

    closed_set = set()

    # Track best cost to each node
    g_score = {start: 0}

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position in closed_set:
            continue

        closed_set.add(current_node.position)

        # Goal reached
        if current_node.position == end:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # 4-direction movement
        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor_pos = (
                current_node.position[0] + move[0],
                current_node.position[1] + move[1]
            )

            # Check bounds
            if not (0 <= neighbor_pos[0] < grid.shape[0] and 0 <= neighbor_pos[1] < grid.shape[1]):
                continue

            # ❗ Treat urban (100) as obstacle (optional but realistic)
            if grid[neighbor_pos] == 100:
                continue

            tentative_g = current_node.g + grid[neighbor_pos]

            if neighbor_pos in g_score and tentative_g >= g_score[neighbor_pos]:
                continue

            neighbor_node = Node(current_node, neighbor_pos)
            neighbor_node.g = tentative_g
            neighbor_node.h = heuristic(neighbor_pos, end)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            g_score[neighbor_pos] = tentative_g
            heapq.heappush(open_list, neighbor_node)

    return None


if __name__ == '__main__':
    grid = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 10, 100, 100, 100, 100, 10, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 10, 100, 1, 1, 100, 10, 1, 1, 10, 10, 10, 1, 1],
        [1, 1, 10, 100, 1, 1, 100, 10, 1, 1, 10, 1, 1, 1, 1],
        [1, 1, 10, 1, 1, 1, 10, 10, 1, 1, 10, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ])

    start_point = (0, 0)
    end_point = (9, 14)

    path = a_star_search(grid, start_point, end_point)

    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.imshow(grid, cmap='terrain', interpolation='nearest')

    if path:
        path_rows = [p[0] for p in path]
        path_cols = [p[1] for p in path]
        ax.plot(path_cols, path_rows, color='red', linewidth=2, marker='o', markersize=4, label='Optimal Path')
        print("Path found!")
    else:
        print("No path found.")

    ax.plot(start_point[1], start_point[0], 'bo', markersize=8, label='Start (Habitat A)')
    ax.plot(end_point[1], end_point[0], 'go', markersize=8, label='End (Habitat B)')

    ax.set_title('A* Search for Wildlife Corridor Optimization')
    ax.set_xlabel('Grid Column')
    ax.set_ylabel('Grid Row')
    ax.legend()

    cbar = fig.colorbar(cax, ticks=[1, 10, 100])
    cbar.ax.set_yticklabels(['Forest (Cost 1)', 'Hills (Cost 10)', 'Urban (Blocked)'])

    plt.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
    plt.show()
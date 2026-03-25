🌿 A* Search for Wildlife Corridor Optimization

📌 Overview

This project implements the **A* (A-Star) Search Algorithm** to find an optimal path between two habitats while minimizing traversal cost across different types of terrain.

The goal is to simulate **wildlife corridor planning**, where animals prefer safer and less energy-consuming routes instead of simply the shortest path.



## 🧠 Concept

The A* algorithm finds the most efficient path using:

* **g(n):** Cost from start node to current node
* **h(n):** Heuristic (estimated cost to goal using Manhattan distance)
* **f(n) = g(n) + h(n):** Total cost function

The algorithm selects paths that minimize overall cost rather than just distance.


🌍 Terrain Representation

The environment is modeled as a 2D grid with different terrain types:

| Terrain Type | Cost | Description                   |
| ------------ | ---- | ----------------------------- |
| Forest       | 1    | Easy to traverse              |
| Hills        | 10   | Moderate difficulty           |
| Urban        | 100  | Blocked (treated as obstacle) |

Urban areas are considered **non-traversable**, simulating real-world avoidance by wildlife.



🚀 Features

* Implementation of **A* pathfinding algorithm**
* Weighted grid-based environment
* Obstacle handling (urban areas blocked)
* Visualization using **Matplotlib**
* Optimal path displayed with start and end points



🖥️ How to Run

### 1. Install dependencies


pip install numpy matplotlib


### 2. Run the program

python main.py


📊 Output

* A grid visualization of terrain
* Start point (Habitat A)
* End point (Habitat B)
* Optimal path highlighted in red



📸 Sample Output

<img width="1690" height="896" alt="image" src="https://github.com/user-attachments/assets/58f6a2f4-74fa-40c5-a2a0-9490655afb96" />


📚 Applications

* Wildlife conservation planning
* Route optimization problems
* Robotics pathfinding
* Game AI navigation



⚙️ Assumptions

* Movement is restricted to **4 directions** (up, down, left, right)
* Heuristic used: **Manhattan distance**
* Urban regions are treated as **blocked obstacles**


👨‍💻 Author

Name-Prafful Shikhar
Roll Number-25SCS1003004010
Section-1CSE27
Email-prafful.25scs1003004010@iilm.edu,praffulshikhar53@gmail.com

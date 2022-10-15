from queue import PriorityQueue, Queue

from PathPlanning.Object import GridMap, Point


def heuristic(goal, node):
    # Use Manhattan Distance as an estimate of priority
    return abs(goal.x - node.x) + abs(goal.y - node.y)

def type_check(graph, start, goal):
    # Used to check the correct type is passed in.
    if not isinstance(graph, GridMap):
        graph = GridMap(graph)

    if not isinstance(start, Point):
        start = Point(start[0], start[1])

    if not isinstance(goal, Point):
        goal = Point(goal[0], goal[1])

def breadth_first_search(graph, start, goal) -> dict:
    # Type checking.
    type_check(graph=graph, start=start, goal=goal)
    # Pathfinding queue.
    frontier = Queue()
    frontier.put(start)
    # Path A->B is stored as parents[B] == A.
    parents = dict()
    # Initialization.
    parents[start] = None

    while not frontier.empty():
        current = frontier.get()
        # Early stopping.
        if current == goal:
            break
        for node in graph.getNeighbor(current):
            # Check whether the node has a parent.
            if node not in parents:
                # Add secondary node to the search queue.
                frontier.put(node)
                # Record parent node.
                parents[node] = current
    return parents

def greedy_best_first_search(graph, start, goal) -> dict:
    # Type checking.
    type_check(graph=graph, start=start, goal=goal)
    # Pathfinding queue.
    frontier = PriorityQueue()
    frontier.put(start)
    # Path A->B is stored as parents[B] == A.
    parents = dict()
    # Initialization.
    start.priority = 0
    parents[start] = None

    while not frontier.empty():
        current = frontier.get()
        # Early stopping.
        if current == goal:
            break
        for node in graph.getNeighbor(current):
            # Check whether the node has a parent.
            if node not in parents:
                # Calculate estimated distance.
                node.priority = heuristic(goal, node)
                # Add secondary node to the search queue.
                frontier.put(node)
                # Record parent node.
                parents[node] = current
    return parents

def dijkstra_search(graph, start, goal) -> dict:
    # Type checking.
    type_check(graph=graph, start=start, goal=goal)
    # Using a priority queue instead of a regular queue.
    frontier = PriorityQueue()
    frontier.put(start)
    # Path A->B is stored as parents[B] == A.
    parents = dict()
    # Cost start->A is stored as costs[A].
    costs = dict()
    # Initialization.
    start.priority = 0
    parents[start] = None
    costs[start] = 0

    while not frontier.empty():
        current = frontier.get()
        # Early stopping.
        if current == goal:
            break
        for node in graph.getNeighbor(current):
            # Calculate the cost from initial node to neighbor point,
            # where walking through the current node.
            new_cost = costs[current] + graph.cost(current, node)
            # Check whether the node has a parent.
            # Determine whether it costs less to go via the current node.
            if (node not in costs) or new_cost < costs[node]:
                # Alter the cost of this point.
                costs[node] = new_cost
                # Changes the way the frontier expands.
                node.priority = new_cost
                # Add secondary node to the search queue.
                frontier.put(node)
                # Record parent node.
                parents[node] = current
    return parents

def a_star_search(graph, start, goal) -> dict:
    # Type checking.
    type_check(graph=graph, start=start, goal=goal)
    # Pathfinding queue.
    frontier = PriorityQueue()
    frontier.put(start)
    # Path A->B is stored as parents[B] = A.
    parents = dict()
    # Cost start->A is stored as costs[A].
    costs = dict()
    # Initialization.
    start.priority = 0
    parents[start] = None
    costs[start] = 0

    while not frontier.empty():
        current = frontier.get()
        # Early stopping.
        if current == goal:
            break
        for node in graph.getNeighbor(current):
            # Calculate the cost from initial node to neighbor point,
            # where walking through the current node.
            new_cost = costs[current] + graph.cost(current, node)
            # If this point not in the costs dict,
            # or arriving via the current node has less cost.
            if (node not in costs) or new_cost < costs[node]:
                # Alter the cost of this point.
                costs[node] = new_cost
                # Add estimated cost as priority.
                node.priority = new_cost + heuristic(goal, node)
                frontier.put(node)
                # Record parent node.
                parents[node] = current
    return parents

import numpy as np
from matplotlib import pyplot as plt

class Point:
    # coordinate point class in 2D map
    def __init__(self, x=0, y=0, priority=None):
        self.x = x
        self.y = y
        # use in overloading comparison operator '<'
        self.priority = priority

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __lt__(self, other):
        # set for PriorityQueue
        # Queue needs implementation of comparison operation
        return self.priority < other.priority
    
    def __eq__(self, other):
        # overload '=='
        # checking both objects of same class
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
    def __hash__(self):
        # make class 'Point' hashable
        return hash((self.x, self.y))

class GridMap:
    # 2D grid map
    def __init__(self, graph):
        # 2D list
        self.graph = graph
        self.height = len(graph)
        self.width = len(graph[0])

    def __repr__(self):
        return f"GridMap(%s)" \
                % '\n'.ljust(9).join([str(line) for line in self.graph])

    def __contains__(self, node):
        # overload component operator 'in'
        # determine point in the range of gird map
        return 0 <= node.x <= self.height-1 and \
               0 <= node.y <= self.width-1

    def isbarrier(self, node) -> int:
        # 0: legal path
        # 1: barrier
        return self.graph[node.x][node.y]

    def cost(self, current, node):
        # Manhattan Distance
        return abs(current.x - node.x) + abs(current.y - node.y)

    # Find the nodes that can be reached,
    # in the four directions of the current node: up, right, down, left.
    mvs = [Point(-1,0),Point(0,1),Point(1,0),Point(0,-1)]

    def getNeighbor(self, current):
        """
        Determine whether the next node is not out of bounds and is not barrier,
        finally, generate neighbor nodes list.
        Use Walrus operator ':=' to avoid bobule adding
        """
        return [node for mv in self.mvs if (node:=current+mv) in self 
                                        and not self.isbarrier(node)]
    
    def get_path(self, parents, start, goal):
        # Get breif path from parents dict.
        path = dict()
        current = goal
        while (node := parents.get(current)) != start:
            path[current] = node
            current = node
        else:
            # Create the start node.
            path[current] = node
        return path 

    def disp(self, res):
        # Displays parent-child nodes relationships.
        n = len(str(len(res)))
        step = 0
        for parent, node in \
        ((parent, node) for (parent, node) in res.items()):
            fmt = "{:>%rd}: {} <- {}" % n
            print(fmt.format(step, node, parent))
            step += 1

    def disp_map(self, parents, start, goal):
        # Displays 2D grid diagrams and planning path.
        plt.figure(figsize=(int(self.width/3), int(self.height/3)), dpi=100)
        ax = plt.gca()
        # Major ticks.
        ax.set_xticks(np.arange(0, self.width, 1))
        ax.set_yticks(np.arange(0, self.height, 1))
        # Labels for major ticks.
        ax.set_xticklabels(np.arange(0, self.width, 1))
        ax.set_yticklabels(np.arange(0, self.height, 1))
        # Minor ticks
        ax.set_xticks(np.arange(-.5, self.width, 1), minor=True)
        ax.set_yticks(np.arange(-.5, self.height, 1), minor=True)
        # Gridlines based on minor ticks.
        ax.grid(which="minor", color="gray", linestyle='-')
        # Special Point.
        # Attention:
        # x & y are inversed in matplotlib drawing coordinates. 
        ax.plot(start.y, start.x, "b*", markersize='11', alpha = 0.5)
        ax.plot(goal.y, goal.x, "rx", markersize='9', alpha = 0.8)
        # Labels.
        ax.set_xlabel(r"$\mathbf{y \rightarrow}$")
        ax.set_ylabel(r"$\mathbf{\leftarrow x}$")
        # Create base grid.
        ax.imshow(self.graph, cmap="Greys")
        # Alignment.
        path = self.get_path(parents=parents, start=start, goal=goal)
        for parent, node in \
        ((parent, node) for (parent, node) in path.items()):
            ax.plot([parent.y, node.y], [parent.x, node.x], linewidth=1.2, color='gray', linestyle='--')
        plt.show()
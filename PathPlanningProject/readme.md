# 路径规划 Path Planning

## 说明 Description

本项目基于 Python 🐍 复现寻路算法教程 [Introduction to the A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

## 库依赖 Requirements
```txt
numpy
matplotlib
queue
```

## 项目结构 Project Structure

主要包含两个 `.py` 文件：`Algorithm.py` & `Object.py`

### Object.py

实现了点类 `<class "Point">` 和平面网格地图类 `<class "GridMap">`

`Point(x=0, y=0, priority=None)`

创建时包含三个属性：索引值 x、索引值 y、和优先级 priority（用于优先队列 PriorityQueue）

`GridMap(graph)`

创建时需传入一张 2 维的列表，有 3 个需外部调用的方法：

1. `disp(res)`

    用于展示子父节点信息。

2. `get_path(parents, start, goal)`

    从存储子父节点信息的字典中获取算法规划的路径。

3. `disp_map(parents, start, goal)`

    绘制一张包含起点、终点、二维网格和路径的地图。

### Algorithm.py

实现了 4 种算法：
|name|`function`|
|:-:|:-:|
|广度优先搜索|`breadth_first_search`|
|Dijkstra 算法|`breadth_first_search`|
|贪婪最佳优先算法|`greedy_best_first_search`|
|A*搜索算法|`a_star_search`|

调用方法： 
`function(graph, start, goal) -> dict`

均返回一个记录子父节点信息的字典。


## 使用实例 Usage Example
导入模块
```python
from PathPlanning.Object import Point, GridMap
from PathPlanning import Algorithm
```

设置初始条件
```python
# record map info here.
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# Set the start-end coordinates.
start = Point(12, 0)
goal = Point(2, 14)
# Instantiate grid map.
graph = GridMap(grid)
```

算法求解
```python
# Select the path planning algorithm.
main = Algorithm.greedy_best_first_search
# Calculate.
parents = main(graph=graph, start=start, goal=goal)
# Show the result.
graph.disp(parents)
graph.disp_map(parents=parents, start=start, goal=goal)
```
输出结果
```
  0: None <- Point(12, 0)
  1: Point(12, 0) <- Point(11, 0)
  2: Point(12, 0) <- Point(12, 1)
  ...
114: Point(1, 14) <- Point(0, 14)
115: Point(1, 14) <- Point(2, 14)
```

![Output]()

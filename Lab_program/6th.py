graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}
h = {
    'A': 6, 'B': 5, 'C': 4,
    'D': 3, 'E': 2, 'F': 2, 'G': 0
}
def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()
    while open_list:
        open_list.sort()
        f, cost, node, path = open_list.pop(0)
        if node == goal:
            print("Optimal Path:", path)
            print("Total Cost:", cost)
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_cost = cost + weight
                    new_f = new_cost + h[neighbor]
                    open_list.append(
                        (new_f, new_cost, neighbor, path + [neighbor])
                    )
astar('A', 'G')

#output
Optimal Path: ['A', 'B', 'D', 'G']
Total Cost: 6

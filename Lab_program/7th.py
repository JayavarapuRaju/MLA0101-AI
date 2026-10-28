def minimax(depth, node, maximizing):
    if depth == 2:
        return node
    if maximizing:
        return max(
            minimax(depth + 1, child, False)
            for child in tree[node]
        )
    else:
        return min(
            minimax(depth + 1, child, True)
            for child in tree[node]
        )
tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [2, 9]
}
result = minimax(0, 'A', True)
print("Best Value:", result)
#output
Best Value: 3

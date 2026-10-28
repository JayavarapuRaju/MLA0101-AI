def alphabeta(depth, node, alpha, beta, maximizing):
    if depth == 2:
        return node
    if maximizing:
        best = -999
        for child in tree[node]:
            value = alphabeta(
                depth + 1, child, alpha, beta, False
            )
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for child in tree[node]:
            value = alphabeta(
                depth + 1, child, alpha, beta, True
            )
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [2, 9]
}
result = alphabeta(0, 'A', -999, 999, True)
print("Best Value:", result)
#output
Best Value: 3

Best Value: 3

from collections import deque

def water_jug():
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(a, b)

        if a == 2:
            print("Goal Reached!")
            return

        states = [
            (4, b),
            (a, 3),
            (0, b),
            (a, 0),
            (a - min(a, 3-b), b + min(a, 3-b)),
            (a + min(b, 4-a), b - min(b, 4-a))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)
water_jug()
#output
0 0
4 0
0 3
4 3
1 3
3 0
1 0
3 3
0 1
4 2
4 1
0 2
2 3
Goal Reached!

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    hanoi(n-1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    hanoi(n-1, auxiliary, source, destination)
n = 3
hanoi(n, 'A', 'B', 'C')
#output
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C


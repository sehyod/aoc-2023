import os

pipes: dict[str, list[tuple[int, int]]] = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)]
}


def part1():
    grid: list[str] = []
    start: tuple[int, int] = (0, 0)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for i, r in enumerate(f):
            grid.append(r.strip())
            if 'S' in r:
                start = (i, r.index('S'))

    neighbour: tuple[int, int] = (0, 0)
    dir: tuple[int, int] = (0, 0)
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (pipe := grid[start[0] + d[0]][start[1] + d[1]]) != '.' and (-d[0], -d[1]) in pipes[pipe]:
            dir = d
            neighbour = (start[0] + d[0], start[1] + d[1])

    steps = 1
    pos = neighbour

    while (pipe := grid[pos[0]][pos[1]]) != 'S':
        dir = [d for d in pipes[pipe] if d[0] != -dir[0] or d[1] != -dir[1]][0]
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        steps += 1

    return steps // 2


def part2():
    grid: list[str] = []
    start: tuple[int, int] = (0, 0)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for i, r in enumerate(f):
            grid.append(r.strip())
            if 'S' in r:
                start = (i, r.index('S'))

    neighbour: tuple[int, int] = (0, 0)
    dir: tuple[int, int] = (0, 0)
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (pipe := grid[start[0] + d[0]][start[1] + d[1]]) != '.' and (-d[0], -d[1]) in pipes[pipe]:
            dir = d
            neighbour = (start[0] + d[0], start[1] + d[1])

    edge: list[tuple[int, int]] = [start]
    pos = neighbour

    while (pipe := grid[pos[0]][pos[1]]) != 'S':
        edge.append(pos)
        dir = [d for d in pipes[pipe] if d[0] != -dir[0] or d[1] != -dir[1]][0]
        pos = (pos[0] + dir[0], pos[1] + dir[1])

    # Shoelace formula
    area = sum([(edge[i][0]*edge[(i + 1) % len(edge)][1])-(edge[(i + 1) %
               len(edge)][0]*edge[i][1]) for i in range(len(edge))])//2

    # Pick's theorem
    return area - len(edge)//2 + 1


if __name__ == '__main__':
    print(part1())
    print(part2())

import os
from math import inf


def part1():
    grid: list[list[int]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            row: list[int] = []
            for c in r.strip():
                row.append(int(c))
            grid.append(row)

    dist: dict[tuple[tuple[int, int], bool], int | float] = {}
    prev: dict[tuple[tuple[int, int], bool],
               tuple[tuple[int, int], bool] | None] = {}

    queue: list[tuple[tuple[int, int], bool]] = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dist[((i, j), False)] = inf
            dist[((i, j), True)] = inf
            prev[((i, j), False)] = None
            prev[((i, j), True)] = None
            queue += [((i, j), False), ((i, j), True)]
    dist[((0, 0), False)] = 0
    dist[((0, 0), True)] = 0

    def neighbours(u: tuple[tuple[int, int], bool]) -> list[tuple[tuple[int, int], bool]]:
        list_neighbours: list[tuple[tuple[int, int], bool]] = []
        ((i, j), vertical) = u

        for k in range(1, 4):
            if not vertical:
                list_neighbours.append(((i + k, j), True))
                list_neighbours.append(((i - k, j), True))
            else:
                list_neighbours.append(((i, j + k), False))
                list_neighbours.append(((i, j - k), False))

        return [n for n in list_neighbours if 0 <= n[0][0] < len(grid) and 0 <= n[0][1] < len(grid[0])]

    while len(queue):
        u = queue.pop(min([(i, dist[u])
                      for i, u in enumerate(queue)], key=lambda x: x[1])[0])
        if u[0] == (len(grid) - 1, len(grid[0]) - 1):
            return dist[u]
        for n in neighbours(u):
            if n in queue:
                new_weight = dist[u]
                c = u[0]
                fact = -1 if n[0][0] < u[0][0] or n[0][1] < u[0][1] else 1
                while c != n[0]:
                    c = (c[0] + n[1]*fact, c[1] + (1 - n[1])*fact)
                    new_weight += grid[c[0]][c[1]]
                if new_weight < dist[n]:
                    dist[n] = new_weight
                    prev[n] = u


def part2():
    grid: list[list[int]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            row: list[int] = []
            for c in r.strip():
                row.append(int(c))
            grid.append(row)

    dist: dict[tuple[tuple[int, int], bool], int | float] = {}
    prev: dict[tuple[tuple[int, int], bool],
               tuple[tuple[int, int], bool] | None] = {}

    queue: list[tuple[tuple[int, int], bool]] = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dist[((i, j), False)] = inf
            dist[((i, j), True)] = inf
            prev[((i, j), False)] = None
            prev[((i, j), True)] = None
            queue += [((i, j), False), ((i, j), True)]
    dist[((0, 0), False)] = 0
    dist[((0, 0), True)] = 0

    def neighbours(u: tuple[tuple[int, int], bool]) -> list[tuple[tuple[int, int], bool]]:
        list_neighbours: list[tuple[tuple[int, int], bool]] = []
        ((i, j), vertical) = u

        for k in range(4, 11):
            if not vertical:
                list_neighbours.append(((i + k, j), True))
                list_neighbours.append(((i - k, j), True))
            else:
                list_neighbours.append(((i, j + k), False))
                list_neighbours.append(((i, j - k), False))

        return [n for n in list_neighbours if 0 <= n[0][0] < len(grid) and 0 <= n[0][1] < len(grid[0])]

    while len(queue):
        u = queue.pop(min([(i, dist[u])
                      for i, u in enumerate(queue)], key=lambda x: x[1])[0])
        if u[0] == (len(grid) - 1, len(grid[0]) - 1):
            return dist[u]
        for n in neighbours(u):
            if n in queue:
                new_weight = dist[u]
                c = u[0]
                fact = -1 if n[0][0] < u[0][0] or n[0][1] < u[0][1] else 1
                while c != n[0]:
                    c = (c[0] + n[1]*fact, c[1] + (1 - n[1])*fact)
                    new_weight += grid[c[0]][c[1]]
                if new_weight < dist[n]:
                    dist[n] = new_weight
                    prev[n] = u


if __name__ == '__main__':
    print(part1())
    print(part2())

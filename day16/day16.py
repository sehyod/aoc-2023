import os


def part1():
    grid: list[str] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            grid.append(r.strip())

    memo: dict[tuple[int, int, tuple[int, int]],
               list[tuple[int, int, tuple[int, int]]]] = {}

    def next(i: int, j: int, dir: tuple[int, int]) -> list[tuple[int, int, tuple[int, int]]]:
        if (i, j, dir) in memo:
            return memo[i, j, dir]
        match grid[i][j]:
            case '.':
                memo[i, j, dir] = [(i + dir[0], j + dir[1], dir)]
            case '\\':
                memo[i, j, dir] = [(i + dir[1], j + dir[0], (dir[1], dir[0]))]
            case '/':
                memo[i, j, dir] = [
                    (i - dir[1], j - dir[0], (-dir[1], -dir[0]))]
            case '|':
                if dir[1] == 0:
                    memo[i, j, dir] = [(i + dir[0], j + dir[1], dir)]
                else:
                    memo[i, j, dir] = [(i - 1, j, (-1, 0)), (i + 1, j, (1, 0))]
            case '-':
                if dir[0] == 0:
                    memo[i, j, dir] = [(i + dir[0], j + dir[1], dir)]
                else:
                    memo[i, j, dir] = [(i, j - 1, (0, -1)), (i, j + 1, (0, 1))]

        return memo[i, j, dir]

    queue: list[tuple[int, int, tuple[int, int]]] = [(0, 0, (0, 1))]
    visited: dict[tuple[int, int], list[tuple[int, int]]] = {}

    while len(queue) > 0:
        (i, j, dir) = queue.pop(0)

        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if (i, j) not in visited or dir not in visited[i, j]:
                visited[i, j] = (visited[i, j] + [dir]) if (i,
                                                            j) in visited else [dir]
                queue += next(i, j, dir)

    return len(visited.keys())


def part2():
    grid: list[str] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            grid.append(r.strip())

    memo: dict[tuple[int, int, tuple[int, int]],
               list[tuple[int, int, tuple[int, int]]]] = {}

    def next(i: int, j: int, dir: tuple[int, int]) -> list[tuple[int, int, tuple[int, int]]]:
        if (i, j, dir) in memo:
            return memo[i, j, dir]
        match grid[i][j]:
            case '.':
                memo[i, j, dir] = [(i + dir[0], j + dir[1], dir)]
            case '\\':
                memo[i, j, dir] = [(i + dir[1], j + dir[0], (dir[1], dir[0]))]
            case '/':
                memo[i, j, dir] = [
                    (i - dir[1], j - dir[0], (-dir[1], -dir[0]))]
            case '|':
                if dir[1] == 0:
                    memo[i, j, dir] = [(i + dir[0], j + dir[1], dir)]
                else:
                    memo[i, j, dir] = [(i - 1, j, (-1, 0)), (i + 1, j, (1, 0))]
            case '-':
                if dir[0] == 0:
                    memo[i, j, dir] = [(i + dir[0], j + dir[1], dir)]
                else:
                    memo[i, j, dir] = [(i, j - 1, (0, -1)), (i, j + 1, (0, 1))]

        return memo[i, j, dir]

    def count(initial_state: tuple[int, int, tuple[int, int]]) -> int:
        queue = [initial_state]
        visited: dict[tuple[int, int], list[tuple[int, int]]] = {}

        while len(queue) > 0:
            (i, j, dir) = queue.pop(0)

            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if (i, j) not in visited or dir not in visited[i, j]:
                    visited[i, j] = (visited[i, j] + [dir]) if (i,
                                                                j) in visited else [dir]
                    queue += next(i, j, dir)

        return len(visited.keys())

    return max([count(state) for state in [(0, j, (1, 0)) for j in range(len(grid[0]))]+[(len(grid) - 1, j, (-1, 0)) for j in range(len(grid[0]))]+[(i, 0, (0, 1)) for i in range(len(grid))]+[(i, len(grid[0]) - 1, (0, -1)) for i in range(len(grid))]])


if __name__ == '__main__':
    print(part1())
    print(part2())

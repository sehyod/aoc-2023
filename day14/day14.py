import os


def part1():
    platform: list[list[str]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            platform.append([*r.strip()])

    weight = 0

    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == 'O':
                pos = i
                while pos > 0 and platform[pos - 1][j] == '.':
                    platform[pos][j] = '.'
                    platform[pos - 1][j] = 'O'
                    pos -= 1
                weight += len(platform) - pos

    return weight


def move(platform: list[list[str]], rocks: list[tuple[int, int]], delta: tuple[int, int]):
    updated_rocks: list[tuple[int, int]] = []

    for rock in rocks:
        i, j = rock
        while 0 <= i + delta[0] < len(platform) and 0 <= j + delta[1] < len(platform[0]) and platform[i + delta[0]][j + delta[1]] == '.':
            platform[i][j] = '.'
            i += delta[0]
            j += delta[1]
            platform[i][j] = 'O'
        updated_rocks.append((i, j))

    return updated_rocks


def cycle(platform: list[list[str]], rocks: list[tuple[int, int]]):
    updated_rocks = move(platform, sorted(
        rocks, key=lambda r: r), (-1, 0))  # North
    updated_rocks = move(platform, sorted(
        updated_rocks, key=lambda r: (r[1], r[0])), (0, -1))  # West
    updated_rocks = move(platform, sorted(
        updated_rocks, key=lambda r: r, reverse=True), (1, 0))  # South
    updated_rocks = move(platform, sorted(
        updated_rocks, key=lambda r: (r[1], r[0]), reverse=True), (0, 1))  # East

    return updated_rocks


def part2():
    platform: list[list[str]] = []
    rocks: list[tuple[int, int]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for i, r in enumerate(f):
            platform.append([*r.strip()])
            if 'O' in r:
                for j, c in enumerate(r):
                    if c == 'O':
                        rocks.append((i, j))

    # Store, for each rocks cofiguration, the step index at which it occured and the corresponding weight
    memo: dict[str, tuple[int, int]] = {}
    for i in range(1000000000):
        rocks = sorted(cycle(platform, rocks))
        if str(rocks) not in memo:
            memo[str(rocks)] = (i, sum(len(platform) - rock[0]
                                       for rock in rocks))
        else:
            step = memo[str(rocks)][0] + (1000000000 -
                                          i) % (i - memo[str(rocks)][0]) - 1
            return [item[1][1] for item in memo.items() if item[1][0] == step][0]


if __name__ == '__main__':
    print(part1())
    print(part2())

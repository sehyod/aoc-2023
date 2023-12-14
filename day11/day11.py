import os


def part1():
    universe: list[str] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            universe.append(r.strip())

    temp_universe: list[str] = []
    for r in universe:
        if '#' not in r:
            temp_universe.append(r)
        temp_universe.append(r)

    universe = ['']*len(temp_universe)
    for j in range(len(temp_universe[0])):
        if all(r[j] == '.' for r in temp_universe):
            for i in range(len(universe)):
                universe[i] += '.'
        for i in range(len(universe)):
            universe[i] += temp_universe[i][j]

    galaxies: list[tuple[int, int]] = []
    for i, r in enumerate(universe):
        for j, c in enumerate(r):
            if c == '#':
                galaxies.append((i, j))

    dist = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            dist += abs(galaxies[j][1] - galaxies[i][1]) + \
                abs(galaxies[j][0] - galaxies[i][0])

    return dist


def part2():
    SIZE = 1000000
    universe: list[str] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            universe.append(r.strip())

    empty_rows = []
    empty_columns = []
    for i, r in enumerate(universe):
        if '#' not in r:
            empty_rows.append(i)

    for j in range(len(universe[0])):
        if all(r[j] == '.' for r in universe):
            empty_columns.append(j)

    galaxies: list[tuple[int, int]] = []
    for i, r in enumerate(universe):
        for j, c in enumerate(r):
            if c == '#':
                galaxies.append((i, j))

    dist = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            dist += abs(galaxies[j][1] - galaxies[i][1]) + \
                abs(galaxies[j][0] - galaxies[i][0]) + (SIZE - 1)*len([row for row in empty_rows if min(galaxies[i][0], galaxies[j][0])
                                                                       < row < max(galaxies[i][0], galaxies[j][0])]) + (SIZE - 1)*len([col for col in empty_columns if min(galaxies[i][1], galaxies[j][1]) < col < max(galaxies[i][1], galaxies[j][1])])

    return dist


if __name__ == '__main__':
    print(part1())
    print(part2())

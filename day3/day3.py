import os


def get_neighbours(i, j1, j2, engine_height, engine_width):
    """Returns the neighbour positions of the number contained between (i, j1) and (i, j2)"""

    # All neighbour coordinates, including the ones outside of the engine
    coordinates = [(k, l) for k in range(i - 1, i + 2)
                   for l in range(j1 - 1, j2 + 2) if k != i or l == j1 - 1 or l == j2 + 1]

    return [(k, l) for (k, l) in coordinates if 0 <= k < engine_height and 0 <= l < engine_width]


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    engine: list[str] = []
    s = 0

    with open(filename) as f:
        for r in f:
            engine.append(r.strip())

    for i, row in enumerate(engine):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                j2 = j + 1
                while j2 < len(row) and row[j2].isdigit():
                    j2 += 1
                neighbours = get_neighbours(
                    i, j, j2 - 1, len(engine), len(row))

                if any([not engine[n[0]][n[1]].isdigit() and engine[n[0]][n[1]] != '.' for n in neighbours]):
                    s += int(row[j:j2])
                j = j2
            j += 1

    return s


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    engine: list[str] = []
    gears = {}

    with open(filename) as f:
        for r in f:
            engine.append(r.strip())

    for i, row in enumerate(engine):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                j2 = j + 1
                while j2 < len(row) and row[j2].isdigit():
                    j2 += 1
                neighbours = get_neighbours(
                    i, j, j2 - 1, len(engine), len(row))

                for n in [n for n in neighbours if engine[n[0]][n[1]] == '*']:
                    if n not in gears:
                        gears[n] = []
                    gears[n].append(int(row[j: j2]))

                j = j2
            j += 1

    return sum([part_numbers[0]*part_numbers[1] for part_numbers in gears.values() if len(part_numbers) == 2])


if __name__ == '__main__':
    print(part1())
    print(part2())

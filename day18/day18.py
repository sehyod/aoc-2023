import os


def part1():
    instructions: list[str] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            instructions.append(r.strip())

    pos = (0, 0)
    tot = 0
    vertices: list[tuple[int, int]] = [pos]

    for instruction in instructions:
        dir, number, *_ = instruction.split()
        number = int(number)
        tot += number

        dir = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }[dir]

        pos = (pos[0] + number*dir[0], pos[1] + number*dir[1])
        vertices.append(pos)

    vertices.pop()
    # Shoelace formula
    return (tot-sum([(vertices[i][0]*vertices[(i + 1) % len(vertices)][1])-(vertices[(i + 1) %
                                                                                     len(vertices)][0]*vertices[i][1]) for i in range(len(vertices))]))//2 + 1


def part2():
    instructions: list[str] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            instructions.append(r.strip())

    pos = (0, 0)
    tot = 0
    vertices: list[tuple[int, int]] = [pos]

    for instruction in instructions:
        _, _, hexa = instruction.split()
        hexa = hexa[2:-1]
        dir = 'RDLU'[int(hexa[-1])]
        number = int(hexa[:-1], 16)
        tot += number

        dir = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }[dir]

        pos = (pos[0] + number*dir[0], pos[1] + number*dir[1])
        vertices.append(pos)

    vertices.pop()
    # Shoelace formula
    return (tot-sum([(vertices[i][0]*vertices[(i + 1) % len(vertices)][1])-(vertices[(i + 1) %
                                                                                     len(vertices)][0]*vertices[i][1]) for i in range(len(vertices))]))//2 + 1


if __name__ == '__main__':
    print(part1())
    print(part2())

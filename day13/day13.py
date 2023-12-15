import os


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    shapes: list[list[str]] = []
    with open(filename) as f:
        current_shape: list[str] = []
        for r in f:
            r = r.strip()
            if len(r) == 0:
                shapes.append(current_shape)
                current_shape = []
            else:
                current_shape.append(r.strip())
        shapes.append(current_shape)

    tot = 0
    for shape in shapes:
        height = len(shape)
        for i in range(1, height):
            length = min(i, height - i)
            if shape[i - length:i] == shape[i + length - 1:i - 1:-1]:
                tot += 100*i
                break
        width = len(shape[0])
        for j in range(1, width):
            length = min(j, width - j)
            if all(shape[i][j - length:j] == shape[i][j + length - 1:j - 1:-1] for i in range(height)):
                tot += j
                break

    return tot


def compare(u1: list[str], u2: list[str]):
    errors = 0
    for s1, s2 in zip(u1, u2):
        for (c1, c2) in zip(s1, s2):
            if c1 != c2:
                errors += 1
                if errors == 2:
                    return False

    return errors == 1


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    shapes: list[list[str]] = []
    with open(filename) as f:
        current_shape: list[str] = []
        for r in f:
            r = r.strip()
            if len(r) == 0:
                shapes.append(current_shape)
                current_shape = []
            else:
                current_shape.append(r.strip())
        shapes.append(current_shape)

    tot = 0
    for shape in shapes:
        height = len(shape)
        for i in range(1, height):
            length = min(i, height - i)
            if compare(shape[i - length:i], shape[i + length - 1:i - 1:-1]):
                tot += 100*i
                break
        width = len(shape[0])
        for j in range(1, width):
            length = min(j, width - j)
            if compare([shape[i][j - length:j] for i in range(height)], [shape[i][j + length - 1:j - 1:-1] for i in range(height)]):
                tot += j
                break

    return tot


if __name__ == '__main__':
    print(part1())
    print(part2())

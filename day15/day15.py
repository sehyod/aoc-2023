import os
import re


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    steps: list[str] = []

    with open(filename) as f:
        for r in f:
            steps = r.strip().split(',')

    tot = 0

    for step in steps:
        hash = 0
        for c in step:
            hash += ord(c)
            hash *= 17
            hash %= 256
        tot += hash

    return tot


def hash(label: str):
    hash = 0

    for c in label:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    steps: list[tuple[str, int | None]] = []
    boxes: list[dict[str, int]] = [{} for _ in range(256)]

    with open(filename) as f:
        for r in f:
            for step in r.strip().split(','):
                if '=' in step:
                    focal = int(re.findall(r'\d+', step)[0])
                    steps.append((re.findall(r'[a-z]+', step)[0], focal))
                else:
                    steps.append((re.findall(r'[a-z]+', step)[0], None))

    for (label, op) in steps:
        h = hash(label)
        if op is not None:
            boxes[h][label] = op
        else:
            boxes[h] = {k: v for k, v in boxes[h].items() if k != label}

    power = 0

    for box in range(256):
        for slot, focal_length in enumerate(boxes[box].values()):
            power += (1 + box)*(1 + slot)*focal_length

    return power


if __name__ == '__main__':
    print(part1())
    print(part2())

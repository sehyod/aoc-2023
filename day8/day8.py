import os
import re
from math import lcm


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    d = {}
    steps = 0
    instructions = None
    pos = 'AAA'
    last = 'ZZZ'

    with open(filename) as f:
        instructions, _, *rest = f
        instructions = instructions.strip()
        for r in rest:
            source, left, right = re.findall(r'[A-Z]{3}', r)
            d[source] = [left, right]

    while pos != last:
        pos = d[pos][0 if instructions[steps %
                                       len(instructions)] == 'L' else 1]
        steps += 1
    return steps


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    d = {}
    instructions = None
    pos: list[str] = []

    with open(filename) as f:
        instructions, _, *rest = f
        instructions = instructions.strip()
        for r in rest:
            source, left, right = re.findall(r'[A-Z]{3}', r)
            d[source] = [left, right]
            if source.endswith('A'):
                pos.append(source)

    res: list[int] = []
    for p in pos:
        steps = 0

        while not p.endswith('Z'):
            p = d[p][0 if instructions[steps %
                                       len(instructions)] == 'L' else 1]
            steps += 1

        res.append(steps)

    return lcm(*res)


if __name__ == '__main__':
    print(part1())
    print(part2())

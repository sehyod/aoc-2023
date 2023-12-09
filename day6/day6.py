import os
import re
from math import sqrt, floor, ceil


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    times = []
    distances = []

    with open(filename) as f:
        for i, r in enumerate(f):
            if i == 0:
                times = map(int, re.findall(r'\d+', r))
            else:
                distances = map(int, re.findall(r'\d+', r))

    p = 1
    for i, (t, d) in enumerate(zip(times, distances)):
        delta = t**2 - 4*d
        r1 = (t - sqrt(delta))/2
        r2 = (t + sqrt(delta))/2

        ceiled_r1 = ceil(r1)
        floored_r2 = floor(r2)

        tot = floored_r2 - ceiled_r1 + 1

        if ceiled_r1 == r1:
            tot -= 1
        if floored_r2 == r2:
            tot -= 1

        p *= tot

    return p


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    time = 0
    distance = 0

    with open(filename) as f:
        for i, r in enumerate(f):
            if i == 0:
                time = int(''.join(re.findall(r'\d+', r)))
            else:
                distance = int(''.join(re.findall(r'\d+', r)))

    delta = time**2 - 4*distance
    r1 = (time - sqrt(delta))/2
    r2 = (time + sqrt(delta))/2

    ceiled_r1 = ceil(r1)
    floored_r2 = floor(r2)

    tot = floored_r2 - ceiled_r1 + 1

    if ceiled_r1 == r1:
        tot -= 1
    if floored_r2 == r2:
        tot -= 1

    return tot


if __name__ == '__main__':
    print(part1())
    print(part2())

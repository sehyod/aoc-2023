import os
import re


memo: dict[tuple[str, str, int], int] = {}


def arrangements(springs: str, count: list[int], current=0) -> int:
    if (springs, str(count), current) in memo:
        return memo[springs, str(count), current]

    if len(springs) == 0:
        if (len(count) == 0 and current == 0) or (len(count) == 1 and count[0] == current):
            memo[springs, str(count), current] = 1
            return 1
        else:
            memo[springs, str(count), current] = 0
            return 0

    res = 0
    possibilities = ['#', '.'] if springs[0] == '?' else [springs[0]]

    for p in possibilities:
        if p == '.':
            if len(count) > 0 and current == count[0]:
                res += arrangements(springs[1:], count[1:], 0)
            elif current == 0:
                res += arrangements(springs[1:], count, current)
        elif p == '#' and len(count) > 0 and current < count[0]:
            res += arrangements(springs[1:], count, current + 1)

    memo[springs, str(count), current] = res
    return res


def part1():
    data: list[tuple[str, list[int]]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            springs, count = r.strip().split()
            data.append((springs, list(map(int, count.split(',')))))

    return sum(arrangements(springs, count) for springs, count in data)


def part2():
    data: list[tuple[str, list[int]]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            springs, count = r.strip().split()
            data.append((springs, list(map(int, count.split(',')))))

    return sum([arrangements('?'.join([springs]*5), count*5) for springs, count in data])


if __name__ == '__main__':
    print(part1())
    print(part2())

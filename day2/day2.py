import os
from functools import reduce


def parse_subset(subset: str):
    res: dict[str, int] = {}

    for cubes in subset.split(', '):
        [amount, color] = cubes.split(' ')
        res[color] = int(amount)

    return res


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    ids_sum = 0
    limits = {'red': 12, 'green': 13, 'blue': 14}

    with open(filename) as f:
        for r in f:
            [game_id, subsets] = r.strip().split(': ')
            game_id = int(game_id.split(' ')[1])
            subsets = [parse_subset(subset) for subset in subsets.split('; ')]
            if all([all([amount <= limits[color] for (color, amount) in subset.items()]) for subset in subsets]):
                ids_sum += game_id

    return ids_sum


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    total_power = 0
    COLORS = ['red', 'green', 'blue']

    with open(filename) as f:
        for r in f:
            [game_id, subsets] = r.strip().split(': ')
            game_id = int(game_id.split(' ')[1])
            subsets = [parse_subset(subset) for subset in subsets.split('; ')]

            cubes = {color: max(
                [subset[color] if color in subset else 0 for subset in subsets]) for color in COLORS}
            power = reduce(lambda a, b: a*b, cubes.values())
            total_power += power

    return total_power


if __name__ == '__main__':
    print(part1())
    print(part2())

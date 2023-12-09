import os
import re


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    seeds: list[int] = []
    mappings: list[list[list[int]]] = []

    with open(filename) as f:
        current_mapping = []
        for r in f:
            if r.startswith('seeds: '):
                seeds = list(map(int, re.findall(r'\d+', r)))
            elif len(r.strip()) == 0:
                continue
            elif ':' in r:
                mappings.append(current_mapping)
                current_mapping = []
            else:
                current_mapping.append(list(map(int, re.findall(r'\d+', r))))
        mappings.append(current_mapping)

    def compute_location(seed):
        current_value = seed
        for mapping in mappings:
            for [dest, source, range] in mapping:
                if source <= current_value < source + range:
                    current_value = dest + current_value - source
                    break
        return current_value

    return min(map(compute_location, seeds))


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    seeds: list[tuple[int, int]] = []
    mappings: list[list[list[int]]] = []

    with open(filename) as f:
        current_mapping = []
        for r in f:
            if r.startswith('seeds: '):
                seed_ranges = list(map(int, re.findall(r'\d+', r)))
                for start, length in zip(seed_ranges[::2], seed_ranges[1::2]):
                    seeds.append((start, start + length - 1))
            elif len(r.strip()) == 0:
                continue
            elif ':' in r:
                mappings.append(current_mapping)
                current_mapping = []
            else:
                current_mapping.append(list(map(int, re.findall(r'\d+', r))))
        mappings.append(current_mapping)

    state = [*seeds]
    for mapping in mappings:
        new_state = []
        while len(state):
            current_value = state.pop()
            found = False
            for [dest, source, range] in mapping:
                if source <= current_value[0] < source + range:
                    if source <= current_value[1] < source + range:
                        new_state.append(
                            (dest + current_value[0] - source, dest + current_value[1] - source))
                    else:
                        new_state.append(
                            (dest + current_value[0] - source, dest + range))
                        state.append((source + range, current_value[1]))
                    found = True
                    break
                elif source <= current_value[1] < source + range:
                    new_state.append((dest, dest + current_value[1] - source))
                    state.append((current_value[0], source - 1))
                    found = True
                    break
            if not found:
                new_state.append(current_value)

        state = [*new_state]

    return min([a for (a, _) in state])


if __name__ == '__main__':
    print(part1())
    print(part2())

import os
import graphviz
from math import lcm


def part1():
    start: list[str] = []
    modules: dict[str, tuple[list[str], dict[str, int] | int]] = {}

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            name, dest = r.strip().split(' -> ')
            dest = dest.split(', ')
            if name == 'broadcaster':
                start = dest
            elif name.startswith('%'):
                modules[name[1:]] = (dest, 0)
            elif name.startswith('&'):
                modules[name[1:]] = (dest, {})
    # Set initial values for Conjunctions
    for module in modules:
        for dest in modules[module][0]:
            if dest in modules:
                maybe_dict = modules[dest][1]
                if isinstance(maybe_dict, dict):
                    maybe_dict[module] = 0

    low_pulses = 0
    high_pulses = 0
    for _ in range(1000):
        low_pulses += 1
        queue: list[tuple[str, int, str]] = [
            (module, 0, '') for module in start]
        while len(queue) > 0:
            module, signal, origin = queue.pop(0)

            if signal == 1:
                high_pulses += 1
            else:
                low_pulses += 1

            if module not in modules:
                continue

            (dest, state) = modules[module]
            if isinstance(state, dict):  # Conjunction
                state[origin] = signal
                if all(s == 1 for s in state.values()):
                    for d in dest:
                        queue.append((d, 0, module))
                else:
                    for d in dest:
                        queue.append((d, 1, module))
            else:  # Flip-flop
                if signal == 0:
                    updated_state = 1 - state
                    modules[module] = (dest, updated_state)
                    for d in dest:
                        queue.append((d, updated_state, module))
    return low_pulses * high_pulses


def part2():
    graph = graphviz.Digraph()
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            name, dest = r.strip().split(' -> ')
            dest = dest.split(', ')
            if name == 'broadcaster':
                graph.node('broadcaster', 'broadcaster')
                for d in dest:
                    graph.edge(name, d)
            else:
                graph.node(name[1:], name)
                for d in dest:
                    graph.edge(name[1:], d)

    graph.render(os.path.join(dirname, 'graph.gv'))

    # Deduced from the graph
    return lcm(4003, 4027, 3919, 3917)


if __name__ == '__main__':
    print(part1())
    print(part2())

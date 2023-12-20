import os


def part1():
    workflow: dict[str, str] = {}
    parts: list[dict[str, int]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    is_workflow = True
    with open(filename) as f:
        for r in f:
            if len(r.strip()) == 0:
                is_workflow = False
            elif is_workflow:
                name = r[:r.index('{')]
                instructions = r.strip()[len(name) + 1:-1]
                workflow[name] = instructions
            else:
                part = {}
                for p in r.strip()[1:-1].split(','):
                    name, quantity = p.split('=')
                    part[name] = int(quantity)
                parts.append(part)

    def go_through(part: dict[str, int]):
        step = 'in'
        while True:
            if step == 'A':
                return True
            elif step == 'R':
                return False
            instructions = workflow[step]
            for inst in instructions.split(','):
                if ':' not in inst:
                    step = inst
                    break
                if eval(f'{part[inst[0]]}{inst[1]}{inst[2:inst.index(":")]}'):
                    step = inst[inst.index(':') + 1:]
                    break

    return sum(sum(part.values()) for part in parts if go_through(part))


def part2():
    workflow: dict[str, str] = {}

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    is_workflow = True
    with open(filename) as f:
        for r in f:
            if len(r.strip()) == 0:
                is_workflow = False
            elif is_workflow:
                name = r[:r.index('{')]
                instructions = r.strip()[len(name) + 1:-1]
                workflow[name] = instructions
            else:
                break

    queue: list[tuple[dict[str, tuple[int, int]], str]] = [
        ({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, 'in')]

    res: list[dict[str, tuple[int, int]]] = []
    while len(queue) > 0:
        state, step = queue.pop(0)
        if step == 'A':
            res.append(state)
            continue
        elif step == 'R':
            continue
        instructions = workflow[step]
        current_state = {**state}
        for inst in instructions.split(','):
            if ':' not in inst:
                queue.append((current_state, inst))
                break
            cond, dest = inst.split(':')
            category, op, *number = cond
            number = int(''.join(number))
            if op == '<':
                if current_state[category][0] < number:
                    queue.append(
                        ({**current_state, category: (current_state[category][0], min(current_state[category][1], number - 1))}, dest))
                if current_state[category][1] >= number:
                    current_state[category] = (
                        max(current_state[category][0], number), current_state[category][1])
                else:
                    break
            elif op == '>':
                if current_state[category][1] > number:
                    queue.append(
                        ({**current_state, category: (max(current_state[category][0], number + 1), current_state[category][1])}, dest))
                if current_state[category][0] <= number:
                    current_state[category] = (current_state[category][0], min(
                        current_state[category][1], number))
                else:
                    break

    return sum((state['x'][1] - state['x'][0] + 1)*(state['m'][1] - state['m'][0] + 1)*(state['a'][1] - state['a'][0] + 1)*(state['s'][1] - state['s'][0] + 1) for state in res)


if __name__ == '__main__':
    print(part1())
    print(part2())

import adventofcode

test_program = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]

def find_loop_acc(program):
    """
    >>> find_loop_acc(test_program)
    5
    """
    return run_program(program)[0]

def find_swap(program):
    """
    >>> find_swap(test_program)
    8
    """
    for i in range(len(program)):
        prog_copy = program.copy()
        if 'acc' not in prog_copy[i]:
            if 'nop' in prog_copy[i]:
                prog_copy[i] = prog_copy[i].replace('nop', 'jmp')
            else:
                prog_copy[i] = prog_copy[i].replace('jmp', 'nop')
            result = run_program(prog_copy)
            if result[1] == 1:
                return result[0]
    return -1

def run_program(program):
    acc = 0
    pc = 0
    prog = parse_program(program)
    while pc < len(prog):
        curr = prog[pc]
        if curr[1] != 0:
            return (acc, 0)
        curr[1] += 1
        inst = curr[0].split()
        if inst[0] == 'nop':
            pc += 1
        if inst[0] == 'acc':
            acc += int(inst[1])
            pc += 1
        if inst[0] == 'jmp':
            pc += int(inst[1])
    return (acc, 1)

def parse_program(program):
    return [[line, 0] for line in program]

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 1782, find_loop_acc(puzzle_input))
    adventofcode.answer(2, 797, find_swap(puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

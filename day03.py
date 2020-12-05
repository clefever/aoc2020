import adventofcode
from math import prod

test_slope = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]

def tree_count(slope_map, right, down):
    """
    >>> tree_count(test_slope, 3, 1)
    7
    """
    trees = 0
    x_loc = 0
    for line in slope_map[down::down]:
        x_loc = (x_loc + right) % len(line)
        if line[x_loc] == '#':
            trees += 1
    return trees

def all_slopes(slope_map):
    """
    >>> all_slopes(test_slope)
    336
    """
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(tree_count(slope_map, slope[0], slope[1]) for slope in slopes)

def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 156, tree_count(puzzle_input, 3, 1))
    adventofcode.answer(2, 3521829480, all_slopes(puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

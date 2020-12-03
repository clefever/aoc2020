import adventofcode

def sum_two_2020(entries):
    """
    >>> sum_two_2020([1721, 979, 366, 299, 675, 1456])
    514579
    """
    for i, entry1 in enumerate(entries, start=1):
        for entry2 in entries[i:]:
            if entry1 + entry2 == 2020:
                return entry1 * entry2
    return -1

def sum_three_2020(entries):
    """
    >>> sum_three_2020([1721, 979, 366, 299, 675, 1456])
    241861950
    """
    for i, entry1 in enumerate(entries, start=1):
        for j, entry2 in enumerate(entries[i:], start=i):
            for entry3 in entries[j:]:
                if entry1 + entry2 + entry3 == 2020:
                    return entry1 * entry2 * entry3
    return -1

def main():
    puzzle_input = adventofcode.read_input(1)
    entries = [int(entry) for entry in puzzle_input]
    adventofcode.answer(1, 1020084, sum_two_2020(entries))
    adventofcode.answer(2, 295086480, sum_three_2020(entries))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

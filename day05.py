import adventofcode
import re

def get_seat_id(seat_code):
    """
    >>> get_seat_id('BFFFBBFRRR')
    567
    >>> get_seat_id('FFFBBBFRRR')
    119
    >>> get_seat_id('BBFFBBFRLL')
    820
    """
    seat_code = re.sub(r'B|R', '1', seat_code)
    seat_code = re.sub(r'F|L', '0', seat_code)
    return int(seat_code[:7], 2) * 8 + int(seat_code[7:], 2)

def max_seat_id(seats):
    return max(get_seat_id(seat) for seat in seats)

def my_seat(seats):
    seat_list = [get_seat_id(seat) for seat in seats]
    seat_list.sort()
    for i in range(len(seat_list)):
        if seat_list[i] != (seat_list[i+1] - 1):
            return seat_list[i] + 1
    return -1

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 818, max_seat_id(puzzle_input))
    adventofcode.answer(2, 559, my_seat(puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

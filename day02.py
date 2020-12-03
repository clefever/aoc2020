import adventofcode
import re

def is_valid_password(line):
    """
    >>> is_valid_password('1-3 a: abcde')
    True
    >>> is_valid_password('1-3 b: cdefg')
    False
    >>> is_valid_password('2-9 c: ccccccccc')
    True
    """
    params = [token for token in re.split(r':|-|\s', line) if token != '']
    lower, upper, char, password = int(params[0]), int(params[1]), params[2], params[3]
    count = password.count(char)
    return count >= lower and count <= upper

def is_valid_password2(line):
    """
    >>> is_valid_password2('1-3 a: abcde')
    True
    >>> is_valid_password2('1-3 b: cdefg')
    False
    >>> is_valid_password2('2-9 c: ccccccccc')
    False
    """
    params = [token for token in re.split(r':|-|\s', line) if token != '']
    pos1, pos2, char, password = int(params[0]), int(params[1]), params[2], params[3]
    return bool(password[pos1-1] == char) != bool(password[pos2-1] == char) 

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 454, sum(1 if is_valid_password(password) else 0 for password in puzzle_input))
    adventofcode.answer(2, 649, sum(1 if is_valid_password2(password) else 0 for password in puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

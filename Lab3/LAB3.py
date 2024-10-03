# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables.
# Use recursion, otherwise no credit will be given
# No helper functions allowed!


def is_power_of(base, num):
    """
    >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
    True
    >>> is_power_of(5, 1)    # pow(5, 0) = 1
    True
    >>> is_power_of(5, 5)    # pow(5, 1) = 5
    True
    >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
    False
    >>> is_power_of(3, 9)
    True
    >>> is_power_of(3, 8)
    False
    >>> is_power_of(3, 10)
    False
    >>> is_power_of(1, 8)
    False
    >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
    False
    >>> is_power_of(4, 16)
    True
    >>> is_power_of(4, 64)
    True
    >>> is_power_of(4, 63)
    False
    >>> is_power_of(4, 65)
    False
    >>> is_power_of(4, 32)
    False
    >>> is_power_of(0, 2)
    False
    """
    return (
        False
        if base == 1 or base == 0
        else num == 1 if num < base else is_power_of(base, num / base)
    )


def cut(a_list):
    """
    >>> cut([7, 4, 0])
    [7, 4, 0]
    >>> myList=[7, 4, -2, 1, 9]
    >>> cut(myList)   # Found(-2) Delete -2 and 1
    [7, 4, 9]
    >>> myList
    [7, 4, -2, 1, 9]
    >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
    [9]
    >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
    []
    >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
    [5, 7, 6, 785, 5, 0, 42]
    """
    if len(a_list) == 0:
        return []
    if a_list[0] < 0:
        rmf = abs(a_list[0])
        return cut(a_list[rmf:])
    return [a_list[0]] + cut(a_list[1:])


def right_max(num_list):
    """
    >>> right_max([3, 7, 2, 8, 6, 4, 5])
    [8, 8, 8, 8, 6, 5, 5]
    >>> right_max([1, 2, 3, 4, 5, 6])
    [6, 6, 6, 6, 6, 6]
    >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
    [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    if len(num_list) == 0:
        return []
    if len(num_list) == 1:
        return num_list
    rest = right_max(num_list[1:])
    return [max(num_list[0], rest[0])] + rest


def consecutive_digits(num):
    """
    >>> consecutive_digits(2222466666678)
    True
    >>> consecutive_digits(12345684562)
    False
    >>> consecutive_digits(122)
    True
    >>> consecutive_digits(123)
    False
    >>> consecutive_digits(123456789)
    False
    >>> consecutive_digits(22)
    True
    >>> consecutive_digits(2)
    False
    """
    return (
        False
        if num < 10
        else True if num % 10 == (num // 10) % 10 else consecutive_digits(num // 10)
    )


def only_evens(num):
    """
    >>> only_evens(4386112)
    4862
    >>> only_evens(0)
    0
    >>> only_evens(357997555531)
    0
    >>> only_evens(13847896213354889741236)
    84862488426
    >>> only_evens(123456789)
    2468
    """
    if num < 10:
        return 0 if num % 2 != 0 else num
    num_next = num % 10
    return only_evens(num // 10) if num_next % 2 != 0 else only_evens(num // 10) * 10 + num_next


def run_tests():
    import doctest

    # - Run tests in all docstrings
    # doctest.testmod(verbose=True)

    # - Run tests per function - Uncomment the next line to run doctest by function. Replace is_power_of with the name of the function you want to test
    #doctest.run_docstring_examples(
    #    only_evens, globals(), name="LAB3", verbose=True
    #)


if __name__ == "__main__":
    run_tests()

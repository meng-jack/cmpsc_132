def countOdd(num_list):
    """
        Returns the number of odd elements in num_list
        * num_list: list of numbers

        >>> countOdd([1,1,1,2,2,5,5,7])
        6
        >>> countOdd([2,4,6,8])
        0
        >>> countOdd([1.5,2,3,3,8])
        3
    """
    odd_count = 0
    for num in range(len(num_list)):
        if num_list[num] % 2 != 0:
            odd_count += 1
    return odd_count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
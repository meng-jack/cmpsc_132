# EXTRA CREDIT LAB
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


# ========= PART 1 ================

from typing import Callable


vector_plus_one = lambda l: [x+1 for x in l]     #-- Replace None with your lambda function

collatz_steps = lambda l:list(map(lambda n:3*n+1 if n%2!=0 else n//2,filter(lambda x:isinstance(x,int) and x>0,l)))
  #-- Replace None with your lambda function

exchange_matrix = lambda n:[[1 if i+j==n-1 else 0 for j in range(n)] for i in range(n)]     #-- Replace None with your lambda function

get_nonzero = lambda m:[(i,j) for i in range(len(m)) for j in range(len(m[i])) if m[i][j]!=0]     #-- Replace None with your lambda function



# ========= PART 2 ================

def mulDigits(num, fn:Callable[[int],bool]) -> int:
    """
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
    """
    prod=1
    while num > 0:
        digit=num%10 # get last digit
        if fn(digit):
            prod*=digit
        num//=10 # remove last digit
    return prod

def getCount(x):
    """
        >>> getCount(6)(62156)
        2
        >>> digit = getCount(7)
        >>> digit(9457845778457077076)
        7
        >>> digit(-945784578457077076)
        6
        >>> getCount(6)(-65062156)
        3
    """
    def count(num):
        count=0
        num=abs(num)
        while num > 0:
            if num%10==x: # check if digit is x
                count+=1 # increment count
            num//=10 # remove last digit
        return count
    return count

class Dual_Iterator:
    """
        >>> it = Dual_Iterator([2, 4, 6, 8, 10])
        >>> next(it)
        2
        >>> next(it)
        4
        >>> next(it)
        6
        >>> it.reverse()
        >>> next(it)
        4
        >>> next(it)
        2
        >>> next(it)
        10
        >>> it.reverse()
        >>> next(it)
        2
        >>> next(it)
        4
        >>> next(it)
        6
        >>> it.reverse()
        >>> next(it)
        4
        >>> next(it)
        2
        >>> next(it)
        10
        >>> next(it)
        8
        >>> next(it)
        6
        >>> it2 = Dual_Iterator([2, 4, 6, 8, 10])
        >>> [next(it2) for _ in range(12)]
        [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4]
        >>> it2.reverse()
        >>> [next(it2) for _ in range(12)]
        [2, 10, 8, 6, 4, 2, 10, 8, 6, 4, 2, 10]
    """
    def __init__(self, sequence):
        self.seq:list=sequence
        self.index:int=-1
        self.reverse_flag:bool=False


    def __iter__(self):  # Do not modify
        return self


    def __next__(self):
        if self.reverse_flag:
            if self.index<=0: # check if the index is already at the start
                self.index=len(self.seq)-1 # loop it back
            else:
                self.index-=1
        else:
            if self.index>=len(self.seq)-1: # check if the index is already at the end
                self.index=0 # loop it front
            else:
                self.index+=1
        return self.seq[self.index]

    def reverse(self):
        self.reverse_flag=not self.reverse_flag # invert the flag


def frange(*args):
    '''
        >>> list(frange(7.5))
        [0, 1, 2, 3, 4, 5, 6, 7]
        >>> seq = frange(0,7, 0.1)
        >>> type(seq)
        <class 'generator'>
        >>> list(seq)
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]
        >>> list(seq)
        []
        >>> list(frange(0,7, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75]
        >>> list(frange(0,7.75, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5]
        >>> list(frange(0,7.75, -0.5))
        []
        >>> list(frange(7.75,0, -0.5))
        [7.75, 7.25, 6.75, 6.25, 5.75, 5.25, 4.75, 4.25, 3.75, 3.25, 2.75, 2.25, 1.75, 1.25, 0.75, 0.25]
    '''
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')

    # - YOUR CODE STARTS HERE
    res=start
    while (step>0 and round(res,10)<stop) or (step<0 and round(res,10)>stop): # mitigate the floating point precision error as we go forward using round()
        yield round(res,10)
        res+=step


# ========= TESTING ASSERTIONS FOR PART 1 - DO NOT MODIFY ================

def test_vector_plus_one():
    assert vector_plus_one([1, 2, 3]) == [2, 3, 4]
    assert vector_plus_one([0, 0, 0]) == [1, 1, 1]
    assert vector_plus_one([-1, -2, -3, -4, -5]) == [0, -1, -2, -3, -4]
    assert vector_plus_one([]) == []
    print('All cases for vector_plus_one passed!')

def test_collatz_steps():
    assert collatz_steps([1, 2, 3, 4]) == [4, 1, 10, 2]
    assert collatz_steps([0, "", -2, 1.5, 2.0]) == []
    assert collatz_steps([-1, -2, -3, -4, -5]) == []
    assert collatz_steps([]) == []
    print('All cases for collatz_steps passed!')


def test_exchange_matrix():
    assert exchange_matrix(1) == [[1]]
    assert exchange_matrix(2) == [[0, 1], [1, 0]]
    assert exchange_matrix(3) == [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    print('All cases for exchange_matrix passed!')


def test_get_nonzero():
    assert get_nonzero([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) == [(0, 0), (1, 1), (2, 2)]
    assert get_nonzero([[-1, 0, 0], [0, 0, 0], [0, 0, -3]]) == [(0, 0), (2, 2)]
    assert get_nonzero([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == []
    print('All cases for get_non_zero passed!')


# ========= STARTER TESTING ================

def run_tests():
    # For Part 1
    #-- Uncomment function per function to test
    test_vector_plus_one()
    test_collatz_steps()
    test_exchange_matrix()
    test_get_nonzero()

    # For Part 2
    import doctest
    # -- Run tests per function - Uncomment the next line to run doctest by function. Replace mulDigits with the name of the function you want to test
    doctest.run_docstring_examples(mulDigits, globals(), name='LAB8',verbose=True)
    doctest.run_docstring_examples(getCount, globals(), name='LAB8',verbose=True)
    doctest.run_docstring_examples(Dual_Iterator, globals(), name='LAB8',verbose=True)
    doctest.run_docstring_examples(frange, globals(), name='LAB8',verbose=True)


if __name__ == "__main__":
    run_tests()

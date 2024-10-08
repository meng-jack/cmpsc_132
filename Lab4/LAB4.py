# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


class Node:  # You are not allowed to modify this class
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__


class Malloc_Library:
    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst
        None -> None -> None -> None -> None
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.free()
        >>> temp.next is None
        True
    """

    def __init__(self):  # You are not allowed to modify the constructor
        self.head = None

    def __repr__(self):  # You are not allowed to modify this method
        current = self.head
        out = []
        while current != None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__

    def __len__(self):
        i = 0
        curr = self.head
        while curr != None:
            i += 1
            curr = curr.next
        return i

    def __setitem__(self, pos, value):
        if pos >= len(self):
            raise IndexError
        curr = self.head
        for i in range(pos):
            curr = curr.next
        curr.value = value

    def __getitem__(self, pos):
        if pos >= len(self):
            return IndexError
        curr = self.head
        for i in range(pos):
            curr = curr.next
        return curr.value

    def malloc(self, size):
        self.head = Node()
        curr = self.head
        for i in range(size - 1):
            curr.next = Node()
            curr = curr.next

    def calloc(self, size):
        self.head = Node(0)
        curr = self.head
        for i in range(size - 1):
            curr.next = Node(0)
            curr = curr.next

    def free(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next is not None:
            temp = curr.next
            curr.next = None
            curr = temp
        self.head = None

    def realloc(self, size):
        if size > len(self):
            if self.head is None:
                self.malloc(size)
            else:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                for i in range(size - len(self)):
                    curr.next = Node()
                    curr = curr.next
        elif size < len(self):
            curr = self.head
            for i in range(size - 1):
                curr = curr.next
            temp = curr.next
            curr.next = None
            while temp is not None:
                temp2 = temp.next
                temp.next = None
        elif size == 0:
            self.free()
        else:
            self.malloc(size)

    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        """
        This method is intended to copy values from one list (original list) to another (pointer_2)
starting at specified positions and up to a given number of nodes (size). The function takes in few
arguments: self is original list or pointer, ptr1_start_idx is the starting position in the original list
from  which  copying  begins,  pointer_2  is  the  target  list  where  the  values  will  be  copied,
ptr2_start_idx is the starting position in the target list where copied values will be placed. Positions
follow the syntax of Python sequences [0, size-1]. No changes are made to the lists when any of
the starting points are not within the corresponding list size. size parameter is the number of values
to be copied from source (self) to destination (pointer_2). If size is larger than original list’s length,
then size becomes the size of the original list.
NOTE :-  Memory allocation is done only when malloc(), calloc() or realloc() methods are called
on the pointer (list). So if there is no memory then, copying of values is not done. This is depicted
in the first examples in the doctests given below.
        """
        


def run_tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    run_tests()

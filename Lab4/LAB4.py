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
        while current is not None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__

    def __len__(self):
        i = 0
        curr = self.head
        while curr is not None:
            i += 1
            curr = curr.next
        return i

    def __setitem__(self, pos, value):
        if pos >= len(self):
            raise IndexError
        curr = self.head
        for i in range(pos):
            curr = curr.next  # type: ignore
        curr.value = value  # type: ignore

    def __getitem__(self, pos):
        if pos >= len(self):
            return IndexError
        curr = self.head
        for i in range(pos):
            curr = curr.next  # type: ignore
        return curr.value  # type: ignore

    def malloc(self, size):
        self.head = Node()
        curr = self.head
        for i in range(size - 1):
            curr.next = Node()  # type: ignore
            curr = curr.next  # type: ignore

    def calloc(self, size):
        self.head = Node(0)
        curr = self.head
        for i in range(size - 1):
            curr.next = Node(0)  # type: ignore
            curr = curr.next  # type: ignore

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
        if len(self) == 0:
            self.malloc(size)
        elif size > len(self):
            if self.head is None:
                self.malloc(size)
            else:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                for i in range(size - len(self)):
                    curr.next = Node()  # type: ignore
                    curr = curr.next  # type: ignore
        elif size < len(self):
            curr = self.head
            for i in range(size - 1):
                curr = curr.next  # type: ignore
            temp = curr.next  # type: ignore
            curr.next = None  # type: ignore
            while temp is not None:
                curr = temp
                temp = temp.next
                curr.next = None
        elif size == 0:
            self.free()

    def memcpy(
        self,
        ptr1_start_idx: int,
        pointer_2: "Malloc_Library",
        ptr2_start_idx: int,
        size: int,
    ) -> None:
        if ptr1_start_idx >= len(self) or ptr2_start_idx >= len(pointer_2):
            return
        if ptr1_start_idx + size > len(self):
            size = len(self) - ptr1_start_idx
        if ptr2_start_idx + size > len(pointer_2):
            size = len(pointer_2) - ptr2_start_idx
        ptr1 = self.head
        for i in range(ptr1_start_idx):
            ptr1 = ptr1.next  # type: ignore
        ptr2 = pointer_2.head
        for i in range(ptr2_start_idx):
            ptr2 = ptr2.next  # type: ignore
        for i in range(size):
            ptr2.value = ptr1.value  # type: ignore
            ptr1 = ptr1.next  # type: ignore
            ptr2 = ptr2.next  # type: ignore


def run_tests():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    run_tests()

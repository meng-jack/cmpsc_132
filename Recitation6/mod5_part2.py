class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class LinkedList:
    '''
>>> lst = LinkedList()
>>> lst.add(4)
>>> lst.add(5)
>>> lst.add(6)
>>> lst
Head:Node(6)
Tail:Node(4)
List:6 -> 5 -> 4
>>> lst.duplicate(6)
>>> lst
Head:Node(6)
Tail:Node(4)
List:6 -> 6 -> 5 -> 4
>>> lst.duplicate(13)
>>> lst
Head:Node(6)
Tail:Node(4)
List:6 -> 6 -> 5 -> 4
>>> lst.add(1)
>>> lst.duplicate(6)
>>> lst
Head:Node(1)
Tail:Node(4)
List:1 -> 6 -> 6 -> 6 -> 6 -> 5 -> 4
>>> lst.duplicate(4)
>>> lst
Head:Node(1)
Tail:Node(4)
List:1 -> 6 -> 6 -> 6 -> 6 -> 5 -> 4 -> 4
    '''

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head, self.tail, out)

    __repr__ = __str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def add(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def duplicate(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                dupe = Node(item)
                dupe.next = current.next
                current.next = dupe
                current = dupe.next
            else:
                current = current.next


# Recitation Activity #12

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.current_node=-1

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__

    def __next__(self):
        if self.current_node is None or self.isEmpty():
            raise StopIteration
        else:
            if self.current_node == -1:
                self.current_node=self.head

            current = self.current_node
            self.current_node = self.current_node.next
            return current

    def isEmpty(self):
        return self.head==None


    def __len__(self):
        return self.count


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.count+=1

    def __iter__(self):
        self.current_node=-1          # - Reinitializes the instance attribute for future iterations
        return self

    # def __getitem__(self,value):
    #     current=self.head
    #     while current is not None:
    #         if current.value==value:
    #             return current
    #         else:
    #             current=current.next
    #     return None
def traverse(linked_object):
    current=linked_object.head
    while current:
        yield current
        current=current.next

my_list=LinkedList()
my_list.add(5)
my_list.add(4)
my_list.add(3)
my_list.add(2)
print(list(traverse(my_list)))
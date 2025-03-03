class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class LinkedList:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start is None
        
    def insert_at_start(self, item):
        newnode = Node(item, self.start)
        self.start = newnode
        
    def insert_at_end(self, item):
        newnode = Node(item)
        if self.is_empty():
            self.start = newnode
            return
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = newnode
        
    def traverse(self):
        if self.is_empty():
            print("List is empty")
            return
        temp = self.start
        while temp:
            print(temp.item, end=" -> ")
            temp = temp.next
        print("None")
        
sll = LinkedList()
sll.insert_at_start(10)
sll.insert_at_end(20)
sll.insert_at_end(40)
sll.traverse()
        
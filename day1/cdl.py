class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, item):
        newNode = Node(item)
        if self.is_empty():
            newNode.prev = newNode
            newNode.next = newNode
        else:
            newNode.next = self.start
            newNode.prev = self.start.prev
            self.start.prev.next = newNode
            self.start.prev=newNode
        self.start = newNode
        
    def insert_at_last(self, item):
        newNode = Node(item)
        if self.is_empty():
            newNode.prev = newNode
            newNode.next = newNode
            self.start = newNode
        else:
            newNode.next = self.start
            newNode.prev= self.start.prev
            newNode.prev.next = newNode
            self.start.prev = newNode
            
    def search(self, item):
        temp = self.start
        if temp == None:
            return None
        if temp.item == item:
            return temp
        else:
            temp = temp.next
            
        while temp != self.start:
            if temp.item == item:
                return temp
            temp = temp.next
        return None
    
    def insert_sfter(self, temp, item):
        if temp is not None:
            newNode = Node(item)
            newNode.next= temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
            
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=' ')
                temp = temp.next
                
    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
    
    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    
    def delete_item(self, item):
            if self.start is not None:
                temp=self.start
                if temp.item==item:
                    self.delete_first()
                else:
                    temp=temp.next
                    while temp is not self.start:
                        if temp.item == item:
                            temp.next.prev = temp.prev
                            temp.prev.next=temp.next
    
    def __iter__(self):
        return CDLIterator(self.start)

class CDLIterator:
    def __init__(self, start):
        self.current=start
        self.count=0
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        item = self.current.item
        self.current=self.current.next
        return item
           
mylist = CircularDoublyLinkedList()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_at_last(40)
mylist.insert_sfter(mylist.search(30), 45)
mylist.delete_last()

for x in mylist:
    print(x, end=' ')
    
print()



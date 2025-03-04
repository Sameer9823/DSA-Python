class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next
        
class SingleLinkedList:
    def __init__(self, start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self, item):
        newnode = Node(item, self.start)
        self.start=newnode
        
    def insert_at_last(self, item):
        newnode = Node(item)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
        else:
            self.start=newnode
            
    def search(self, item):
        temp =self.start
        while temp is not None:
            if temp.item == item:
                return temp
            temp= temp.next
        return None
    
    def insert_in_position(self, temp, item):
        if temp is not None:
            newnode=Node(item, temp.next)
            temp.next=newnode
            
    def printList(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end = ' ')
            temp=temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            
    def delete_item(self, item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==item:
                self.start=None
        else:
            temp=self.start
            if temp.item==item:
                self.start=temp.next
            else:      
                while temp.next is not None:
                    if temp.next.item==item:
                        temp.next=temp.next.next
                        break 
                    temp=temp.next
                    
    def __iter__(self):
        return SllItertor(self.start)
    
class SllItertor:
    def __init__(self, start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        item=self.current.item
        self.current=self.current.next
        return item
    
            
            
sll = SingleLinkedList()
sll.insert_at_start(55)
sll.insert_at_start(53)
sll.insert_at_last(77)
sll.insert_in_position(sll.search(55),28)

# sll.printList()
print()
for x in sll:
    print(x,end=' ')
# sll.delete_last()
# sll.printList()

        
        

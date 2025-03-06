class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class DoubleLinkedList():
    def __init__(self, start=None):
        self.start = start
        
    def is_empty(self):
        return self.start is None
    
    def insert_first(self, item):
        newNode = Node(None, item, self.start)
        if not self.is_empty():
            self.start.prev = newNode
        self.start = newNode
        
    def insert_last(self, item):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next
        
        newNode=Node(temp, item, None)
        if temp == None:
            self.start = newNode
        else:
            temp.next = newNode
            
    def search(self, item):
        temp=self.start
        while temp is not None:
            if temp.item == item:
                return temp
            temp= temp.next
        return None
    def insert_after(self, temp, item):
        if temp is not None:
            newNode=Node(temp,item,temp.next)
            if temp.next is not None:
                temp.next.prev = newNode
            temp.next= newNode
            
    def print_list(self):
        temp= self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
                
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next = None
            
    def delete_item(self, item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==item:
                self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                    if temp.item==item:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        if temp.prev is not None:
                            temp.prev.next = temp.next
                        else:
                            self.start=temp.next
                        break
                    temp=temp.next
    
    def __iter__(self):
        return DoubleLinkedListIterator(self.start)
                    

class DoubleLinkedListIterator:
    def __init__(self, start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data

list=DoubleLinkedList()
list.insert_first(10)
list.insert_last(20)
for x in list:
    print(x, end=' ')
                    
                
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class SingleLinkedList:
    def __init__(self, start=None):
        self.start = start
        
    def is_empty(self):
        return self.start is None
    
    def insert_first(self, item):
        newNode = Node(item, self.start)
        self.start = newNode
        
    def insert_last(self, item):
        newNode = Node(item)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        else:
            self.start = newNode
            
    def insert_item(self, temp, item):
        if temp is not None:
            newNode = Node(item, temp.next)
            temp.next = newNode
            
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.item
    
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            return temp
        
    def search(self, item):
        temp = self.start
        while temp is not None:
            if temp.item == item:
                return temp
            return temp.next
        return None
    
    def delete_item(self, item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == item:
                self.start = None
        else:
            temp = self.start
            if temp.item == item:
                self.start =temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=" -> ")
            temp = temp.next
                    
sll= SingleLinkedList()
sll.insert_first(55)
sll.print_list()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)          #create a new node
        
        if self.head is None:           #if List is empty
            self.head=new_node          
            self.tail=new_node
        else:                           #if the list already contain some value
            self.tail.next=new_node
            self.tail=new_node
        
        self.length += 1

    
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while (temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length -= 1
        if self.length ==0:
            self.head=None
            self.tail=None
        return temp                     #use temp.value to test




my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

# print('Linked List:')
# my_linked_list.print_list()

#(2) Items-Returns 2 Node 
print(my_linked_list.pop())

#(1)Item - returns 1 Node
print(my_linked_list.pop())

#(0) - Returns None
print(my_linked_list.pop())
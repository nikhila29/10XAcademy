# Node 
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# None <- 1 -> None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Forward traversal
    def forwardDisplay(self):
        print('\n')
        temp = self.head
        while (temp != None):
            print(str(temp.val) + "<->", end=" ")
            temp = temp.next
        print('None')
        print('\n')

    # back traversal
    def backwardDisplay(self): 
        # reverse the linked list and print.. -> only was if it was SLL (singly LL)
        # Go to the tail and get it and do backward traversal
        print('\n')
        temp_tail = self.tail
        while (temp_tail != None):
            print(str(temp_tail.val) + "<->", end=" ")
            temp_tail = temp_tail.prev
        print('None')
        print('\n')

    # append(val)
    def append(self, val):
        # this function will just take in the val and append or push 
        # into the Doubly LL
        # always try to write exit first code.
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head # None <- 1 -> None
            return
        
        newNode = Node(val)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
    
    # Insertion After postionX
    def insertAfterPositionX(self, x, val):
        if self.head is None:
            return
        
        if x == 0: # is head  # 1(temp) <-> 2 <-> 3 <-> 4 <-> 5, 
            newNode = Node(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
        temp = self.head
        y = 0
        while (y < x and temp is not None):
            temp = temp.next
            y += 1
        
        if temp is None: # invalid Position
            return  "Invalid position bro"
        
        newNode = Node(val)
        temp1 = temp.next # temp1 3, temp 2
        # new Node links
        newNode.next = temp1
        newNode.prev = temp
        # check temp's links
        temp.next = newNode
        # check temp1 or 3's link # if inserting at the end
        if temp1 is not None:
            temp1.prev = newNode
        else:
            self.tail = newNode

    # Deletion.



# a.append(1) [1, 2, 3, 4, 5,]

dll = DoublyLL() # None..!
dll.append(1) #  None <- 1 -> None [1]
dll.append(2) #  None <- 1 <-> 2 -> None [1, 2]
dll.append(3) #  None <- 1 <-> 2 <-> 3 < -> 4 -> None... [1, 2, 3]
dll.append(4)
dll.append(5)
dll.append(6)


dll.forwardDisplay()
# dll.backwardDisplay()
dll.insertAfterPositionX(2, 7)

dll.forwardDisplay()
dll.backwardDisplay()
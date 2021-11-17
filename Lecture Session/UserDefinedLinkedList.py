class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# # Single linkedlist CRUD - 
# # we talk we should always a head...
# def insertAthead(head, val):
#     # write the for this.

# for i in range():  while (temp != None..):
#     if a[i] == ke
#         return True
#     return false..

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while (temp != None):
            print(str(temp.data) + "->", end=" ")
            temp = temp.next
        print('\n')
    
    def insertAtHeadAndEnd(self, val):
        if self.head is None:
            self.head = Node(val)
            return # the bug was here !! not returning after adding at end

        temp = self.head
        while(temp.next != None):
            temp = temp.next
        
        temp.next = Node(val)

    def InsertAfterPositionX(self , x, val):
        # position starts from 1
        # 3 head, middle , tail
        if x == 0:
            # head insertion
            newNode = Node(val)
            newNode.next = self.head # 1 ->  2 -> 3 ->  4 -> 5 -> None    6 , 7 10
            self.head = newNode
            return # need to return it after adding
        
        # Need cover the invalid positions..
        temp = self.head
        y = 1 # you can also do this by decreasing x..
        while (y < x and temp != None):
            temp = temp.next 
            y += 1
        # after 5 loops temp will become None..
        if temp is None:
            return None
        
        newNode = Node(val)
        newNode.next = temp.next
        temp.next = newNode

    # def InsertBeforePositionX():

    # def InsertAtPositionX():
    
    # linked position starts from 0, 1 ,2 ,3 
    def deleteNodeAtGivenPosition(self, position):
        if self.head is None:
            return # No list provided so returning,
        # Delete the Node
        if position == 0:
            # Delete head
            temp  = self.head
            self.head = temp.next # self.head.next
            del (temp)
            return
        
        temp = self.head
        # a -> b -> c -> d -> e -> None..
        # 0 -> 1 -> 2 -> 3 -> 4 
        # deleting other than head.. position = 
        # y = 0
        while (position > 1 and temp!=None):
            temp = temp.next
            position -= 1
        
        if temp is None and temp.next is None:
            return

        delnode = temp.next
        temp.next  = delnode.next
        del(delnode)

# temp a, position 2 # no loop
# temp b, position 1 # 1st loop.

# temp a, position 3 # no loop
# temp b, posi 2 # 1st loop 
# temp c, posi 1 # 2nd loop

# temp a , y 0 , posi 2  # no loop
# temp b, y 1 , posi 2 # 1 loop

# temp a , y 0 , posi 3  # no loop
# temp b, y 1 , posi 3 # 1 loop
# temp c, y 2 , posi 3 # 1 loop


# dry run of the while loop.
# 1 ->  2 -> 3 ->  4 -> 5
# 7 -> 4, 3 -> 7

# 1 ->  2 -> 3 -> 7 -> 4 -> 5
# y = 1, temp 1 , x 3
# y = 2, temp 2 , x 3
# y = 3, temp 3 , x 3
# complete func(head, x)

linkedlist1 = SingleLinkedList() # .... head = None.. => a = []


linkedlist1.insertAtHeadAndEnd('a')
linkedlist1.insertAtHeadAndEnd('b')
linkedlist1.insertAtHeadAndEnd('c')
linkedlist1.insertAtHeadAndEnd('d')
linkedlist1.insertAtHeadAndEnd('e')
linkedlist1.insertAtHeadAndEnd('f')
linkedlist1.insertAtHeadAndEnd('g')

linkedlist1.display()
# linkedlist1.InsertAfterPositionX(10, 7)
# linkedlist1.display()

linkedlist1.deleteNodeAtGivenPosition(3)

linkedlist1.display()

# print(linkedlist1.getNth(0))
# print(linkedlist1.getNth(3))
# print(linkedlist1.getNth(4))
# print(linkedlist1.getNth(5))
# print(linkedlist1.getNth(10))

# 1 -> 2 -> 3 -> 4 ->
# linkedlist1.head 
# linkedlist1.display()
# linkedlist1.

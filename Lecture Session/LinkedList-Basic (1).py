class Node:
    """
        This is single node class
    """
    def __init__(self, val = None, nextNode = None):
        self.val = val
        self.next = nextNode

node1 = Node(25, None)
node2 = Node(60, None)
node3 = Node(30, None)
node4 = Node(40, None)

print node1.val
print node1.next 

print node1
print node2
print node3

# a = [1, 2, 3]
# 1 -> 2 -> 3
node1.next = node2 # 25 -> 60
print "node1 next after assinging"
print node1.next

node2.next = node3 # 25 -> 60 -> 30
node3.next = node4 # 25 -> 60 -> 30 -> 40 -> None

print node1.val # 25
print node2.val # 60
print node3.next.val #  node3.next ~~~ node4.val
print node1.next.next #  address of node3


print node4.next # None

# 25 -> 60 -> 30 -> 40
# node2  node1 ?

# given a linked list with head node is head tell me the length of the linked list..
head = node1 # head - 25 

# for i in range(len(a)):
# print a[i]
# print a

# head.next = 60
# 25 -> 60 -> 30 -> 40 -> None.
print ("\n")
lengthOfLinkedList = 0
temp = head
while (temp != None):
    lengthOfLinkedList += 1
    temp = temp.next  

# head = 25, temp = 25
# loop 1st time temp = 60 
# loop 2nd time temp = 30
# loop 3rd time temp = 40
# loop 4th time temp = None

# we still have our linkedlist from head in head 
# temp 

print "lenght of Linked List"
print lengthOfLinkedList

print "head after traversal :: "
print  head

print "temp after traversal :: "
print temp













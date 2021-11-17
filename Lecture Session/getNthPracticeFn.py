def getNth(self, index): 
    ####WRITE CODE HERE###
    if index <= 0:
        return None
    if self.head is None:
        return None
    
    temp = self.head
    temp_y = 1
    while(temp_y < index and temp is not None):
        temp = temp.next
        temp_y += 1
    
    if temp is None:
        return None
    
    return temp.data

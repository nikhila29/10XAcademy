# 1. Maintain a List
# 2. Pick an Item 
# 3. Is the Item is it present in the list 
#     a. if it present increase the count of the item
#     b. if it not present add to your list 
# 4. do this for all the items in the list

# items[] - counts[]
# kindle - 1 + 1 = 2
# alexa - 1
# fire phone - 1
# iphone 12 - 1

# [kindle, alexa, firephone]
# range(0, items_len) = range(items_len)
# [0         1          2 .. ] 0 , 1, 2, 3
# [kindle, alexa, firephone]
# [1, 1, 1]

#     (key , value)
# { [kindle , 2], [alexa, 1], [firephone, 1] }

number_of_items = int(input())
items = [] # out list # 1. Maintain a List
counts = []
def istheItemPresentReturnIndex(currItem, items): # [kindle 0, alexa 1, firephone 2] 3
    items_len = len(items)
    for i in range(items_len): # 3 times
        if currItem == items[i]:
            return i
    
    return -1

for index in range(number_of_items):
    currItem = input()  # 2. Pick an Item 
    #3. Is the Item is it present in the list 
    curr_index = istheItemPresentReturnIndex(currItem, items) # -1, (0 - number_of_items-1)
    if curr_index < 0:
        # 3.aif it not present add to your list 
        items.append(currItem)
        counts.append(1)
    else:
        # 3.b if it present increase the count of the item
        # counts[curr_index] = counts[curr_index] + 1
        counts[curr_index] += 1

print("\n\n")
for index in range(len(items)):
    print(items[index] + " --- " + str(counts[index]))




# Dictionary ..!
# { [kindle , 2], [alexa, 1], [firephone, 1] }
# [1, 2, 3, 4]

# Is a (Key, Value) store..
# {
#     'Kindle' : 2,
#     'alexa': 1,
#     'firephone': 1
# }

# CRUD -> Create , Retrieve, Update , Delete , Membership Test

# Create 
# a = [] , a = [1, 2, 3, 4]
# mydict = {} , mydict = {'kindle':2, 'alexa':1}
# Add new values
# a.append(5) [1, 2, 3, 4, 5]
# mydict['firephone'] = 1 # mydict = {'kindle':2, 'alexa':1, 'firephone': 1}

# Retrival 
# a[1] 2  a = [1, 2, 3, 4]
# mydict['kindle'] print 2
# how loop over it..

# Update 
# a[1] = 6 [1, 6, 3, 4, 5]
# mydict['kindle'] = 4 # mydict = {'kindle':4, 'alexa':1, 'firephone': 1}

# Membership Test
# In array you had to loop over all the elemets so -> O(n)
# 'kindle' in mydict true or false -> O(1) 


        



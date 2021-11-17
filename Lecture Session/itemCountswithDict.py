# 1. Maintain a List
# 2. Pick an Item 
# 3. Is the Item is it present in the list 
#     a. if it present increase the count of the item
#     b. if it not present add to your list 
# 4. do this for all the items in the list

number_of_items = int(input())
mydict = {}

for index in range(number_of_items):
    currItem = input()
    if currItem in mydict:
        # true if the item is present a key
        # mydict[currItem] += 1
        mydict[currItem] = mydict[currItem] + 1
    else:
        # false item not present 
        mydict[currItem] = 1

print("\n\n\n")

# how to loop dictionary
for (key, value) in mydict.items():
    print(key + " --- " + str(value))


# Key points 

# new Datastructure dict -> Hashtable / Hashmap
# CRUD 
# why we dictonaries over arrays.


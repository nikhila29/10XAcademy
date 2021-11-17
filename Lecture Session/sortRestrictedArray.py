

num = int(input())
inputArray = []
for index in range(num):
    currInput = int(input())
    inputArray.append(currInput)

print(inputArray)
countsDict = {}
# [1 1 2 2 3 3] {1:1} dict[1] = dict[1] + 1 => {1 : 2}
for index in range(num): # Looping over all the array
    element = inputArray[index]
    if element in countsDict:
        # if it already in we just increase it's count
        countsDict[element] += 1
    else:
        # we add it to the list ..
        countsDict[element] = 1

print("\n\n")
print(countsDict)
print("\n\n")

# We already know that dict keys are only 1 or 2 or 3
# [1, 2, 3, 3, 3, 3, 2] - 7

# python 3.
# {
#   1 : 1,
#   2 : 2,
#   3 : 4
# }
sortedArray = []
for i in range(1,4): #1, 2, 3
    count = countsDict[i]
    for j in range(count): 
        sortedArray.append(i)

print(sortedArray)


# Time complexity

# BestCase complexity Merge Sort ; nlogn
# Quick Sort : nlogn

# Lets analyze out code O(n) + O(n) = O(n)

# values()
# keys()
# del() -> pop()
# len()
# items()

# value = myDict[key]
# del(myDict[key])

# value =  myDict.pop(key)

# for value in myDict.values():
#    print(value)++
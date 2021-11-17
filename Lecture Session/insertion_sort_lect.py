def insertionSort(arr) :
    for i in range(1, len(arr)) :
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [19, 12, 15, 14, 18, 16]
insertionSort(arr)
for i in range(len(arr)):
    print (arr[i])

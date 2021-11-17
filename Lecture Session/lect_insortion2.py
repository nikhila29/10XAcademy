def insertionSort(arr) :
    mid = int((0 + len(arr)-1)/2)

    for i in range(1, mid + 1) :
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    for i in range(mid + 2, len(arr)) :
        key = arr[i]
        j = i-1
        while j >=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [19, 12, -15, 14, -18]
insertionSort(arr)
for i in range(len(arr)):
    print (arr[i])

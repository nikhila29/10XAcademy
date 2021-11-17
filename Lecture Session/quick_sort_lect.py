# implement Quick Sort
class QuickSort:
    arr = []
    def __init__(self, arr):
        self.arr = arr
    # swap
    def swap(self, i,j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
    # partition
    def partition(self, l,h):
        pivot = self.arr[l]
        i = l
        j = h
        while i < j:
            # [60, 20, 5, 40]
            # increment i until we get element greater than pivot
            while self.arr[i]<= pivot and l<h:
                i = i+1 # 4
            # decrement j until we get element less than pivot
            while self.arr[j]> pivot and j>l:
                j = j - 1
            if i < j:
                self.swap(i,j)
        return j # return the expected position of pivot
    # quickSort -> divide and conquer
    def quickSort(self, l, h): # 0, 2
        if l < h:
            p = self.partition(l,h) # 2
            self.swap(l,p)
            self.quickSort(p+1, h) # quick sort on right sub array
            self.quickSort(l, p-1) # quick sort on left sub array
    def sort(self, reverse=False):
        self.quickSort(0, len(self.arr)-1)
        if reverse:
            self.arr = self.arr[::-1]
# q = QuickSort([30, 15, 55, 25, 60, 80, 20])
# print(q.arr)
# q.sort()
# print(q.arr)
# 3
# 1 3 -5
# -2 4 1
# n = int(input())
# arr1 = []
# for i in range(n):
#     arr1.append(int(input()))
# arr2 = []
# for i in range(n):
#     arr2.append(int(input()))
# # ascending Order
# q = QuickSort(arr1)
# q.sort()
# arr1 = q.arr
# print(arr1)
# descending order
q = QuickSort([-2, 4, 1])
q.sort()
arr2 = q.arr
print(arr2)
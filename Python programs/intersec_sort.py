def intersect(nums1, nums2):
    p1=0
    p2=0
    res=[]
    while p1<len(nums1) and p2<len(nums2):
        if nums1[p1]==nums2[p2]:
            res.append(nums1[p1])
            p1+=1
            p2+=1
        elif nums1[p1]>nums2[p2]:
            p2+=1
        else:
            p1+=1
    if len(res)==0:
        res.append(-1)
    return res

    
# DO NOT change anything below this line
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))

    for element in intersect(nums1, nums2):
        print(element)
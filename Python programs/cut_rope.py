def cutRope(A):# 5 1 1 2 3 5--min=1 or len(A)=6
    res=[]     # 5-1, 1-1, 1-1,2-1,3-1,5-1==4 0 0 1 2 4 =min=1 or len(A)=4 (min of 1 are 2 so reduce len(A) by 2)
    n=len(A)    # 4-1, 1-1, 2-1, 4-1=3 0 1 3=min=1
    A.sort()
    count=1
    for i in range(1,len(A)):
        if A[i]==A[i-1]:
            count+=1
        else:
            n-=count
            res.append(n)
            count=1
    return res


# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)
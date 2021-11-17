
def maximum_value(input_numbers):
    return max(input_numbers)
def minimum_value(input_numbers):
    return min(input_numbers)
def get_numbers_in_range(input_numbers, m1, m2):
    lst5=[]
    if m1>m2:
        for i in range(0,len(input_numbers)):
            if input_numbers[i]<=m1 and input_numbers[i]>=m2:
                lst5.append(input_numbers[i])
    elif m1<=m2:
        for i in range(0,len(input_numbers)):
            if input_numbers[i]>=m1 and input_numbers[i]<=m2:
                lst5.append(input_numbers[i])
    if len(lst5)==0:
        return [-1]
    else:
        return lst5

if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]
def even_odd_separator(numbers):
    list=[]
    for i in range(len(numbers)):
        if numbers[i]%2!=0:
            list.append(numbers[i])
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            list.append(numbers[i])
    return list
    
    
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    separated = even_odd_separator(numbers)
    for num in separated:
    	print(num)
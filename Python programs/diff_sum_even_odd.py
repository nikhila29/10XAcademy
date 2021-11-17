def difference_sum_even_odd_index(numbers):
    even=0
    odd=0
    for i in range(len(numbers)):
        
        if i%2==0:
            even+=numbers[i]
        else:
            odd+=numbers[i]
    return even - odd
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))
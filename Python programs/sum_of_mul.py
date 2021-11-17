def sum_of_multiples(numbers,mult):
    sum=0
    for i in numbers:
        if i%mult==0:
            sum+=i 
    return sum





if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    mult = int(input())
    print(sum_of_multiples(numbers, mult))
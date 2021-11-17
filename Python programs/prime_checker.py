def is_prime(input_number):
    f=0
    for i in range(2,input_number):
        if input_number%i==0:
            f=1
            break
    if f==0 and input_number!=1:
        return True
    else:
        return False
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))
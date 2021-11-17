
def factorial(n):
    # Implement this function
    if n<0:
        print("undefined")
    if n==0:
        return 1
    return n*factorial(n-1)

# Do not edit anything below
if __name__ == "__main__":

    n = int(input())
    print(factorial(n))
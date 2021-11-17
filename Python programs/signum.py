def signum(number):
    if number>0:
        return 1
    elif number<0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    test_input = float(input())
    print(signum(test_input))
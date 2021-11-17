def stringInsertionSort(str):
    str_insert=("".join(sorted(input_string)))
    return str_insert

### DO NOT CHANGE ANYTHING BELOW THIS LINE
if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))
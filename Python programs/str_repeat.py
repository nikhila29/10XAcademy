def string_repeat(string_to_repeat, repeat):

    new_str=string_to_repeat+' '
    repeat=int(repeat)
    return (new_str *  repeat)




if __name__ == "__main__":
    input_string = input()
    input_number = input()
    print(string_repeat(input_string, input_number))
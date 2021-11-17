def word_smith(forbidden_alphabets):
    # You can start from here
    def remove(input_string):
        list=' '
        for i in input_string:
            if i not in forbidden_alphabets:
                list+=i 
        return list
    return remove
		
		



### Do not change anything below this line.
if __name__ == "__main__":
    alphabets = [i for i in input().split(' ')]
    input_string = input()
    chopper = word_smith(alphabets)
    print(chopper(input_string))
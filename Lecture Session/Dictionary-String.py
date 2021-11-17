def generate_counts_dict_from_string(input_str):
    # this will return counts dict
    countsDict = {}
    for i in range(len(input_str)):
        char = input_str[i] # r, e , t, u , r, n
        if char in countsDict:
            countsDict[char] += 1
        else:
            countsDict[char] = 1
    
    return countsDict

# {
#     a : 1
#     p : 2
#     l : 1
#     e : 1
# }

def longest_string_is(main_string_counts, small_strings_list):
    max_value = -1
    for i in range(len(small_strings_list)): # apple bad desk banana me this that a abc abcd pple 
        child_string = small_strings_list[i]
        child_string_counts = generate_counts_dict_from_string(child_string)

        print (child_string + " -- count Dict" + str(child_string_counts))

        can_we_make_child_string = True
        for key in child_string_counts: # a , p, l ,e , w
            if key in main_string_counts:
                # child strings count or value for this key should be 
                # <= main string one..
                if child_string_counts[key] > main_string_counts[key]:
                    can_we_make_child_string = False
            else:
                can_we_make_child_string = False
                break
        
        print (child_string + "---" + str(can_we_make_child_string))
        if can_we_make_child_string and max_value < len(child_string):
            max_value = len(child_string)
    
    return max_value


main_string = input()
small_strings = input()


small_strings_list = small_strings.split(' ')
print(main_string)
print("\n")
print(small_strings_list)

main_string_counts = generate_counts_dict_from_string(main_string)
print(longest_string_is(main_string_counts, small_strings_list))



#O(m) + (O(1000) * O(1000))

#O(m) + (O(1000))

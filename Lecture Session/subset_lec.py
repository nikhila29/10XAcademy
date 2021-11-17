def subset_helper(inp, out) :
    if len(inp) == 0 :
        print(out)
        return 
    out1 = out    # exclusion
    out2 = out + inp[0:1]   #inclusion
    i = 1
    while i+1 < len(inp) and inp[i] == inp[i+1] :
        i = i+1
    subset_helper(inp[i:], out1)
    subset_helper(inp[i:], out2)

def subset(str) :
   if len(str) == 0 :
       return
   subset_helper(''.join(sorted(str)), "")    

subset("abcb")

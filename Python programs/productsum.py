n=input()
def ProductAndSum(n):
    sum=0
    product=1
    for i in n:
        sum=sum+int(i)
        product=product*int(i)
    return product-sum 
print(ProductAndSum(n))    
       

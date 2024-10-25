def count_even_odd(lst):
    # Your code goes here
    even_count = 0
    odd_count = 0
    for l in lst:
        if l%2==0:
            even_count+=1
        else:
            odd_count+=1 
            
    return even_count, odd_count
    
a=count_even_odd([1,2,3,4,5,6,7,8,9,10,-1,-2,3.5])
print(f"Even and odd are {a} respectively")

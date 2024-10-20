def check_unique(lst):
    # Your code goes here
    s=set()
    for num in lst:
        if num in s:
            return False
            
        s.add(num)
        
    return True
    
print(check_unique([1,2,3,4,4,5]))

def rotate_list(lst, k):
    # Your code goes here
    if not lst:
        return []
        k = k % len(lst)
    for _ in range(k):
        last_element = lst.pop()
        lst.insert(0, last_element)
    
    return lst
    
print(rotate_list([1,2,3,4,5,6],3))


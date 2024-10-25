def is_subset(lst1, lst2):
    # Your code goes here
    for element in lst1:
        found = False
        for item in lst2:
            if item == element:
                found = True
                break
        if not found:
            return element,item,"is in the list"
    return True
print(is_subset([1,2,3],[1,2,3,4,5]))


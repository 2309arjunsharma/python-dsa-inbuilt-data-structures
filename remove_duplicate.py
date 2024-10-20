def remove_duplicates(lst):
    # Your code goes here
    list=[]
    for i in lst:
        if i not in list:
            list.append(i)
    return list
        
print(remove_duplicates([1,2,2,3,4,4,4,5,6,6]))
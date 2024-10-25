
def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    if(len(keys) != len(values)):
        return False
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
 
    return result
    
print(merge_lists_to_dictionary(['a','b','c'],[1,2,3]))
print('a'+'b'+'c')

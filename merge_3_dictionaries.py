def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = value
    for key, value in dict3.items():
        merged_dict[key] = value
    
    return merged_dict
    
print(merge_three_dictionaries({'a':10, 'b':20}, {'c':30, 'd':40}, {'e':50, 'f':100}))


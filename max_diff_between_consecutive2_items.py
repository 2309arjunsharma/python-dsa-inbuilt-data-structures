def max_consecutive_difference(lst):
    # Your code goes here
    if len(lst) < 2:
        return 0
    diffence = 0
    for i in range(1, len(lst)):
        current_diff = abs(lst[i] - lst[i - 1])
        if current_diff > diffence:
            diffence=current_diff
    return diffence

print(max_consecutive_difference([1,2,3,4,56]))
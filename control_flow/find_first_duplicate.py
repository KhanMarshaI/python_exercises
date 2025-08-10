# **Find First Duplicate**  
# Implement `first_duplicate(seq)` that returns the first value that appears twice, 
# using a `for`/`else` construct.

def first_duplicate(seq):
    seen = set()
    for item in seq:
        if item in seen:
            return item
        seen.add(item)
    else:
        return -1
    

print(first_duplicate([1,3,2,1,2,4,5,4,5]))
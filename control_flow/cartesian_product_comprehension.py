# Given two lists of numbers, create a list of (a, b, a*b) tuples for every combination where a*b is even.

list1 = [4,2,11,7,9]
list2 = [3,8,5,13,15]

cartesianList = [(a,b,a*b) for a in list1 for b in list2 if a*b %2 == 0]

print(cartesianList)
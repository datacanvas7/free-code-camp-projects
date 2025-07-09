from mean_var_std import calculate

# Test cases
print(calculate([0,1,2,3,4,5,6,7,8]))
print(calculate([2,6,2,8,4,0,1,5,7]))
try:
    print(calculate([1,2,3]))  # Should raise ValueError
except ValueError as e:
    print(e)
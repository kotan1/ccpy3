#%%
n = [1, 3, 5, 7]
print n
n.pop(1)
# Returns 3 (the item at index 1)
print n

n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n

del(n[1])
# Doesn't return anything
print n

#%%
n = [1, 3, 5]
print n
# Remove the first item in the list here
n.remove(1)
print n
n.pop(0)
print n
del(n[0])
print n
#%%
c = ['C' for x in range(5) if x < 3]
print c

#%%
cubes_by_four = [x ** 3 for x in range(1, 11) if x ** 3 % 4 == 0]
print cubes_by_four
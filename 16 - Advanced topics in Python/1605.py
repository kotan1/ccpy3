#%%
new_list = [x for x in range(1, 6)]
print new_list

doubles = [x * 2 for x in range(1, 6)]
print doubles

doubles_by_3 = [x * 2 for x in range(1, 7) if (x * 2) % 3 == 0]
print doubles_by_3
#%%
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print even_squares
#%%
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print item

#%%
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9], [10, 11, 12]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  
  return results

print flatten(n)
#%%
def double_first(n):
  n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
print numbers
double_first(numbers)
print numbers

#%%
def list_function(x):
  x[1] += 3
  return x

n = [3, 5, 7]
print n
print list_function(n)
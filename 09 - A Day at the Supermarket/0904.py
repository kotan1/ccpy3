#%%
def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print small

#%%
# Write your function below!
def fizz_count(x):
  total = 0
  for word in x:
    if word == 'fizz':
      total += 1
  
  return total

fizz_count(["fizz","cat","fizz"])
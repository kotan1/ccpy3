def product(n):
  res = 1
  
  for i in n:
    res *= i
  
  return res

print product([4, 5, 5])
def factorial(x):
  res = 1
  
  for i in range(2, x + 1):
    res *= i
    
  return res

print factorial(3)
print factorial(10)
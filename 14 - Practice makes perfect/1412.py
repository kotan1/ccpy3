def purify(n):
  res = []
  
  for i in n:
    if i % 2 == 0:
      res.append(i)
  
  return res

print purify([1,2,3])
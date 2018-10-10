def remove_duplicates(n):
  res = []
  
  for i in n:
    if i not in res:
      res.append(i)
      
  return res

print remove_duplicates([1, 1, 2, 2])
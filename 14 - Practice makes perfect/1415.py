def median(n):
  res = 0
  
  if(len(n) == 1):
    return n[0]
  elif (len(n) == 2):
    return 0.5 * (n[0] + n[1])
  elif (len(n) % 2 == 1):
  	res = sorted(n)[len(n)/2]
  else:
    res = 0.5 * (sorted(n)[len(n)/2 - 1] + sorted(n)[len(n)/2])
  return res

print median([1, 1, 2])
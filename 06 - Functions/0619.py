def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return "Nope"

print distance_from_zero(-3.14)
print distance_from_zero("asdf")
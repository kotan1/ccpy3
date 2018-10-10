def is_int(x):
  if abs(x) - int(abs(x)) == 0:
    return True
  else:
    return False

print is_int(-1)
print is_int(-7.0)
print is_int(3.14159)
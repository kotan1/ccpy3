def flip_bit(number, n):
  mask = 0b1 << (n - 1)
  return bin(number ^ mask)

print int(flip_bit(255,  8), 2)
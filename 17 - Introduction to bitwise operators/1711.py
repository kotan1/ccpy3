def check_bit4(input):
  mask = 0b1000
  if(input & mask):
    return "on"
  else:
    return "off"

print check_bit4(0b101001)
print check_bit4(0b110110)
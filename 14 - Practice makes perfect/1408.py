def anti_vowel(text):
  vowels = "aeouiAEOUI"
  res = ""
  
  for c in text:
    if c not in vowels:
      res += c
      
  return res

print anti_vowel("Hey You!")
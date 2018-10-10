def reverse(s):
  res = ""
  
  for i in range(len(s) - 1, -1, -1):
  	res += s[i]
    
  return res

print reverse("")
print reverse("K#t@n!")
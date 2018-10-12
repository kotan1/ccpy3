#%%
for number in range(5):
  print number,

print 

d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key],

print 

for letter in "Eric":
  print letter,  # note the comma!
  
print

#%%
my_dict = {
  "cat": 1,
  "dog": 2,
  "pig": 3
}

print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]
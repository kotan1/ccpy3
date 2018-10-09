#%%
letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters
#%%
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("cat")
suitcase.append("lunchbox")
suitcase.append("hat")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
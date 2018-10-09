#%%
animals = ["ant", "bat", "cat"]
print animals
#print animals.index("bat")
animals.insert(animals.index("bat"), "dog")
print animals

#%%
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"
print animals

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation
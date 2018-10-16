#%%
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive

#%%

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Zippo", 3)
hippo.description()
sloth = Animal("Bob", 4)
ocelot = Animal("Toleco", 2)

print hippo.health
print sloth.health
print ocelot.health

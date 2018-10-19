class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    while len(start) > 0:
      current_vertex = start.pop(0)
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertex = self.graph_dict[current_vertex]
        next_vertices = vertex.get_edges()
        start += next_vertices
     
    return False
   

no_path_exists = True


directed_railway = Graph(True)

callan_station = Vertex('callan')
peel_station = Vertex('peel')
ulfstead_station = Vertex('ulfstead')
harwick_station = Vertex('harwick')

directed_railway.add_vertex(callan_station)
directed_railway.add_vertex(peel_station)
directed_railway.add_vertex(harwick_station)
directed_railway.add_vertex(ulfstead_station)

directed_railway.add_edge(harwick_station, peel_station)
directed_railway.add_edge(peel_station, callan_station)


path_exists = directed_railway.find_path('harwick', 'harwick')
print(path_exists)

#Uncomment for final checkpoint

print("\n\n\nFinding path from harwick to callan\n")
new_path_exists = directed_railway.find_path('harwick', 'callan')
print(new_path_exists)
print("\n\nTrying to find path from harwick to ulfstead\n")
no_path_exists = directed_railway.find_path('harwick', 'ulfstead')
print(no_path_exists)


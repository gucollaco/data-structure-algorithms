from collections import defaultdict

# path finding algorithm using breadth first search
# implementation can be found on: https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph
# this class represents a directed graph using adjacency list representation
class Graph:
  def __init__(self,vertices):
    self.V= vertices #No. of vertices
    self.graph = defaultdict(list) # default dictionary to store graph

  # function to add an edge to graph
  def addEdge(self,u,v):
    self.graph[u].append(v)
    
  # use BFS to check path between s and d
  def isReachable(self, s, d):
    # mark all the vertices as not visited
    visited =[False]*(self.V)

    # create a queue for BFS
    queue=[]

    # mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:
      # dequeue a vertex from queue
      n = queue.pop(0)
        
      # if this adjacent node is the destination node,
      # then return true
      if n == d:
        return True

      # else, continue to do BFS
      for i in self.graph[n]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True

    # if BFS is complete without visited d
    return False

# polynomial example (path finding algorithm)
def polynomial_example():
  print("_______________________________________")
  print("** Polynomial Example (Path finding) **")
  # create a simple graph
  simple_graph = Graph(5)
  print("Graph created, with 5 vertices (indices 0, 1, 2, 3 and 4).")
  simple_graph.addEdge(0, 1)
  print("Edge added from 0 to 1")
  simple_graph.addEdge(0, 2)
  print("Edge added from 0 to 2")
  simple_graph.addEdge(0, 3)
  print("Edge added from 0 to 3")
  simple_graph.addEdge(1, 4)
  print("Edge added from 1 to 4")
  simple_graph.addEdge(2, 4)
  print("Edge added from 2 to 4")
  simple_graph.addEdge(3, 4)  
  print("Edge added from 3 to 4")

  # checking if some paths are found
  u, v = 0, 4
  if simple_graph.isReachable(u, v):
    print("A path was found from " + str(u) + " to " + str(v))
  else:
    print("No path was found from " + str(u) + " to " + str(v))

  u, v = 0, 2
  if simple_graph.isReachable(u, v):
    print("A path was found from " + str(u) + " to " + str(v))
  else:
    print("No path was found from " + str(u) + " to " + str(v))

  u, v = 3, 0
  if simple_graph.isReachable(u, v):
    print("A path was found from " + str(u) + " to " + str(v))
  else:
    print("No path was found from " + str(u) + " to " + str(v))

  u, v = 1, 2
  if simple_graph.isReachable(u, v):
    print("A path was found from " + str(u) + " to " + str(v))
  else:
    print("No path was found from " + str(u) + " to " + str(v))

  return

# method to find the hamiltonian path
# implementation can be found on: https://stackoverflow.com/questions/47982604/hamiltonian-path-using-python
def hamilton_path(G, size, pt, path=[]):
  print('Hamiltonian path called with Vertex={} (Current Path={})'.format(pt, path))
  if pt not in set(path):
    path.append(pt)
    if len(path)==size:
      return path
    for pt_next in G.get(pt, []):
      res_path = [i for i in path]
      candidate = hamilton_path(G, size, pt_next, res_path)
      if candidate is not None:  # skip loop or dead end
        return candidate
    print('Path {} is a dead end'.format(path))
  else:
    print('Vertex {} is already in path {}'.format(pt, path))
  # loop or dead end, None is implicitly returned

# nondeterministic polynomial example (hamiltonian path)
def nondeterministic_polynomial_example():
  print("\n____________________________________________________________")
  print("** Nondeterministic Polynomial Example (Hamiltonian path) **")

  print("\n* Example where a Hamiltonian path CAN'T be found *")
  simple_graph = {1:[2,3], 2:[4], 3:[4], 4:[]}
  print("Graph: " + str(simple_graph))
  print("Starting point: 1")
  path = hamilton_path(simple_graph, 4, 1, [])
  if path != None:
    print('The following path is a hamiltonian path for the given graph: ' + str(path))
  else:
    print('No hamiltonian path could be found starting from the given point')

  print("\n____________________________________________________________")
  print("** Nondeterministic Polynomial Example (Hamiltonian path) **")
  print("\n* Example where a Hamiltonian path CAN be found *")
  simple_graph = {1:[2,3], 2:[3,4], 3:[4], 4:[]}
  print("Graph: " + str(simple_graph))
  print("Starting point: 1")
  path = hamilton_path(simple_graph, 4, 1, [])
  if path != None:
    print('The following path is a hamiltonian path for the given graph: ' + str(path))
  else:
    print('No hamiltonian path could be found starting from the given point')

# main function
def main():
  polynomial_example()
  nondeterministic_polynomial_example()

# calling the main function
if __name__ == "__main__":
  main()

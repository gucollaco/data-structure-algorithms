# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

from collections import defaultdict

# DFS implementation
# imported from: https://stackoverflow.com/questions/29320556/finding-longest-path-in-a-graph
def DFS(G,v,seen=None,path=None):
  if seen is None: seen = []
  if path is None: path = [v]

  seen.append(v)

  paths = []
  for t in G[v]:
    if t not in seen:
      t_path = path + [t]
      paths.append(tuple(t_path))
      paths.extend(DFS(G, t, seen[:], t_path))
  return paths

# main function
def main():
  answers = []
  while True:
    try:
      # the received values
      values = input()
      N, M = list(map(int, values.split()))

      # break execution when both N and M are 0 
      if (N == 0 and M == 0):
        break
      
      # here we receive the connection inputs, for N rows
      connection_rows = []
      counter = 0
      for _ in range(N):
        connection_row = input()

        # add a node name representation
        new = []
        for element in connection_row:
          if (element == '.'):
            new.append(str(counter))
            counter += 1
          else:
            new.append(element)
        connection_rows.append(new)
      
      # here we will keep the edges that has connection
      # having an edge representation of the graph
      edges = []
      for i in range(N):
        for j in range(M):
          if (connection_rows[i][j] != '#'):
            # here we check if there is a connection with the elements on top, bottom, left or right
            if (i > 0):
              if (connection_rows[i-1][j] != '#' and [connection_rows[i-1][j], connection_rows[i][j]] not in edges):
                edges.append([connection_rows[i-1][j], connection_rows[i][j]])
            if (i < (N-1)):
              if (connection_rows[i+1][j] != '#' and [connection_rows[i+1][j], connection_rows[i][j]] not in edges):
                edges.append([connection_rows[i+1][j], connection_rows[i][j]])
            if (j > 0):
              if (connection_rows[i][j-1] != '#' and [connection_rows[i][j], connection_rows[i][j-1]] not in edges):
                edges.append([connection_rows[i][j], connection_rows[i][j-1]])
            if (j < (M-1)):
              if (connection_rows[i][j+1] != '#' and [connection_rows[i][j], connection_rows[i][j+1]] not in edges):
                edges.append([connection_rows[i][j], connection_rows[i][j+1]])
      
      # build the graph dictionary, based on the edges list
      G = defaultdict(list)
      for (s,t) in edges:
        G[s].append(t)

      # gets all paths
      all_paths = []
      for node in set(G.keys()):
        for path in DFS(G, node):
          all_paths.append(path)
      
      # gets the length of the longest path, and prints it
      max_path_len = max(len(p) for p in all_paths) - 1
      answers.append(max_path_len)
      
      # we could print the values directly
      # print(max_path_len)

    # while loop breaks on EOF
    except EOFError:
      break

  # printing the values at the end
  for val in answers:
    print(val)

# calling the main function
if __name__ == "__main__":
  main()

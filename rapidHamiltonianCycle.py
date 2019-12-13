def hamiltonian(path, vertices):
  if len(set(path)) < vertices:
    return "NO"
  for i in range(vertices-1):
    if matrix[path[i]][path[i+1]] != 1:
      return "NO"
  if matrix[path[-1]][path[0]] != 1:
    return "NO"

  return "YES"

vertices, edges = input().split()
vertices, edges = int(vertices), int(edges)

matrix = [[0]*vertices for l in range(vertices)]

for edge in range(edges):
  v1, v2 = input().split()
  v1, v2 = int(v1), int(v2)
  matrix[v1][v2] = 1
  matrix[v2][v1] = 1

tests = int(input())

for test in range(tests):
  path = [int(v) for v in input().split()]
  print(hamiltonian(path, vertices))

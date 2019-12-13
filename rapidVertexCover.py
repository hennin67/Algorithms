def main():
  vertices, edges, tested = map(int, input().split())

  combos = [None]*vertices
  for pair in range(vertices):
    combos[pair] = set()

  for edge in range(edges):
    v1,v2 = map(int, input().split())
    combos[v1].add(v2)
    combos[v2].add(v1)

  print(vertices, int((vertices*(vertices-1))/2-edges), vertices-tested)

  for i in range(vertices):
    for j in range(i+1,vertices):
      if j not in combos[i]:
        print(i,j)

main()

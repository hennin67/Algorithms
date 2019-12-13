def main():
  vertices, pairs = input().split()
  vertices, pairs = int(vertices), int(pairs)
  vlist = [set()]*vertices

  for pair in range(pairs):
    s1, s2, w = input().split()
    s1, s2, w = int(s1), int(s2), int(w)
    if not vlist[s1]:
      vlist[s1] = set([(s2,w)])
    else:
      vlist[s1].add((s2,w))
    if not vlist[s2]:
      vlist[s2] = set([(s1,w)])
    else:
      vlist[s2].add((s1,w))

  total = 0
  edges = []
  vertex = 0
  used = [vertex]

  while True:
    edges = edges + [x for x in vlist[vertex] if x not in used]
    edges.sort(key=lambda x: x[1], reverse=True)
    if edges:
      temp = edges.pop()
    while temp[0] in used:
      if not len(edges):
        temp = -1
        break
      temp = edges.pop()
    if temp == -1:
      break
    vertex = temp[0]
    used.append(vertex)
    total += temp[1]

  print(total)

if __name__ == "__main__":
  main()

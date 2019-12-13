vlist = dict()
visited = dict()
sites, connections = input().split()
sites, connections = int(sites), int(connections)

for site in range(sites):
  vlist[site] = set()
  visited[site] = -1

for connection in range(connections):
  temp = [int(x) for x in input().split()]
  vlist[temp[0]].add(temp[1])
  vlist[temp[1]].add(temp[0])

s = 0
q = []
q.append(s)
visited[s] = 1
count = 1
while True:
  while q:
    s = q.pop(0)
    for i in vlist[s]:
      if visited[i] == -1:
        q.append(i)
        visited[i] = 1
  done = True
  for key in visited:
    if visited[key] == -1:
      s = key
      q.append(s)
      visited[s] = 1
      done = False
      count += 1
      break
  if done:
    break

print(count)

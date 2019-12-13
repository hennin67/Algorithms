from itertools import combinations

vlist = dict()
vertices, pairs = input().split()
vertices, pairs = int(vertices), int(pairs)

for pair in range(vertices):
  vlist[pair] = set()

for pair in range(pairs):
  curr = [int(x) for x in input().split()]
  vlist[curr[0]].add(curr[1])
  vlist[curr[1]].add(curr[0])

key = max(vlist, key=lambda x:len(vlist[x]))
item = vlist[key]
comb = combinations(item, 2)
print(len(list(comb))+len(item))

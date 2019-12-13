def main():
  sites, pairs = input().split()
  sites, pairs = int(sites), int(pairs)

  pairV = []
  options = [set()]*sites

  for pairs in range(pairs):
    s1, s2 = input().split()
    s1, s2 = int(s1), int(s2)
    pairV.append((s1,s2))
    if not options[s1]:
      options[s1] = set([s2])
    else:
      options[s1].add(s2)
    if not options[s2]:
      options[s2] = set([s1])
    else:
      options[s2].add(s1)

  mx = 0
  for i in pairV:
    a = i[0]
    b = i[1]
    s1 = options[a]
    s2 = options[b]
    s3 = s1.copy()
    s3.update(s2)
    c = len(s3)
    if c > mx:
      mx = c

  print(int((mx*(mx-1))/2))

main()

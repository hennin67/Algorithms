class MyBest:
  best = 0

  def Solve(self, options, included, need, sites, excluded):
    # if items already excluded, only keep going if remaining items fit need
    if len(excluded):
      incl = included[:]
      ne = need[:]
      for i in options:
        i = i[0]
        incl.append(i)
        ne = [(s[0],s[1]-{i}) for s in ne if len(s[1]-{i}) > 0 and s[0] not in incl]
      if len(ne) != 0:
        return sites+1

    options.sort(key=lambda t: len(t[1]))
    inc = len(included)

    #if already worse than best, quit
    if inc >= self.best:
      return sites + 1

    # if have everything needed
    if not len(need):
      if inc < self.best:
        self.best = inc
      return inc

    # if have everything but 1 in needed
    if len(need) == 1:
      if inc + 1 < self.best:
        self.best = inc + 1
      return inc + 1

    # if ran out of options
    if not len(options):
      return sites + 1

    # i : item to include or exclude
    # temp : items which must be included if i excluded
    i, temp = options.pop()
    included.append(i)

    needInc = [(s[0],s[1]-{i}) for s in need if len(s[1]-{i}) > 0 and s[0] not in included]

    in_result = self.Solve(options[:], included[:], needInc[:], sites, excluded[:]);

    excluded.append(included.pop())

    # include items which must be included due to item being excluded
    toDelete = []
    for site in reversed(range(len(options))):
      if options[site][0] in temp:
        toDelete.append(site)
        i = options[site][0]
        included.append(i)
        need = [(s[0],s[1]-{i}) for s in need if len(s[1]-{i}) > 0 and s[0] not in included]
    for d in toDelete:
      options.pop(d)

    out_result = self.Solve(options[:], included[:], need[:], sites, excluded[:]);

    if in_result < out_result:
      return in_result
    return out_result

def main():
  sites, connections = input().split()
  sites, connections = int(sites), int(connections)

  options = [set()]*sites

  for connection in range(connections):
    s1, s2 = input().split()
    s1, s2 = int(s1), int(s2)
    if not options[s1]:
      options[s1] = set([s2])
    else:
      options[s1].add(s2)
    if not options[s2]:
      options[s2] = set([s1])
    else:
      options[s2].add(s1)

  for site in range(len(options)):
    options[site] = (site, options[site])

  c = MyBest()
  c.best = sites + 1
  print(c.Solve(options[:], [], options[:], sites, []))

if __name__ == "__main__":
  main()

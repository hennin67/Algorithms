class MyBest:
  best = 0

  def Solve(self, options, included, need, ppl, exc):
    #ONLY WHEN SOMEONE EXCLUDED ALREADY
    if exc:
      if len(list(set(need) - set(x for l in options for x in l))) != 0:
        return ppl

    inc = len(included)
    nee = len(need)

    # if already worse than best, quit
    if inc >= self.best:
      return ppl

    # if no more skills needed
    if not nee:
      if inc < self.best:
        self.best = inc
      return inc

    # if one more skill needed
    if nee == 1:
      if inc+1 < self.best:
        self.best = inc+1
      return inc+1

    # if ran out of options
    if not len(options):
      return ppl

    # get rid of item if not in need
    temp = options.pop()
    diff = list(set(need) - set(temp))
    while len(diff) == len(need) and len(options):
      temp = options.pop()
      diff = list(set(need) - temp)
    # remove subsets and sort
    optionsInc = [s-temp for s in options if len(s-temp) > 0]
    optionsInc.sort(key=len)
    included.append(temp)
    exc = True

    in_result = self.Solve(list(optionsInc), included, diff, ppl, exc);

    included.pop()
    out_result = self.Solve(options, included, need, ppl, exc);

    if in_result < out_result:
      return in_result
    return out_result

def main():
  #turn strings into numbers
  count = 0
  items = dict()
  ppl, size = input().split()
  ppl = int(ppl)
  need = {skill for skill in input().split()}

  options = []
  for person in range(ppl):
    temp = []
    num = int(input())
    for skill in input().split():
      if skill in need:
        if skill not in items:
          items[skill] = [count,1]
          count+=1
        else:
          items[skill][1]+=1
        temp.append(items[skill][0])

    if len(temp):
      options.append(set(temp))

  need = [items[skill][0] for skill in need]

  #get rid of subsets
  sets = [set(l) for l in options]
  options = [l for l,s in zip(options,sets) if not any(s < other for other in sets)]

  included = []
  # get rid of unique items
  unique = [skill for skill in items.keys() if items[skill][1]==1]
  if len(unique):
    for l in options:
      for skill in unique:
        if skill in l:
          need = list(set(need) - set(l))
          included.append(l)
          unique.remove(skill)
          break

    options = [l for l in options if l not in included]

  #sort items
  options.sort(key=len)

  c = MyBest()
  c.best = ppl+1
  print(c.Solve(options, included, need, ppl+1, exc = False))

if __name__ == "__main__":
  main()

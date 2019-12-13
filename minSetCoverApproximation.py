import time
import collections

def main():
  start = time.time()
  crew, needed = map(int, input().split())
  options = [None]*crew
  skills = [0]*needed

  for person in range(crew):
    input()
    options[person] = (person, set())
    for skill in input().split():
        options[person][1].add(int(skill))
        skills[int(skill)]+=1

  # find unique skills
  unique = {i for i,skill in enumerate(skills) if skill == 1}
  # add people who have unique skills
  included = [person[0] for person in options if person[1]&unique]
  # get fulfilled skills
  fulfilled = {skill for person in options for skill in person[1] if person[0] in included}
  # get current options
  options = [(person[0],person[1]-fulfilled) for person in options if person[0] not in included and person[1]-fulfilled]

  while len(fulfilled) < needed: #and (time.time()-start) < 9.95:
    # get value of each person
    values = [[x for x in person[1]] for person in options]
    values = [x for y in values for x in y]
    dic = collections.Counter(values)

    # give each person a score based on need
    for person in range(len(options)):
      value = 0
      items = options[person][1]
      for item in items:
        value += (crew-dic[item])
      options[person] = (options[person][0], options[person][1], value)

    # sort by least value summation THEN by number of skills
    options.sort(key=lambda x: x[2] or len(x[1]))

    temp = options.pop()
    included.append(temp[0])
    fulfilled.update(temp[1])
    options = [(person[0],person[1]-fulfilled) for person in options if person[0] not in included and person[1]-fulfilled]

  # get rid of excess guys whose skills have been covered by everyone else

  print(len(included))
  included.sort()
  print(" ".join(str(x) for x in included))

main()

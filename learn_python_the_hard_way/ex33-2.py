# TODO: Revise ex33.py from Study Drils

def testwhile(limit, incr):
  i = 0
  numbers = []

  while i < limit:
    print(f"At the top, i is {i}")
    numbers.append(i)

    i = i + incr
    print("Numbers now: ", numbers)
    print(f"At the bottom, i is {i}")

  return numbers

def testwithfor(limit, incr):
  numbers = []

  for i in range(0, limit, incr):
    print(f"At the top, i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)
    print(f"At the bottom, i is {i}")

  return numbers


#numbers = testwhile(6, 2)
numbers = testwithfor(6, 2)
print("The numbers:")
for n in numbers:
  print(n)

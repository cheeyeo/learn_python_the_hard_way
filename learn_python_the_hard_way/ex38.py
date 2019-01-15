ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("There are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 7, "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print(f"Adding {next_one}")
  stuff.append(next_one)
  print(f"There are {len(stuff)} items now.")


print("There we go: ", stuff)
print("Let's do things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

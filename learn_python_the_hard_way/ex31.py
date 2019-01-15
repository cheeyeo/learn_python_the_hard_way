print("""You enter a dark room with two doors.
Do you go through door 1 or door 2?""")

door = input("> ")

if door == "1":
  print("There's a giant bear here eating.")
  print("What do you do?")
  print("1. Take the cake.")
  print("2. Scream at the bear.")

  bear = input("> ")

  if bear == "1":
    print("The bear eats your face off. Good job!")
  elif bear == "2":
    print("The bear eats your legs off. Good job!")
  else:
    print(f"Well, doing {bear} is probably better. Bear runs away.")

elif door == "2":
  print("You stare into the endless abyss at Cthulu's retina")
  print("1. Blueberries")
  print("2. Yellow jacket")
  print("3. Understanding revolvers yelling melodies.")

  insanity = input("> ")

  if insanity == "1":
    print("Your body survivies powered by a mind of jello.")
  else:
    print("The insanity rots you into a pool of muck.")
    print("Good Job!")
else:
  print("You stumble around and fall on a knife and die. Good Job!")

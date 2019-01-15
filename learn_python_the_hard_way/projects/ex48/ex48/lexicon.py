def scan(inputz):
  lexicon = {
    "direction": ["north", "south", "east", "west", "down", "up", "left", "right", "back"],
    "verb": ["go", "stop", "kill", "eat"],
    "stop": ["the", "in", "from", "at", "it", "of"],
    "noun": ["door", "bear", "princess", "cabinet"]
  }

  pairs = {}
  for group, group_items in lexicon.items():
    for item in group_items:
      pairs.update({item: group})

  sentence = []

  for word in inputz.split():
    if word.lower() in pairs.keys():
      sentence.append((pairs[word.lower()], word))
    else:
      try:
        sentence.append(('number', int(word)))
      except ValueError:
        sentence.append(('error', word))

  return sentence


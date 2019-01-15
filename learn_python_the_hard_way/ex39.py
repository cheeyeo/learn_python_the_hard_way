# create mapping of states to abbreviation
states = {
 'Oregon': 'OR',
 'Florida': 'FL',
 'California': 'CA',
 'New York': 'NY',
 'Michigan': 'MI'
}

# creates a basic set of states and some cities
cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * len(cities))
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * len(states))
print("Michigan's abbrev: ", states['Michigan'])
print("Florida's abbrev: ", states['Florida'])

# use the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbrev
print('-' * len(states))
for state, abbrev in list(states.items()):
  print(f"{state} is abbreviated {abbrev}")

# print every city
print('-' * len(cities))
for abbrev, city in list(cities.items()):
  print(f"{abbrev} has city {city}")

# do both
print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has city {cities[abbrev]}")


print('-' * 10)
state = states.get('Texas')
if not state:
  print("Sorry, no Texas")


city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is {city}")

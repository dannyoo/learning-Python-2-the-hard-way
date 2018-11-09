# Create a mapping of state to abbreviations
states= {
    'Oregon' : 'OR',
    'Florida': 'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('_' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('_' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('--' * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every states abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print("%s is abbreviated %s" % (state, abbrev))
    
# print every city in states
print("-" * 10)
for abbrev, city in list(cities.items()):
    print("%s has the city %s" % (abbrev, city))


#now do both at the same time 
print("-" * 10)
for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has city {cities[abbrev]}")
print("Not PROBLEMATIC anymore")
    

print("*" * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
  print("Sorry, no Texas.")
print("*" * 10)
# get a city with a default value 

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

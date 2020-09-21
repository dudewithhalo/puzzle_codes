#ok this is the new file
#creates a mapping of state to abbreviation
states = {
    'Bihar' : 'BR',
    'Punjab' : 'PB', 
    'Jharkhand' : 'JH'
}

#creates a basic set of states and some cities in them
cities = {
    'BR' : 'Patna',
    'JH' : 'Bokaro',
}

# add some more cities

cities['BR'] = 'Hajipur'
cities['PB'] = 'Jalandhar'

#print out some cities

print('^-^' * 10)
print('BR state has : ', cities['BR'])
print('PB state has : ', cities['PB'])

#print some states

print('_' * 10),
print('Bihar abbreviation is : ', states['Bihar'])
print('Punjab abbreviation is : ', states['Punjab'])

#do it by using the state then cities dictionary

print('_' * 10)
print('Bihar has : ', cities[states['Bihar']])
print('Punjab has : ', cities[states['Punjab']])

#print every state abbreviation

print('_' * 10)
for state, abbrev in states.items():
    print('%s is abbreviated as %s' %(state, abbrev))
    
#print every city in state

print('_' * 10)
for abbrev,city in cities.items():
    print('%s has city %s' %(abbrev, city))
    
#now doing both at the same time

print('_' * 10)
for state, abbrev in states.items():
    print('%s state is abbreviated %s and has city %s' %(states, abbrev, cities[abbrev]))
    
print('_' * 10)
#safely get an abbreviation by state that might not be there

state = states.get('Darbhanga', None)

if not state:
    print('Sorry, not popular')

#get a city with a default value

city = cities.get('DR', 'does not Exist')
print ('The city for the state DR is : %s' %(city))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'
assert destination in destinationss, 'Sorry, Small World currently does not fly to this destination!'


# Write your code below: 

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)

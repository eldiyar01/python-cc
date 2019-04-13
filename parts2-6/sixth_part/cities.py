cities = {
'Moscow': {
'population': '2000000',
'fact': 'its capital',
'country': 'Russia',
},
'New-Yourk': {
'population': '4000000',
'fact': 'its not capital',
'country': 'USA',
}
}

for city in cities:
	print(city+':\n', cities[city])

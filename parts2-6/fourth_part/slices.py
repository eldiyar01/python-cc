my_foods = ['pizza', 'falafel', 'carrot cake','cannoli', 'ice cream']
print('The first three items in the list are: ' + str(my_foods[:3]))
print('Three items from the middle of the list are: ' + str(my_foods[1:4]) )
print('The last three items in the list are ' + str(my_foods[:-4]))
print('\n')
my_pizzas = ['pizza','pizza-2','pizza-3']
friend_pizzas = my_pizzas[:]
my_pizzas.append('pizza-4')
friend_pizzas.append('pizza-5')
print('My favorite pizzas are: ')
for pizza in my_pizzas:
	print(pizza)
print('\nfriend favorite pizzas are: ')
for pizza in friend_pizzas:
	print(pizza)

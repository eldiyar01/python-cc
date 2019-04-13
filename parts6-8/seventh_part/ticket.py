message = ('How old are u?: ')
while True :
	olds = int(input(message))
	if olds <= 3:
		print('free for u')
		break
	elif olds in range(3,13):
		print('12$')
		break
	elif olds > 12:
		print('15$')
		break

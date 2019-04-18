def album(name,album):
	music = {name: album}
	return music
while True:
	print("Please enter your album\nprint 'q' to quit\n ")
	enter_n = input('Enter names artist: ')
	if enter_n == 'q':
		break
	else:
		print()	
		enter_a = input('Enter names album: ')
		if enter_a == 'q':
			break
	
	full = album(enter_n, enter_a)
	print(full)	
	print()


		

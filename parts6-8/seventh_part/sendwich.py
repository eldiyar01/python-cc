sandwich = ['pastram','tuna','pastram','meat','vagetable','pastram']
finished=[]
while sandwich:
	if 'pastram' in sandwich:
		sandwich.remove('pastram') 
		print('we dont have pastram')	
	else:	
		made = sandwich.pop()
		(finished.append(made))
		print('I made you sandwich '+str(made))
print(finished)

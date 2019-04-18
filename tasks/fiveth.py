def find_digit (num, nth):
	abs(num)	
	if nth<0:
		print(-1) 
	else:
		a=str(num)
		b=str(nth)
		print(num // 10**nth % 10)
find_digit(42,5)

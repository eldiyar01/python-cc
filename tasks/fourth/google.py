a = input('write hello: ')
if a=='hello':
	first = print('1)google-kz')
	secnd = print('2)google-kg')
	third = print('3)google-ru')
	b = input('Choose filial: ')
	if b =='1)':
		with open("google_kz.txt", "a") as f:
			comp=input('write complaint: ')
			f.write('\n'+str(comp))
	if b =='2)':
		with open("google_kg.txt", "a") as f:		
			comp=input('write complaint: ')
			f.write('\n'+str(comp))			
	if b =='3)':
		with open("google_ru.txt", "a") as f:
			comp=input('write complaint: ')
			f.write('\n'+str(comp))		

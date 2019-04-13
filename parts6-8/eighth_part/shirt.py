def shirt(size,text):
	print('Size-'+str(size) ,'Text: '+text)
shirt(11, 'text')
shirt(text='read', size=21)


def make_shirt(size='L',text='I love python'):
	print('Size-'+str(size) ,'Text: '+text)

make_shirt()

make_shirt(text='read', size='S')

def music(artist, album, treck=''):
	mus={artist: album}
	if treck:
		mus['treck'] = treck
	return mus
print(music('Jack Starwberry', 'Pop food',11))
print(music('Jack Starwberry', 'buttercup'))
print(music('Jack Starwberry', 'dead weight'))

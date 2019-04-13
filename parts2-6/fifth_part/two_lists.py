current_users = ['Bloodseeker', 'Lina', 'CrystalMaiden', 'sven', 'morph']
new_users = ['monkeyking', 'pangolier', 'underlord', 'Sven','MORPh']

for user in current_users:
	if user.title() or user.lower() or user.upper() in new_users:
		print('user with '+ user +' name already exists')
	elif user.title() or user.lower() or user.upper() not in new_users:
		print ('you can use '+ user +' name')

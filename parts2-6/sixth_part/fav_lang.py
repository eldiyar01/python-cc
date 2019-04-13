favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'john': '',
'lil': ''
}
for lang in favorite_languages:
	if favorite_languages[lang] != '':
		print(lang+' thanks')
	else:
		print(lang + ' can you pass the poll?')

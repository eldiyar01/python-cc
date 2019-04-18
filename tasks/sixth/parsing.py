from bs4 import BeautifulSoup
import requests
import csv
import time


def get_html(url):
	req = requests.get(url)
	return req.text
	
def write_csv(data):
	with open('lalafo.csv','a') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'],data['price']))

def get_phone(html):
	soup = BeautifulSoup(html,'lxml')
	phones =soup.find('div', class_="list-view").find_all('div', class_='category-item') 
	for phone in phones:
		try:
			title = phone.find('div', class_='details').find('a', class_='name').text
			print(title)
		except:
			title=''
		try:
			price = phone.find('div',class_='details').find('div', class_='price').text
			print(price)
		except:
			price=''
		
		try:
			image = phone.find('div',class_='image').find('a', class_='image-holder').find('img').get('src')
			
		except:
			image=''
		data = {'title': title, 'price':price}
		write_csv(data)
		
def main():
	time.sleep(3600)
	url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary'
	html = get_html(url)
	get_phone(html)
	

while True:
	main()

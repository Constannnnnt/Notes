#!/usr/bin/env python3
'''
	This module prompts to crawl the url addresses of movies on douban.com
'''
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	'''This function crawls on douban.com'''
	page = 1
	while page <= max_pages:
		url = 'https://www.douban.com/tag/2015/movie=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")
		for link in soup.findAll('a', {'class': 'title'}):
			href = link.get('href')
			title = link.string
			title = title.encode("utf-8")
			textFile.write(title + '\t' +href)
		for link in soup.findAll('span', {'class': 'rating_nums'}):
			rating_num = link.string
			textFile.wirte(rating_num)
			textFile.write('\n')
		page += 1

if __name__ == '__main__':
	textFile = open("Douban_Movie.txt", "w") # pylint: disable=invalid-name
	textFile.write("Moive_name" + '\t' + "Web_Address" + '\t' + "rating_num")
	trade_spider(1)
	textFile.close()

import sys
import os
import requests
from bs4 import BeautifulSoup

def crawl(url='http://www.imdb.com', ll='7.5', ul='10.0'):
	os.system('clear')
	print('STARTING - ' + url)
	print('FINDING MOVIES RATED BETWEEN ' + ll + ' and ' + ul + '...')
	dictionary = {url: True}
	movies = []
	print()
	try:
		while len(movies) < 100:
			for k, v in dictionary.items():
				if v == True:
					url = k
					dictionary[k] = False
					break
			source = requests.get(url)
			soup = BeautifulSoup(source.text)
			links = soup.select('a[href^=/title/tt]')
			print(soup.title.string[:-7] + '  (' + str(len(movies)) + ' found)') 
			for link in links:
				newKey = 'http://www.imdb.com' + link.get('href')[:16]
				if newKey != url:
					if newKey not in dictionary:
						dictionary[newKey] = True
			content = soup.select('meta[property=og:type]')
			if len(content) > 0 and content[0]['content'] == 'video.movie':
				title = soup.select('meta[property=og:type]')
				rating = soup.select('span[itemprop=ratingValue]')
				if len(rating) > 0 and float(rating[0].string) >= float(ll) and float(rating[0].string) <= float(ul):	
					movies.append(soup.title.string[:-7])
		os.system('clear')
		print('ALL DONE !')
	except:
		os.system('clear')
		print('OH SNAP ! SOMETHING WENT WRONG...')
	finally:
		print()
		print(movies)
		print()
		
if __name__ == '__main__':
	crawl(*sys.argv[1:])
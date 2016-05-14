import re, urllib,csv
from bs4 import BeautifulSoup
def stock_groups():
	base_url = 'http://www.hisse.net/forum/'
	f = urllib.urlopen(base_url+'forum.php')
	text=f.read()
	soup=BeautifulSoup(text)
	stock_groups = {}
	for link in soup.find_all("a"):
		if link.text.isupper():
			hisse_url = re.search(r'[^&]+',link['href'])
			hisse_url = base_url+hisse_url.group(0)
			stock_groups[link.text]= hisse_url
	writer = csv.writer(open('C:/Users/ag2270/Dropbox/SerdarProje/data/stock_groups.csv','wb'))
	for key, value in stock_groups.items():
		try:
			writer.writerow([key,value])
		except UnicodeEncodeError:
			print key.encode('utf-8')	
def stock_links():
	f=open('C:/Users/ag2270/Dropbox/SerdarProje/data/stock_links.csv','wb')
	writer_first = csv.writer(f)
	stock_links = {}	
	with open('C:/Users/ag2270/Dropbox/SerdarProje/data/stock_groups_clean.csv', mode='r') as infile:
	    reader = csv.reader(infile)
	    with open('C:/Users/ag2270/Dropbox/SerdarProje/data/stock_groups_clean_new.csv', mode='w') as outfile:
	        writer = csv.writer(outfile)
	        stock_groups = {rows[0]:rows[1] for rows in reader}    	
	for key,value in stock_groups.items():
		f = urllib.urlopen(value)
		text=f.read()
		soup=BeautifulSoup(text)
		table = soup.find_all("a", {"class":"title"})
		for link in table:
			hisse_url = re.search(r'[^&]+',link['href'])
			hisse_url = 'http://www.hisse.net/forum/'+hisse_url.group(0)
			stock_links[link.text]=hisse_url
			#unicode olmayanlari yazamiyor
			try:
				writer_first.writerow([link.text[0:5],hisse_url])
			except UnicodeEncodeError:
				print link.text.encode('utf-8')
stock_links()


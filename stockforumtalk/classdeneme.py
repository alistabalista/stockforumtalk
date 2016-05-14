import re, urllib
from bs4 import BeautifulSoup
import 
class UrlOpener(object):
 	def __init__(self,name,stocks):
 		self.name = name
 		self.stocks = stocks

class HissenetOpener(UrlOpener):
	def __init__(self,stocks):
		UrlOpener.__init__(self,"hissenet",stocks)
	def get_stocks(self):
		return self.stocks
	def get_hisseurl(self):
		base_url = 'http://www.hisse.net/forum/'
		f = urllib.urlopen(base_url+'forum.php')
		text=f.read()
		soup=BeautifulSoup(text)
		#print soup.prettify("iso-8859-9")
		#kod biraz yavas calisyor bu looplari duzelmeye calis
		stock = self.stocks 
		for link in soup.find_all("a"):
			if stock in link.text:
				hisse_url = base_url+link.get("href")
				hisse_url = re.search(r'[^&]+',hisse_url)
				hisse_url = hisse_url.group(0)
				f = urllib.urlopen(hisse_url)
				text=f.read()
				inner_soup=BeautifulSoup(text)
				for inner_link in inner_soup.find_all("a", {"class":"title"}):
					if stock in inner_link.text:
						hisse_url = re.search(r'[^&]+',inner_link['href'])
						hisse_url = base_url+hisse_url.group(0)
						print(hisse_url)
	def is_stock_in(self):

		# for link in soup.find_all("a"):
		# 	if stock in link.text:
		# 		hisse_url = base_url+link.get("href")
		# 		hisse_url = re.search(r'[^&]+',hisse_url)
		# 		hisse_url = hisse_url.group(0)
		# 		f = urllib.urlopen(hisse_url)
		# 		text=f.read()
		# 		inner_soup=BeautifulSoup(text)
		# 		for inner_link in inner_soup.find_all("a", {"class":"title"}):
		# 			if stock in inner_link.text:
		# 				hisse_url = re.search(r'[^&]+',inner_link['href'])
		# 				hisse_url = base_url+hisse_url.group(0)
		# 				print(hisse_url)

#execution

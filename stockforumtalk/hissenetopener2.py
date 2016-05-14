import re, urllib
from bs4 import BeautifulSoup,SoupStrainer     
#soupstrainer ve requests kullanmaya bak
base_url = 'http://www.hisse.net/forum/'
f = urllib.urlopen(base_url+'forum.php')
text=f.read()
forum_id=''
soup=BeautifulSoup(text)
#print soup.prettify("iso-8859-9")
stock='DOCO'
for link in soup.find_all("a"):
	if stock in link.text:
		hisse_url = base_url+link.get("href")
		hisse_url = re.search(r'[^&]+',hisse_url)
		hisse_url = hisse_url.group(0)
		f = urllib.urlopen(hisse_url)
		text=f.read()
		inner_soup=BeautifulSoup(text)
		for inner_link in inner_soup.find_all("a"):
			if stock in inner_link.text:
				forum_id = inner_link.get("id") if inner_link.get("id") != None else "Empty"
				if 'thread_title' in forum_id:
					hisse_url = inner_link.get("href")
					hisse_url = re.search(r'[^&]+',hisse_url)
					hisse_url = base_url+hisse_url.group(0)
					print(hisse_url)
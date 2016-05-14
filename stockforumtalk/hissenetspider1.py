
import re, urllib,csv,datetime
from bs4 import BeautifulSoup
def date_seperator(date_str):
	#bu fonksiyon tam calismiyor daha.
	#date olayini nasil yapacagimiza bakalim.
	if date_str[0:3]==u'D\xfcn':
		date = datetime.date.today()-datetime.timedelta(days=1)
		date = datetime.mon
		date = str(date)+date_str[4:]
	elif date_str[0:5]==u'Bug\xfcn':
		date = datetime.date.today()
	else:
		date = date_str		
	return date

f = urllib.urlopen('http://www.hisse.net/forum/showthread.php?t=55810&page=116')
text=f.read()
text = text.decode('iso-8859-9')
soup=BeautifulSoup(text)
#bu postlarin icerigini almak icin
contents = soup.find_all( "blockquote", {"class":"postcontent restore"} )
counters = soup.find_all( "a", {"class":"postcounter"} )
dates = soup.find_all( "span", {"class":"date"} )
a = open('C:/Users/ag2270/Dropbox/SerdarProje/data/posts.csv','wb')
writer=csv.writer(a)
for content,counter,date in zip(contents,counters,dates):
	date=date_seperator(date.text)
	writer.writerow([content.text.encode('utf-8'),counter.text.encode('utf-8'),date.encode('utf-8')])
a.close()


#sonsayfayi almaca
# table = soup.find("span", {"class":"first_last"} )
# lastpage = re.findall(r'page=(\d+)',str(table))
# print lastpage[0]

# url ='http://www.hisse.net/forum/showthread.php?t=55810&page='+lastpage[0]
# print url
# f = urllib.urlopen(url)

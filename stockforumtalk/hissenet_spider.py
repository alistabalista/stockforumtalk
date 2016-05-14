class HissenetSpider:
	"""Hissenet Spider"""
	name = "hissnet"
	allowed_domains =["hisse.net"]
	start_urls = [
	"www.hisse.net/forum/forum.php"
	]

	def parse(self, response):
		filename = responese.url.split("/")[-2]
		open(filename,"wb").write(response.body)
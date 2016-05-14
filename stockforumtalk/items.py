from scrapy.item import Item, Field
class HissenetItem(Item):
	"""Hissenet icin scraper denemesi"""
	url=Field()
	name=Field()
	link=Field()
	
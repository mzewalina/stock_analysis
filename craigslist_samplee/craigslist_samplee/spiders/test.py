from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_samplee.items import CraigslistSampleeItem

class MySpider(BaseSpider):
	name="craig"
	allowed_domains= ["craigslist.org"]
	start_urls=["http://sfbay.craigslist.org/sfc/npo/"]
	
	def parse(self, response):
		hxs= HtmlXPathSelector(response)
		titles= hxs.select("//p")
		items=[]
		for titles in titles:
			item=CraislistsampleeItem()
			item['title']=titles.select("a/text()").extract()
			item['link']=titles.select("a/@href").extract()
			item.append(item)
		return items
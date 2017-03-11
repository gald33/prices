# -*- coding: utf-8 -*-
import scrapy


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ["file:///home/gal/prices/scrapedfiles/xml"]
    start_urls = ['file:///home/gal/prices/scrapedfiles/xml/1.xml']

    def parse(self, response):
        for item in response.xpath("//Item").extract():
	    	print 'ITEM:' + item + '\n'
	    	#print 'ITEM_SKU:' + item.xpath("//ItemCode") + '\n'
            #yield MyItem(title=url)

	
# -*- coding: utf-8 -*-
import scrapy


class TokensnifferSpider(scrapy.Spider):
	name = "tokensniffer"
	allowed_domains = ['https://url.publishedprices.co.il/']
	start_urls = ['https://url.publishedprices.co.il/login/user']

	def parse(self, response):
		for token in response.xpath("//input[@id[contains(.,'csrftoken')]]/@value").extract():
			csrftoken = token
			print 'CSRF VALUE:' + csrftoken + '\n'
			with open('csrftoken.txt', 'w') as f:
				f.write(csrftoken)

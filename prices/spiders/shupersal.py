'''# -*- coding: utf-8 -*-
import scrapy


class ShupersalSpider(scrapy.Spider):
    name = "shupersal"
    allowed_domains = ['http://www.ign.co.il/']
    start_urls = ['http://www.ign.co.il/']
    #allowed_domains = ['http://prices.shufersal.co.il//']
    #start_urls = ['http://prices.shufersal.co.il//']
#    rules = [
 #       Rule(LinkExtractor(allow='(http:\/\/prices.shufersal.co.il)'),follow=True,callback="parse")
  #  ]

    def parse(self, response):
        print "Gathering links from page " + str(response)
#        for link in response.xpath("//a[@href[contains(.,'page')]]/@href").extract():
 #           if link is not None:
  #              link = response.urljoin(link)
   #             print link
    #            yield scrapy.Request(link, callback=self.download_files)
        for link in response.xpath('//a/@href').extract():
            link = response.urljoin(link)
            print link
            yield scrapy.Request(link, callback=self.parse)
            
    def download_files(self, response):
        print "Downloading files from page " + str(response)
        for url in response.xpath("//a[@href[contains(.,'.gz')]]/@href").extract():
            yield {'file_urls':[url]}	
   		    #yield MyItem(title=url)
            #print 'FILE TO DOWNLOAD:' + url + '\n'
'''
import scrapy


class ShupersalSpider(scrapy.Spider):
    name = "shupersal"

    start_urls = ['http://prices.shufersal.co.il/']


    def parse(self, response):
        print "Gathering links from page " + str(response)
        for url in response.xpath("//a[@href[contains(.,'.gz')]]/@href").extract():
            print "Downloading files from page " + str(response)
            yield {'file_urls':[url]}
        # follow links to author pages
#        for href in response.css('.author + a::attr(href)').extract():
 #           yield scrapy.Request(response.urljoin(href),
  #                               callback=self.parse_author)

        # follow pagination links
        for link in response.xpath("//a[@href[contains(.,'page')]]/@href").extract():
            if link is not None:
                link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse)

#    def parse_author(self, response):
 #       print "P?A?SS"

# -*- coding: UTF-8 -*-
import scrapy
from scrapy.shell import inspect_response
from datetime import datetime
import pytz
import branches
import config
from pprint import pprint


class SupermarketSpider(scrapy.Spider):
    name = "supermarkets"

    start_urls = ['http://matrixcatalog.co.il/NBCompetitionRegulations.aspx', 'http://prices.shufersal.co.il/']
    time = config.time
    branches = branches.branch_list()

    def parse(self, response):
        # print "Gathering links from page " + str(response)
        # inspect_response(response, self)# -*- coding: UTF-8 -*-
        for url in response.xpath("//a[@href[contains(.,'PriceFull')]]/@href").extract():
            for branch in self.branches:
                if branch + self.time in url:
                    branches.branches_downloaded.append(branch)
                    url = response.urljoin(url)
                    # print "Downloading branch \"" +str(branch) + "\" from \"" + url + "\""
                    yield {'file_urls': [url]}
        for link in response.xpath("//a[@href[contains(.,'page')]]/@href").extract():
            if link is not None:
                link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse)

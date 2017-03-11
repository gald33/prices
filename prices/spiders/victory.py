
import scrapy
from scrapy.shell import inspect_response
from datetime import datetime
import pytz

class VictorySpider(scrapy.Spider):
    name = "victory"
    
    start_urls = ['http://matrixcatalog.co.il/NBCompetitionRegulations.aspx','http://prices.shufersal.co.il/']

    time = datetime.now(tz=pytz.timezone('Asia/Jerusalem')).strftime("%Y%m%d")
    branches = ("PriceFull7290696200003-063-","PriceFull7290027600007-033-")

    def parse(self, response):
        print "Gathering links from page " + str(response)
        #inspect_response(response, self)
        for url in response.xpath("//a[@href[contains(.,'PriceFull')]]/@href").extract():
            for branch in self.branches:
                if branch+self.time in url: 
                    url = response.urljoin(url)
                    print "Downloading branch \"" +str(branch) + "\" from \"" + url + "\""
                    yield {'file_urls':[url]}
        for link in response.xpath("//a[@href[contains(.,'page')]]/@href").extract():
            if link is not None:
                link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse)
               

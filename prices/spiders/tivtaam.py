# -*- coding: utf-8 -*-
import scrapy
import logging
import HTMLParser
from scrapy.shell import inspect_response
from scrapy.http import FormRequest
from scrapy.http.request import Request
import urllib
from scrapy.selector import Selector

class TivtaamSpider(scrapy.Spider):
    name = 'tivtaam'
    start_urls = ['https://url.publishedprices.co.il/']
    with open('csrftoken.txt', 'r') as f:
        csrftoken = f.read()

    def parse(self, response):
        # req =  scrapy.FormRequest.from_response(
        #     response,
        #     formdata={'username': 'john', 'password': 'secret'},
        #     callback=self.after_login
        # )
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'url.publishedprices.co.il',
        'Origin': 'https://url.publishedprices.co.il',
        'Referer': 'https://url.publishedprices.co.il/login',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'} # ,
        # 'Cookie': 'cftpSID=w7Ecwp/DtSfDlnA4w5/DgQrCvlTDtsKEwoRwSFvDiw=='}
        body = "csrftoken={token}&username=tivtaam&password=&Submit=Sign+in".format(token=urllib.quote_plus(self.csrftoken.strip()))
        # body="username=tivtaam&password=&Submit=Sign+in&csrftoken=KcKjZsO5Dw9gw7zDqB%2FDssKiw7vCvMOKf2vDqcOvNA%3D%3D"#"csrftoken=dsOVwqliFxvCtlViIQBVwqBJQkRbw4PDvDk%3D&username=tivtaam&password=&Submit=Sign+in"
        # print '''csrftoken=dsOVwqliFxvCtlViIQBVwqBJQkRbw4PDvDk%3D&username=tivtaam&password=&Submit=Sign+in'''
        # print self.csrftoken.strip()
        # print urllib.quote_plus(self.csrftoken.strip())
        #        'Content-Length': 94,
        req = Request(url='https://url.publishedprices.co.il/login/user',callback=self.after_login, headers=headers , body=body , method='POST')
        return req

    def after_login(self, response):
        inspect_response(response, self)
        print Selector(response=response).extract()
        print "GAL TEST (LEARN FOR NEXT TIME!!)"
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return
        for url in response.xpath("//a[@href[contains(.,'.gz')]]/@href").extract():
	        #yield MyItem(title=url)
		    print 'FILE TO DOWNLOAD:' + url + '\n'
		    d = {'file_urls':[url]}
		    yield d	


# class TivtaamSpider(scrapy.Spider):
#     logging.getLogger('scrapy').setLevel(logging.WARNING)
#     name = "tivtaam"
#     allowed_domains = ['https://url.publishedprices.co.il/']
#     start_urls = ['https://url.publishedprices.co.il/login/']
#     with open('csrftoken.txt', 'r') as f:
#         csrftoken = f.read()
#         print 'CSRFTOKEN READ:' + csrftoken
#         user_agent = ('Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) '
#         'AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 '
#         'Mobile/9A334 Safari/7534.48.3')



        # def parse2(self, response):
        #     print "HELLO"
        #     return scrapy.FormRequest.from_response(
        #     response,
        #     formdata={'username': 'TivTaam'},
        #     callback=self.after_login
        #     )


        # def after_login(self, response):
        #     print "HELLO_HERE"
        #     inspect_response(response, self)
        # check login succeed before going on
        # if "authentication failed" in response.body:
        #     self.logger.error("Login failed")
        #     print '\n\nAUTHENTICATION FAILED\n\n'
        #     return
        #
        #     print '\n\nAUTHENTICATION SUCCESSFUL\n\n'
        #
        #     # continue scraping with authenticated session...
        #     for url in response.xpath("//a[@href[contains(.,'.gz')]]/@href").extract():
        #         #yield MyItem(title=url)
        #         print 'FILE TO DOWNLOAD:' + url + '\n'
        #         d = {'file_urls':[url]}
        #         yield d

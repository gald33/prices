# downloads files, fixes names and then decompress. The compressed files are kept in the 'renamed' folder and marked as 'extract-' in the file name. The output xml files are in the 'xml' folder.

import scrapy
from datetime import datetime
import os
import gzip
from subprocess import call
import xml.etree.ElementTree as ET
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import config
import argparse
import branches


update_log_filename = "update_prices.log"


def update_log(text):
    with open(update_log_filename, "w") as f:
        f.write(text)

# setting arguments
'''
parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store', dest='date',
                    help='selects files date to download and process, e.g. 20161022')
results = parser.parse_args()
if results.date is not None:
	custom_time = int(results.date)
else:
	custom_time = None
config.time = custom_time
'''

# item of a price list, relevent if date is highest but no later than shopping date
'''class Price_rec(scrapy.Item):
	sku = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)'''


def crawl_sites():
    print "Downloading files..."
    process = CrawlerProcess(get_project_settings())
    process.crawl('supermarkets')
    process.start()
    update_log(branches.info())



def rename_files():
    path = config.home_dir + "/scrapedfiles/full/"
    renamed_path = config.home_dir + "/scrapedfiles/renamed/"
    for filename in os.listdir(path):
        if not filename.endswith('.gz'):
            os.rename(path + filename, renamed_path + filename + '.gz')
        else:
            os.rename(path + filename, renamed_path + filename)


def decompress_files_mark():
    print "Decompressing..."
    mark = 'extracted-'  # mark extracted files
    path = config.home_dir + "/scrapedfiles/renamed/"
    xml_path = config.home_dir + "/scrapedfiles/xml/"
    for filename in os.listdir(path):
        if filename.endswith('.gz'):
            if not filename.startswith(mark):
                # command = "gzip -d " + path + " " + filename
                # print command
                # os.system(command)
                # call(command, shell=True)

                # decompress
                out_filename = filename + '.xml'
                in_file = gzip.open(path + filename, 'rb')
                out_file = open(path + out_filename, 'wb')
                out_file.write(in_file.read())
                in_file.close()
                out_file.close()
                # move decompressed file to xml folder
                os.rename(path + out_filename, xml_path + out_filename)
                # mark compressed file so they won't be re-decompressed
                os.rename(path + filename, path + mark + filename)
                
                
def decompress_files():
    print "Decompressing..."
    path = config.home_dir + "/scrapedfiles/renamed/"
    xml_path = config.home_dir + "/scrapedfiles/xml/"
    for filename in os.listdir(path):
        if filename.endswith('.gz'):
            out_filename = filename + '.xml'
            in_file = gzip.open(path + filename, 'rb')
            out_file = open(path + out_filename, 'wb')
            out_file.write(in_file.read())
            in_file.close()
            out_file.close()
            # move decompressed file to xml folder
            os.rename(path + out_filename, xml_path + out_filename)
            os.remove(path + filename)


def rename_xml():
    print "Renaming..."
    time = config.time
    path = config.home_dir + "/scrapedfiles/xml/"
    renamed_path = config.home_dir + "/scrapedfiles/xml_renamed/"
    for filename in os.listdir(path):
        et = ET.parse(path + filename)
        root = et.getroot()
        if root.find('ChainId') == None:
            # print "not shupersal"
            chain_id = root.find('ChainID').text
            sub_chain = root.find('SubChainID').text
            store_id = root.find('StoreID').text
        else:
            chain_id = root.find('ChainId').text
            sub_chain = root.find('SubChainId').text
            store_id = root.find('StoreId').text
        # print "Time: " +str(time)
        # print "chain_id",chain_id
        # print "store_id",store_id
        # print "sub_chain", sub_chain

        os.rename(path + filename,
                  renamed_path + "prices-" + chain_id + "-" + sub_chain + "-" + store_id + "-" + time + ".xml")


def main():
    update_log("Script running @ " + config.time)
    crawl_sites()
    rename_files()
    decompress_files()
    rename_xml()
    print "Done"
    update_log("Script is done")


if __name__ == "__main__":
    main()

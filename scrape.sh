#!/bin/bash
# enter crapy environment and scrape
echo Running scrape.sh >> ~/prices/update_prices.log
date | cat >> ~/prices/update_prices.log
echo scrape
source ~/scrapyenv/bin/activate
cd ~/prices
python update_prices.py
deactivate
echo create csv
python xml_to_csv.py -e /home/gal/scrapedfiles/xml_renamed/ -d /home/gal/scrapedfiles/csv/
echo create categoriess
python create_categories.py
echo add categories
python add_categories.py

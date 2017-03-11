import os
from subprocess import call

command = 'scrapy crawl shupersal'
call(command, shell=True)

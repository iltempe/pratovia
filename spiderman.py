# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#scraping of ordinanze trasporti comune di Prato

import csv
from lxml import html
import requests

#anno
anno='2017'

page = requests.get('http://www.comune.prato.it/servizicomunali/ordinanze/trasporti/archivio/' + anno + '/')
tree = html.fromstring(page.content)

num_list=tree.xpath('//*[@id="main"]/div[2]/strong[3]/text()')
num_string = ''.join(num_list)

page = requests.get('http://www.comune.prato.it/servizicomunali/ordinanze/trasporti/archivio/' + anno + '/?limit=' + num_string)
tree = html.fromstring(page.content)

#scraping all data of the year
stato=tree.xpath('//*[@id="main"]/table/tbody/tr/td[1]/img/@title')
quando=tree.xpath('//*[@id="main"]/table/tbody/tr/td[2]/text()')
num=tree.xpath('//*[@id="main"]/table/tbody/tr/td[3]/text()')
tipo=tree.xpath('//*[@id="main"]/table/tbody/tr/td[4]/text()')
dove=tree.xpath('//*[@id="main"]/table/tbody/tr/td[5]/img/@title')
perche=tree.xpath('//*[@id="main"]/table/tbody/tr/td[6]/img/@title')
oggetto = tree.xpath('//*[@id="main"]/table/tbody/tr/td[7]/a/text()')
link = tree.xpath('//*[@id="main"]/table/tbody/tr/td[7]/a/@href')

#print(oggetto)
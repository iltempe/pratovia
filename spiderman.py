# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#scraping of ordinanze trasporti comune di Prato
import csv
from lxml import html
import requests
from BeautifulSoup import BeautifulSoup
import urllib

#scrive un dataset per l'anno e i dati di cui si è fatto lo scraper
def write_dataset(anno,header,rows):
    with open("dati_mobilità_" + anno + ".csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
    return

#i dettagli dell'ordinanza necessitano di uno scrape con BeautifulSoup
def scrape_ordinanza_details(link,anno):

    return

#anni da estrarre
year=['2017']
separator = "-"

for anno in year:
    dove_all=[]
    page = requests.get('http://www.comune.prato.it/servizicomunali/ordinanze/trasporti/archivio/' + anno + '/')
    tree = html.fromstring(page.content)

    #trovo il numero di delibere
    num_list=tree.xpath('//*[@id="main"]/div[2]/strong[3]/text()')
    num_string = ''.join(num_list)

    #leggo l'html
    page = requests.get('http://www.comune.prato.it/servizicomunali/ordinanze/trasporti/archivio/' + anno + '/?limit=' + num_string)
    #page = requests.get('http://www.comune.prato.it/servizicomunali/ordinanze/trasporti/archivio/' + anno + '/?limit=1')
    tree = html.fromstring(page.content)

    #intervallo righe
    interval=range(1,int(num_string)+1)

    #scraping all data of the year
    stato=tree.xpath('//*[@id="main"]/table/tbody/tr/td[1]/img/@title')
    quando=tree.xpath('//*[@id="main"]/table/tbody/tr/td[2]/text()')
    num=tree.xpath('//*[@id="main"]/table/tbody/tr/td[3]/text()')
    tipo=tree.xpath('//*[@id="main"]/table/tbody/tr/td[4]/text()')
    for i in interval:
        dove=tree.xpath('//*[@id="main"]/table/tbody/tr[' + str(i) + ']/td[5]/img/@alt')
        dove_all.append(separator.join(dove))
    perche=tree.xpath('//*[@id="main"]/table/tbody/tr/td[6]/img/@title')
    oggetto = tree.xpath('//*[@id="main"]/table/tbody/tr/td[7]/a/text()')

    #trasformare ../../archivio/2017/htm/3024.htm in http://www.comune.prato.it/servizicomunali/ordinanze/trasporti/archivio/2017/htm/3024.htm
    link = tree.xpath('//*[@id="main"]/table/tbody/tr/td[7]/a/@href')
    link = [s.replace('../..', 'http://www.comune.prato.it/servizicomunali/ordinanze/trasporti') for s in link]

    #pippo=[scrape_ordinanza_details(s,anno) for s in link]

    print(anno + " data extracted...")

    #scrivi file csv
    header=['stato','data','numero','tipo','luogo','perchè','oggetto','link']
    rows = zip(stato,quando,num,tipo,dove_all,perche,oggetto,link)
    write_dataset(anno, header, rows)
    print(anno + " data written...")


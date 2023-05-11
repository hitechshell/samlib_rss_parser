import requests
from datetime import datetime

def link_by_date(date):
    link = 'http://samlib.ru/logs/'
    link += str(date.year) + '/' + str(date.month).zfill(2) + '-' + str(date.day).zfill(2) + '.log'
    return link

def get_page(link):
    req = requests.get(link)
    return req.content.decode('cp1251')

def get_raw_news(date):
    """
    имя файла|тег oперации|таймштамп-MySQL|title|author|type|janr|annot|date|img_cnt|update-unixtime|size kb
    """
    return get_page(link_by_date(date))

#!/usr/bin/python3
import sys

from gen_rss import gen
from datetime import datetime
from parse_data import get_all_new

conf_dir = '/home/denis'

if len(sys.argv) > 1:
    conf_dir = sys.argv[1]

news = get_all_new(conf_dir + '/last_update.txt')

authors = [] # подписка на авторов
texts = [] # подписка на конкретные тексты

try:
    with open(conf_dir + '/authors.txt', 'r') as f:
      authors += f.read().split()
except:
    pass
try:
    with open(conf_dir + '/texts.txt', 'r') as f:
      texts += f.read().split()
except:
    pass

elems = []
for el in news:
    if el['file'].split('/')[2] in authors or el['file'].split('/') in texts:
        elems.append({
            'title': el['do'] + ' ' + el['title'],
            'link': 'http://samlib.ru' + el['file'] + '.shtml',
            'author': el['author'],
            'description': el['annot'],
            'time': el['timestamp']
        })

"""
elems = [
        {
            'title': 'test',
            'link': 'https://example.com/1234',
            'author': 'Некий Автор',
            'description': 'проверка связи',
            'time': datetime.now(),
        },
        {
            'title': 'example',
            'link': 'https://example.com/123456',
            'author': 'Некий Автор',
            'description': 'проверка связи дубль2',
            'time': datetime(2005, 3, 4),
        },
    ]
"""
gen(elems)

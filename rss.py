#!/usr/bin/python3
import datetime
import time

def pubDate(date_obj):
    #pubdate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    pubdate = date_obj.strftime("%a, %d %b %Y %H:%M:%S +0000")
    return pubdate


begin ='''
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
  <channel>
    <link>http://samlib.ru/</link>
    <language>ru</language>
    <title>Samlib notifications</title>
    <description>Обновления самиздата</description>
    <pubDate>{date}</pubDate>
'''

item_template = '''
<item>
    <author>{author}</author>
    <link>{link}</link>
    <guid>{link}</guid>
    <title>{title}</title>
    <pubDate>{date}</pubDate>
    <description>
        <![CDATA[{description}]]>
    </description>
</item>
'''

end = '''
    </channel>
</rss>
'''

elems = [
    {
        'title': 'test',
        'link': 'https://example.com/1234',
        'author': 'Некий Автор',
        'description': 'проверка связи',
        'time': datetime.datetime.now(),
    },
    {
        'title': 'example',
        'link': 'https://example.com/123456',
        'author': 'Некий Автор',
        'description': 'проверка связи дубль2',
        'time': datetime.datetime(2005, 3, 4),
    },
]

now = datetime.datetime.now()
print(begin.format(date=pubDate(now)))

for elem in elems:
    item_time = elem['time']
    item = item_template.format(
        title=elem['title'],
        author=elem['author'],
        description=elem['description'],
        date=pubDate(item_time),
        link=elem['link']
    )
    print(item)

print(end)

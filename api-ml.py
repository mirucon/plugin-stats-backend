import requests
import json
import re

url_base = 'https://wordpress.org/plugins'
posts = []
requires = []
tested = []
requires_php = []

per_page = 100

r = requests.get(url_base + '/wp-json/wp/v2/posts/?per_page=' + str(per_page))
total_pages = int(r.headers['x-wp-totalpages'])
total_pages += 1

def validation (val):
    if re.search(r"\d", val):
        o = re.search(r"\d(.\d)?(.\d)?", val)
        o = o.group()

        if re.fullmatch(r"\d", o):
            o = o + '.0'

        if re.fullmatch(r"\d.\d.\d", o):
            o = re.search(r"\d.\d", o)
            o = o.group()

        return (o)

    else: 
        return False

for i in range(1, total_pages):
    url = url_base + '/wp-json/wp/v2/posts/?per_page=' + str(per_page) + '&page=' + str(i)
    r = requests.get(url)
    data = r.json()
    posts.append(data)

for post in posts:
    for li in post:
        di = dict(li)
        
        req = validation(di['meta']['requires'])
        tes = validation(di['meta']['tested'])
        php = validation(di['meta']['requires_php'])

        if req:
            requires.append(req)

        if tes:
            tested.append(tes)

        if php:
            requires_php.append(php)

with open('json/requires.json', 'w') as fp:
    json.dump(requires, fp)

with open('json/tested.json', 'w') as fp:
    json.dump(tested, fp)

with open('json/requires_php.json', 'w') as fp:
    json.dump(requires_php, fp)

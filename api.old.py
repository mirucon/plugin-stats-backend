import requests
import json

url_base = 'https://wordpress.org/plugins'
posts = []
plugins = {}

per_page = 100

r = requests.get(url_base + '/wp-json/wp/v2/posts/?per_page=' + str(per_page))
total_pages = int(r.headers['x-wp-totalpages'])
total_pages += 1

for i in range(1, total_pages):
    url = url_base + '/wp-json/wp/v2/posts/?per_page=' + str(per_page) + '&page=' + str(i)
    r = requests.get(url)
    data = r.json()
    posts.append(data)

for post in posts:
    for li in post:
        di = dict(li)
        m = {}
        m['requires'] = di['meta']['requires']
        m['tested'] = di['meta']['tested']
        m['requires_php'] = di['meta']['requires_php']
        o = { di['title']['rendered']: m}
        plugins.update(o)

with open('result.json', 'w') as fp:
    json.dump(plugins, fp)
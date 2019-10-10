from urllib.request import Request, urlopen
from lxml import html
import json, pickle


url = 'https://classes.berkeley.edu/search/class?f%5B0%5D=im_field_term_name%3A851&page={}'

pages = range(0, 373)

all_classes = []

for i in pages:
    print('Page:', i)
    req = Request(url.format(i), headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(req)
    webcontent = response.read()

    f = open('parser-' + str(i) + '.html', 'wb')
    f.write(webcontent)

    tree = html.fromstring(webcontent)

    classes = tree.xpath('//div[@class="handlebarData theme_is_whitehot"]')

    for c in classes:
        cj = json.loads(c.attrib['data-json'])
        all_classes.append(cj)

pickle.dump(all_classes, open('output.pickle', 'w'))

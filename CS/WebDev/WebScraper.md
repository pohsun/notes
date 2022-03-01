#CS/WebDev #CS/ProgLang/Python 

| Category | Description | Packages |
| :---- | :---- | :---- |
| Scraper | Get the response of target webpage. |`request`(static),  `splash`(dynamic), `selenium`(dynamic)|
| Parser | Parse `html`, `xml` into useful information. | `bs4`(slow),`lxml`(fast), `pyquery`(fast) |
| Framework | Scraper + Parser | `scrapy` |

# Scrapers

## [`request`](https://requests.readthedocs.io/en/master/)

```python
import requests

def main():
    for i in range(100):
        rsp = requests.get(f"http://www.example.com/{i}.html")
        with open("example-{i}.txt", "w") as f:
            f.write(rsp.text)
```

### `asyncio` + `requests`
keywords: `grequests`, `aiohttp`

## [`splash`](https://splash.readthedocs.io/en/stable/index.html)

* [中文手冊](https://splash-cn-doc.readthedocs.io/zh_CN/latest/index.html)

## [`selenium`](https://selenium-python.readthedocs.io/)(Not recommanded)

* Useful, but it's slow and memory-consuming. 



## Anti-spider solutions

* https://www.learncodewithmike.com/2020/09/7-tips-to-avoid-getting-blocked-while-scraping.html

### Anti-anti-spider

# Parsers

## [`lxml`](https://lxml.de/index.html#documentation)

### Tutorial

[Official tutorial](https://lxml.de/tutorial.html) is fairly clear and complete. A minimal example is provided below.

```python

import requests
from lxml import html
    
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

# You could check XPath subsection
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')

print('Buyers: ', buyers)
print('Prices: ', prices)    
```

Typical output    

```
Buyers:  ['Carson Busses', 'Earl E. Byrd', 'Patty Cakes', 'Derri Anne Connecticut', 'Moe Dess', 'Leda Doggslife', 'Dan Druff', 'Al Fresco', 'Ido Hoe', 'Howie Kisses', 'Len Lease', 'Phil Meup', 'Ira Pent', 'Ben D. Rules', 'Ave Sectomy', 'Gary Shattire', 'Bobbi Soks', 'Sheila Takya', 'Rose Tattoo', 'Moe Tell']
Prices:  ['$29.95', '$8.37', '$15.26', '$19.25', '$19.25', '$13.99', '$31.57', '$8.49', '$14.47', '$15.86', '$11.11', '$15.98', '$16.27', '$7.50', '$50.85', '$14.26', '$5.68', '$15.00', '$114.07', '$10.09']
```

### [XPath](https://zh.wikipedia.org/wiki/XPath)

* Learn from [examples](http://www.zvon.org/xxl/XPathTutorial/General/examples.html).
* [XPath cheatsheet](https://devhints.io/xpath)
* [XPath testbed](http://www.whitebeam.org/library/guide/TechNotes/xpathtestbed.rhtm)

## [`Beautifulsoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* Parsers

|Parser|Typical usage|Comments|
|----|----|----|
|`html.parser`|`BeautifulSoup(markup, "html.parser")`| Slow |
|`lxml`|`BeautifulSoup(markup, "lxml")`|Very fast.|
|`lxml-xml`| `BeautifulSoup(markup, "lxml-xml")`</br> `BeautifulSoup(markup, "xml")`| The only `xml` parser.|
|`html5lib`|`BeautifulSoup(markup, "html5lib")`|Very slow|

* Way slower with Python

    With [`MercuryRising/parserComparison.py`](https://gist.github.com/MercuryRising/4061368), the performance of each parser could be tested. Even with the `lxml` parser in `bs4`, the performance is still way slower. 
    
```
==== Python version: 3.8.5 (default, Jul 21 2020, 10:48:26)
[Clang 11.0.3 (clang-1103.0.32.62)] =====

==== Total trials: 10000 =====
bs4 total time: 4.7
pq total time: 0.7
lxml (cssselect) total time: 0.7
lxml (xpath) total time: 0.5
regex total time: 1.0 (doesn't find all p)
```

# Framework `scrapy` (Not recommanded)

* [Official Manual](https://docs.scrapy.org/en/latest/)
* [Official tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
* [為什麼不建議使用scrapy，而是從頭開始編寫爬蟲系統？](https://www.zhihu.com/question/293589348/answer/782851279)
    * 不會帶來語法簡化/易讀的優勢
    * 異步結構帶來的高性能和程式碼結構對反爬蟲沒什麼鳥用
        * How about `splash`

## Tutorial

Start a project with `scrapy startproject project_root`, then following hierarchy is created automatically.
```
project_root/
    scrapy.cfg            # deploy configuration file
    project_root/         # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

As a framework, `scrapy` crawls a bunch of webpages with more-or-less shared configuration. The configuration for each page are defined in `project_root/project_root/spiders`.

----

An example configuration is provided below...
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

* attributes/method are necessary to be defined for `scrapy.Spider`:
    * `name`: a **unique name** identifies the Spider
    * `start_request(self)`: must return an *iterable* of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests.
    * `parse(self, response)`: a method that will be called to handle the response downloaded for each of the requests made. The `response` parameter is an instance of `TextResponse` that holds the page content.
        * This is the place where other parser could jump in.
* Launched by `scrapy crawl "quotes"` under `project_root`.
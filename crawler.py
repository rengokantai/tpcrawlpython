__author__ = 'Hernan Y.Ke'
from lxml import html
import requests



class Crawler:
    def __init__(self, start_url,depth):
        self.start_url =start_url
        self.depth = depth
        self.apps = []


    def crawl(self):
        self.get_app_from_link(self.start_url)
        return

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
        developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
        price = tree.xpath('//div[@itemprop="price"]/text()')[0]
        links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')

        app = App(name,developer, price, link)

        self.apps.append(app)

        for link in links:
            print (link)


        print (name)
        return
class App:
    def __init__(self, name,developer, price, link):
        self.name = name
        self.developer = developer
        self.price = price
        self.link = link

    def __str__(self):
        return "name: " + self.name



c = Crawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731', 0)

c.crawl()

for app in c.apps:
    print(app)
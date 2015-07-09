__author__ = 'Hernan Y.Ke'
from lxml import html
import requests



class Crawler:
    def __init__(self, start_url,depth):
        self.start_url =start_url
        self.depth = depth
        self.apps = []
        self.current_depth = 0
        self.depth_links = []


    def crawl(self):
        app=self.get_app_from_link(self.start_url)
        self.apps.append(app)
        self.depth_links.append(app.links)

        while self.current_depth < self.depth:
            current_links =[]
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_from_link(link)
                current_links.extend(current_links)
                self.apps.append(app)
            self.current_depth+=1
            self.depth_links.append(current_links)
        return

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
        developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
        price = tree.xpath('//div[@itemprop="price"]/text()')[0]
        links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')

        app = App(name,developer, price, links)

        self.apps.append(app)
        self.depth_links.append(app.links)

        for link in links:
            print (link)


        print (name)
        return app
class App:
    def __init__(self, name,developer, price, links):
        self.name = name
        self.developer = developer
        self.price = price
        self.links = links

    def __str__(self):
        return "name: " + self.name



c = Crawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731', 0)

c.crawl()

for app in c.apps:
    print(app)
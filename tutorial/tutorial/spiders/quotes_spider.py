import scrapy
from tutorial.items import TutorialItem

class PcsSpider(scrapy.Spider):
    name = "pcsrace"
    start_urls = [
        'https://www.procyclingstats.com/races.php?year=2017&circuit=1&class=&filter=Filter',
        'https://www.procyclingstats.com/races.php?year=2018&circuit=1&class=&filter=Filter'
    ]

    def parse(self, response):
        for race in response.css('tbody tr'):
            item = TutorialItem() 
            item['raceName'] = race.css("td a::text").get()
            item['raceDate'] = race.css("td::text")[0].get()
            item['racePageLink'] = race.css("td a::attr(href)").re(r'race.+')[0]
            item['flag'] = race.css("td span::attr(class)").get()
            item['raceClass'] = race.css("td::text")[2].get()
            item['raceWinner'] = race.css("td.cu500 a::text").get()
            item['raceWinnerLink'] = race.css("td.cu500 a::attr(href)")[0].get()
            yield item
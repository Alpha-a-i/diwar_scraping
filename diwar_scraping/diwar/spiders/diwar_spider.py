import scrapy
import time
class DivarSpider(scrapy.Spider):
    name = 'diwar'

    def start_requests(self):
        with open('tokens.txt', 'r', encoding='utf-8') as f:
            tokens = f.read().strip().split(',')
        for token in tokens:
            url = f'https://divar.ir/v/-/{token.strip()}'
            yield scrapy.Request(url, callback=self.parse)
            time.sleep(30)

    def parse(self, response):
        area = response.xpath('//table[contains(@class, "kt-group-row")]//tr[@class="kt-group-row__data-row"]/td[1]/text()').get()

        if area:
            area = area.strip().replace('٬', '')  
            try:
                area = int(area)
            except ValueError:
                area = None

        yield {
            'Area': area
        }

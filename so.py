import scrapy
import  csv_excel_reader as cer


base_url = 'https://stackoverflow.com/questions/tagged/{}'
class SoSpider(scrapy.Spider):
    name = 'so'
    
    def start_requests(self):
        # tags = cer.get_list_from_csv('so_tags.csv',1,ignore_header=True)
        # tags = cer.get_list_from_csv_pd('so_tags.csv',column_index=1,ignore_header=True)
        # tags = cer.get_list_from_excel('so_tags.csv',1,ignore_header=True)
        tags = cer.get_list_from_excel_pd('so_tags.csv',column_index=1,ignore_header=True)
        for tag in tags:
            yield scrapy.Request(base_url.format(tag))

    def parse(self, response):
        questions = response.xpath('normalize-space(//*[@id="mainbar"]/div[4]/div/div[1]/text())').get()
        questions = questions.strip('questions').strip()

        yield {
            'questions': questions,
            'url': response.url
        }

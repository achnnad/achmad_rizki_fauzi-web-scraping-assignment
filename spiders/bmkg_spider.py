from pathlib import Path

import scrapy


class BmkgSpider(scrapy.Spider):
    name = "bmkg_jakpus"

    def start_requests(self):
        urls = [
            "https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?kab=Jakarta&Prov=DKI_Jakarta&AreaID=501195"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        # get all date 
        list_dates = response.css("ul.nav.nav-tabs").css("li a::text").getall()
        for i, date in enumerate(list_dates):  
            tab_position = 'div#TabPaneCuaca' + str(i+1)
            # get all data per tab
            weather_data = response.css(tab_position).css("div.cuaca-flex-child")
            for weather in weather_data:
                yield {
                    'Tanggal': date, 
                    'Waktu Perkiraan': weather.css("h2.kota::text").get(),
                    'Kondisi Cuaca': weather.css("div.kiri p::text").get(),
                    'Suhu': weather.css("h2.heading-md::text").get(),
                    'Intensitas Hujan': weather.css("div.kanan p::text").getall()[0],
                    'Kecepatan dan Arah Angin': weather.css("div.kanan p::text").getall()[1]
                }
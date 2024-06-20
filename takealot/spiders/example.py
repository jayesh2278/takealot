import scrapy
import pandas as pd
import json

class ExampleSpider(scrapy.Spider):
    name = "takealot"
    start_urls = ["https://www.takealot.com/"]

    def parse(self, response):

        df = pd.read_csv("South.csv")
        column_data = df["Product"]

        for i in column_data:
            url = f"https://api.takealot.com/rest/v-1-10-0/searches/products,filters,facets,sort_options,breadcrumbs,slots_audience,context,seo?dex=CDU2Ef2nzBfNHRBXrnrjzg&r=1&sb=1&si=57db9bffdd956c16386cc65975ce0d53&qsearch={i}&searchbox=true"
            headers = {
                'authority': 'api.takealot.com',
                'accept': '*/*',
                'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,gu;q=0.7',
                'cache-control': 'max-age=0',
                'dnt': '1',
                'origin': 'https://www.takealot.com',
                'referer': 'https://www.takealot.com/',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'Cookie': '__cf_bm=ywnn0PD0asLa20u0lGa2_jHhbdGGOYnMsRGtnKKropU-1685767917-0-AenV4b8nBznVsAQtTBATfn2yop/liNo2ASv7KqYl94cijHUjVeEstvSmvA26B1VC1Ze42CIrbqEBIllm/QcVpeo='
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse_results)

    def parse_results(self, response):
        data = json.loads(response.text)
        result = data["sections"]["products"]["results"][0]["product_views"]["buybox_summary"]["pretty_price"]
        yield {
            "price":result
        }







import scrapy

class DocSpider(scrapy.Spider):
    name = "AndroDoc"
    allowed_domains = ["developer.android.com"]
    start_urls = [
        "https://developer.android.com/reference/android/content/pm/PackageManager",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
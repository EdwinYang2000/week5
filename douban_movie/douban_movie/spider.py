import csv

import asyncio

import aiohttp

import async_timeout

from scrapy.http import HtmlResponse

results = []

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

def parse(url, body):
    response = HtmlResponse(url=url, body=body)
    print (response)

    for repository in response.css('li.public'):
        name = repository.xpath('//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)")
        datetime = repository.xpath('//relative-time/@datetime').extract_first()
        result = (name, datetime)
        print (result)
        results.append(result)


async def task(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)
        parse(url,html.encode('utf-8'))

def main():
    loop = asyncio.get_event_loop()
    url_template = 'https://github.com/shiyanlou?page={}&tab=reponsitories'
    tasks = [task(url_template.format(i)) for i in range(1,5)]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(results)

if __name__ == '__main__':
    main()

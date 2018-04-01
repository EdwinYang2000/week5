import json

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results = []

def parse(response):
    for comment in response.css('div.comment-list-item'):
        result = {'username': comment.xpath('//div[@class="user-username"]/a/text()').extract(),
        'content': comment.xpath('//div[@class="comment-item-content"]/p/text()').extract()}
        results.append(result)


print (results)

def has_next_page(response):
    next_page = response.css('div.pagination-container ul li.disabled').extract_first(default='nextpage')
    print (next_page)

def goto_next_page(driver):
    pass
    element = driver.find_element_by_class('next-page').click()

def wait_page_return(driver, page):
    WebDriverWait(driver, 10).until(
            EC.text_to_be_present_int_element(
                (BY.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
                str(page)
                )
            )

def spider():
    driver = webdriver.PHantomJS()
    url = 'http://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1
    while True:
        wait_page_return(driver, page)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        parse(response)
        if not has_next_page(response):
            break
        page += 1
        goto_next_page(driver)
    with open('/home/shiyanlou/comments.json','w') as f:
        f.write(json.dumps(results))

if __name__ == '__main__':
    spider()

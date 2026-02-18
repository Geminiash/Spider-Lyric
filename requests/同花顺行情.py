import requests
from lxml import etree
import pandas as pd
import time,random

headers = {
    
}

url = "https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/"
response = requests.get(url, headers=headers)

data_list = []

html = etree.HTML(response.text)

review_items = html.xpath("//table[@class='m-table m-pager-table']/tbody/tr")

for item in review_items:
    # 序号
    item_math = item.xpath('.//td[1]/text()')[0]
    # 代码
    item_code = item.xpath('.//td[2]/a/text()')[0]

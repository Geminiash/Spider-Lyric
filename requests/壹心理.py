import requests
from lxml import etree
import pandas as pd
import time,random

cookies = {
    
}

headers = {
                        
}

params = {
    'page': '1',
    'type': 'question',
    'object_name': 'last',
    'title': '',
    'level2_tag': '0',
    'sort': 'id',
    'from': 'houye-dh',
}



data_list = []

for page in range(1,10):

    print('第  ', page, '   页采集成功')
    params['page'] = page
    response = requests.get('https://www.xinli001.com/qa', params=params, cookies=cookies, headers=headers)

    html = etree.HTML(response.text)

    review_items = html.xpath('//ul[@class="content"]/li')

    for item in review_items:
        # 标题
        item_title = item.xpath(".//p[@class='title']/span/a/text()")
        item_title = item_title[0].replace('\n','').replace(' ','')
        # 文本
        item_text = item.xpath('.//p[2]/text()')
        item_text = item_text[0].replace('\n','').replace(' ','')
        
        data_list.append({
            '标题' : item_title,
            '文本' : item_text
        })

    wait_time = random.uniform(2, 5)
    print(f"等待 {wait_time:.2f} 秒...")
    time.sleep(wait_time)

df = pd.DataFrame(data_list)
df.to_csv('壹心理.csv', index=False, encoding='utf-8-sig')
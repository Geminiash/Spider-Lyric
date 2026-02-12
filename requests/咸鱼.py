import requests
import hashlib
import time

cookies = {
    
}

headers = {
   
}

params = {
    
}

data = {
    
}

# 解密
res = '8448dc392ab36cd9bfc156e0a2e3b410&'
ts = str(int(time.time()*1000))
data_salt = res+ts+'&'+params['appKey']+'&'+data['data']
md5_enc = hashlib.md5()
md5_enc.update(data_salt.encode())
result = md5_enc.hexdigest()
params['sign'] = result
params['t'] = ts

response = requests.post(
    'https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

data_list = response.json()["data"]["resultList"]

for item in data_list:
    # 标题
    item_title = item["data"]["item"]["main"]["exContent"].get("detailParams",{}).get("title",'N/A')
    item_title = item_title.replace('\n','')
    # 价格
    item_price = item["data"]["item"]["main"]["clickParam"]["args"]["price"]
    # 地区
    item_area = item["data"]["item"]["main"]["exContent"]["area"]
    # 想要人数
    item_content = item["data"]["item"]["main"]["exContent"]["fishTags"].get("r3",{}).get("tagList",[{}])[0].get("data",{}).get("content",'N/A')
    print(item_content)
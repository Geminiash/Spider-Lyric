import requests
import hashlib
import time

cookies = {
    'cna': 'YAn6IXb451kBASQJikSzIpVx',
    't': '165ba911527b033a630fd2a0baa4b1a7',
    'cookie2': '10f1730cad7002feb0af096bd57659c2',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': '8448dc392ab36cd9bfc156e0a2e3b410_1770907647821',
    '_m_h5_tk_enc': 'ca4060d0820efed7584b8497e82caab2',
    '_samesite_flag_': 'true',
    '_tb_token_': '399e31beeea3e',
    'xlly_s': '1',
    'tfstk': 'gW_ingaF5G-sizDUrx8_AicRHiqd1FTXvt3vHEp4YpJIBA3OgxXcLTCtWZC2ntXpdVITfnpmiF_dXqpTCEfVeE28ezUR11tXu8e8g-HdpURDgquqHDRekIDCMGDl11TjO8e8yzC_oyncZV8V3e-ewC8qbcR4teR2MEuw0VoELpO2uE-2upRe1Iv2gCuat6JBgERw_t8UtIve3E8V36kUhm9lCTQUENop0L61VwAMjL53Vqu0TBDJE1oEz4bhX3pzop0quwAGgg6f84qvUg992HXUJVYcTIX9pTzr-e-lVsdcIP0wWMSC5FQLEbtGnpxPJH4EKBbhwgRCtuVhtZvM4N-nMVLeSIW2mMwoyCYOx3bGfSMF_TpG4F1xZRCHqMxWTHlmbFIRwZtP7PDWp3OcBpBzz2Ye0guoY0yu5qOUMwojchRBtLeIk8WMcCBSwWVnVy-wOCa3tWmjchRBtLF3t0oebBO_-',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.goofish.com',
    'priority': 'u=1, i',
    'referer': 'https://www.goofish.com/',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}

params = {
    'jsv': '2.7.2',
    'appKey': '34839810',
    't': '1770901899285',
    'sign': '249f1db13b011c77058b762f796c87d2',
    'v': '1.0',
    'type': 'originaljson',
    'accountSite': 'xianyu',
    'dataType': 'json',
    'timeout': '20000',
    'api': 'mtop.taobao.idlemtopsearch.pc.search',
    'sessionOption': 'AutoLoginOnly',
    'spm_cnt': 'a21ybx.search.0.0',
    'spm_pre': 'a21ybx.home.searchHistory.1.4c053da6QGi6X2',
    'log_id': '4c053da6QGi6X2',
}

data = {
    'data': '{"pageNumber":2,"keyword":"手机","fromFilter":false,"rowsPerPage":30,"sortValue":"","sortField":"","customDistance":"","gps":"","propValueStr":{},"customGps":"","searchReqFromPage":"pcSearch","extraFilterValue":"{}","userPositionJson":"{}"}',
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
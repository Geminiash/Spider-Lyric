import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd

headers = {
   
}

cookies = {
    
}

cookies_str = '; '.join([f'{key}={value}' for key, value in cookies.items()])

headers['Cookie'] = cookies_str

all_movies = []

for page in range(10):

    start = page * 25
 
    url = f"https://www.douban.com/doulist/3936288/?start={start}&sort=time&playable=0&sub_type="
    
    print(f"正在抓取第{page+1}页，URL: {url}")
    
    try:

        req = urllib.request.Request(url, headers=headers)
 
        response = urllib.request.urlopen(req)

        html = response.read().decode('utf-8')
    
        soup = BeautifulSoup(html, 'html.parser')
        
        movie_items = soup.find_all('div', class_='doulist-item')
        
        print(f"找到{len(movie_items)}个电影项目")

        for item in movie_items:

            movie_data = {
                '电影名称': '',
                '评分': '',
                '评论人数': '',
                '导演': '',
                '类型': '',
                '上映年份': '',
                '国家': ''  
            }
            
            title_tag = item.find('div', class_='title')
            if title_tag:

                movie_data['电影名称'] = title_tag.get_text(strip=True)
            
            rating_tag = item.find('div', class_='rating')
            if rating_tag:

                rating_nums = rating_tag.find('span', class_='rating_nums')
                if rating_nums:

                    movie_data['评分'] = rating_nums.get_text(strip=True)
            
            if rating_tag:
          
                import re
             
                text = rating_tag.get_text(strip=True)
                
                match = re.search(r'\((\d+)人评价\)', text)
                if match:
                    
                    movie_data['评论人数'] = match.group(1)
            
            abstract_tag = item.find('div', class_='abstract')
            if abstract_tag:
            
                abstract_text = abstract_tag.get_text()
                
                lines = abstract_text.strip().split('\n')
                
                for line in lines:
                    line = line.strip()  
               
                    if line.startswith('导演:'):
                        movie_data['导演'] = line.replace('导演:', '').strip()
                 
                    elif line.startswith('类型:'):
                        movie_data['类型'] = line.replace('类型:', '').strip()
                 
                    elif line.startswith('年份:'):
                        movie_data['上映年份'] = line.replace('年份:', '').strip()
                    
                    elif line.startswith('制片国家/地区:'):
                        movie_data['国家'] = line.replace('制片国家/地区:', '').strip()
            
            all_movies.append(movie_data)
        
        print(f"第{page+1}页抓取完成，获取到{len(movie_items)}部电影数据")
        
        time.sleep(5)
        
    except Exception as e:
    
        print(f"抓取第{page+1}页时出错: {e}")
     
        time.sleep(10)
        continue

if all_movies:

    df = pd.DataFrame(all_movies)
    
 
    df.to_excel('豆瓣Top250.xlsx', index=False)
    
    # 打印保存成功信息
    print(f"数据已保存到'豆瓣Top250.xlsx'，共{len(all_movies)}条记录")
else:

    print("未抓取到任何数据")
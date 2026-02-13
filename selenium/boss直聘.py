# pip install DrissionPage -i https://mirrors.aliyun.com/pypi/simple/

from DrissionPage import ChromiumPage
import time
import pandas as pd


jobname = "Python"
url = f"https://www.zhipin.com/web/geek/jobs?query={jobname}&city=100010000"
page = ChromiumPage()
#  创建监听
page.listen.start("wapi/zpgeek/search/joblist.json")
# 打开网站
page.get(url)
time.sleep(16)  # 等待扫码登录  只需要允许一次

data_list = []

for i in range(1,10):
    print(f'正在获取第{i}页数据')
    #  等待数据包加载
    packet = page.listen.wait(timeout=10)
    if packet:
        resp = packet.response.body  # 获取响应内容
        jobList = resp["zpData"]["jobList"]
        for job in jobList:
            # 岗位名称
            item_name = job.get("jobName",'N/A')
            # 薪资     
            item_desc = job.get("salaryDesc",'N/A')
            # 地区        
            item_city = job.get("cityName",'N/A')
            # 经验     
            item_exper = job.get("jobExperience",'N/A')
            # 学历      
            item_degree = job.get("jobDegree",'N/A')
            # 职位技能   
            item_skills = job.get("skills",'N/A')
            
            data_dict = {
                '岗位名称' : item_name,
                '薪资' : item_desc,
                '地区' : item_city,
                '经验' : item_exper,
                '学历' : item_degree,
                '职位技能' : item_skills
            }


            data_list.append(data_dict)

    else:
        print("请求获取失败")
    # 下滑页面
    page.scroll.to_bottom()
    time.sleep(2)

df = pd.DataFrame(data_list, columns=['岗位名称','薪资','地区','经验','学历','职位技能'])
df.to_csv('BOSS直聘.csv', index=False, encoding='utf-8-sig')
print('采集结束')
page.quit()
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求URL
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=10)
content = html.text
# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
# 找到完整的投诉信息框
temp = soup.find('div',class_="tslb_b")
tr_list = temp.find_all('tr')
# 读取表格的每一行信息
th_list = tr_list[0].contents
record=[]
#提取每一行信息
for th_td in tr_list:
    #提取每一列的信息
    row_data=[]
    for data in th_td:
        row_data.append(data.text)
    record.append(row_data.copy())
    row_data.clear()
result = pd.DataFrame(record)
result.to_csv('car_complain_data.csv', index=False, header=False)
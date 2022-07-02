'''
Author: Samrito
Date: 2021-10-21 22:34:17
LastEditors: Samrito
LastEditTime: 2021-10-30 17:12:18
'''
import requests
import re
from bs4 import BeautifulSoup
import csv
import time

proxy = {'http': 'http://127.0.0.1:10809','https': 'httpfd://127.0.0.1:10809'}
def request_wb(url):
    try:
        header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-encoding':'gzip, deflate, br',
                  'accept-language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',}
        reponse = requests.get(url, headers=header,proxies=proxy)
        if reponse.status_code==200:
            return reponse.text
    except requests.RequestException:
        return None


def parse_result(soup):
    info = soup.find("div",{"class":"txt_bottom"}).findAll("div",class_="txt_bottom_item")
    dct = {'导演':None, '编剧':None, '主演':None, '类型':None, '制片国家/地区':None, '语言':None,'片长':None}
    for div in info:
        attr = div.find("div",{"class":"txt_bottom_l"}).string
        attr = re.sub('\s','',attr)
        if '导演：' == attr:
            _ = []
            for name in div.findAll("a"):
                _.append(re.sub('\s','',name.string))
            dct['导演'] = '/'.join(_)
        elif '编剧：' == attr:
            _ = []
            for name in div.findAll("a"):
                _.append(re.sub('\s','',name.string))
            dct['编剧'] = '/'.join(_)
        elif '主演：' == attr:
            _ = []
            for name in div.findAll("a"):
                _.append(re.sub('\s','',name.string))
            dct['主演'] = '/'.join(_)
        elif '类型：' == attr:
            dct['类型'] = re.sub('\s','',div.find("div",{"class":"txt_bottom_r"}).string)
        elif '制片国家/地区：' == attr:
            dct['制片国家/地区'] = re.sub('\s','',div.find("div",{"class":"txt_bottom_r"}).string)
        elif '语言：' == attr:
            dct['语言'] = re.sub('\s','',div.find("div",{"class":"txt_bottom_r"}).string)
        elif '片长：' == attr:
            dct['片长'] = re.sub('\s','',div.find("div",{"class":"txt_bottom_r"}).string)
    with open('detail.csv','a',encoding='utf-8') as fcsv:
        csvwriter = csv.writer(fcsv)
        lst = [dct[e] for e in dct.keys()]
        csvwriter.writerow(lst)
        fcsv.close()
    time.sleep(5)
    
if __name__ == '__main__':
    url = 'https://www.imdb.cn/title/'
    with open('id.txt','r',encoding='utf-8') as f:
        for line in f:
            html = request_wb(url+line[:-1])
            print(html)
            soup = BeautifulSoup(html, 'html.parser')
            print(line)
            parse_result(soup)
        f.close()
    '''url = 'http://httpbin.org/ip'
    print(request_wb(url))'''

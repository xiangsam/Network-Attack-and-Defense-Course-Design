'''
Author: Samrito
Date: 2021-10-21 19:59:09
LastEditors: Samrito
LastEditTime: 2021-10-21 22:32:19
'''
import requests
import re

def request_wb(url):
    try:
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}
        reponse = requests.get(url, headers=headers)
        if reponse.status_code == 200:
            return reponse.text
    except requests.RequestException:
        return None

def parse_result(html):
    pattern = re.compile('<td\sclass="rl_poster">.*?<img\ssrc="(.*?)".*?<td\sclass="rl_name">.*?<a\shref=".?title.?(.*?).?".*?title=\'(.*?)\'\starget.*?<span>.*?(\d+).*?</span>.*?<td\sclass="rl_grade_IMDB">.*?<span>(.*?)</span></td>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'picture': item[0],
            'id': item[1],
            'title': item[2],
            'year': item[3],
            'imdb_score': item[4]
        }

def write_to_sql(html):
    print('begin to write=========>')
    with open('data.txt','w',encoding='utf-8') as f:
        for item in parse_result(html):
            string = [e+' ' for e in item.values()]
            string = ''.join(string) + '\n'
            f.write(string)
        f.close()

def write_to_list(html):
    with open('id.txt','w',encoding='utf-8') as f:
        for item in parse_result(html):
            f.write(item['id']+'\n')
        f.close()

if __name__ == '__main__':
    url = 'https://www.imdb.cn/imdb250/'
    html = request_wb(url)
    with open('html.txt','w',encoding='utf-8') as f:
        f.write(html)
        f.close()
    write_to_sql(html)
    write_to_list(html)
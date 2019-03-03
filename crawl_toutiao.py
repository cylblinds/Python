import requests
import json
import urllib
import re
from bs4 import BeautifulSoup as BS
import os


def get_page(offset):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    paras = {
            'aid': 24,
            'app_name': 'web_search',
            'offset': offset,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': 20,
            'en_qc': 1,
            'cur_tab': 1,
            'from': 'search_tab',
            'pd': 'synthesis'
            }

    url = 'https://www.toutiao.com/api/search/content/?'+urllib.parse.urlencode(paras)
    try:
        res = requests.get(url,headers=headers)
        res.raise_for_status
        json = res.json()
        return json.get('data')
    except:
        return None

def get_json_images(json_data):
    for item in json_data:
        if item.get('article_url'):
            article_url = item.get('article_url')
            url = article_url.replace('http://toutiao.com/group/','https://www.toutiao.com/a')
            title = item.get('title')
            print(url,title)
            if '日本' not in title:
                if not os.path.exists(title):
                    os.makedirs(title)
                    res = requests.get(url)
                    pre = re.compile(r'http:\\\\/\\\\/[\w]+.pstatp.com\\\\/origin\\\\/pgc-image\\\\/[\w]+')
                    result = pre.findall(res.text)
                    for i in result:
                        i = i.replace('\\','')
                        name = i[-23:]
                        print(name)
                        image = requests.get(i)
                        if not os.path.exists(title+'/'+name+'.jpg'):
                            with open(title+'/'+name+'.jpg','wb') as f:
                                    f.write(image.content)
                        else:
                            pass
                else:
                    pass

# def get_heml_images(html_data):

def main(pages):
    for i in range(pages):
        json_data = get_page(20*i)
        get_json_images(json_data)


pages = 2
main(pages)

#/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

class QuNaEr():
    def __init__(self, keyword, page=1):
        self.keyword = keyword
        self.page = page
        print(keyword)

    def qne_spider(self):
        url = 'https://piao.qunar.com/ticket/list.htm?keyword=%s&region=%s&from=mpshouye_hotcity' % (self.keyword, self.page)
        #url = 'https://piao.qunar.com/ticket/list.html?keyword=%s&region=&from=mpl_search_suggest&page=%s' % (self.keyword, self.page)
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        bs_obj = BeautifulSoup(text, 'html.parser')

        arr = bs_obj.find('div',{'class':'result_list'}).contents
        for i in arr:
            info = i.attrs
            print(i)
            name = info.get('data-sight-name')
            address = info.get('data-address')
            count = info.get('data-sale-count')
            point = info.get('data-point')

            price = i.find('span',{'class':'sight_item_price'})
            price = price.find_all('em')
            price = price[0].text

            conn = MongoClient('localhost',port=27017)
            db = conn.QuNaEr
            table = db.qunaer_52

            table.insert_one({
                'name' : name,
                'address' : address,
                'count': count,
                'point' : point,
                'price' : float(price),
                'city' : self.keyword
                })

if __name__ == '__main__':
    citys = ['北京','上海','成都']
    for i in citys:
        for page in range(1,2):
            qne = QuNaEr(i,page = page)
            qne.qne_spider()








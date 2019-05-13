#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from pylab import *
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

mpl.rcParams[ 'font.sans-serif' ] = ['SimHei']

conn = MongoClient('localhost', port=27017)
db = conn.QuNaEr
table = db.qunaer_52

result = table.find().sort([('count',-1)]).limit(15)

x_arr = []
y_arr = []

for i in result:
    x_arr.append(i['name'])
    y_arr.append(i['count'])

plt.bar(x_arr, y_arr, color='rgb')
plt.gcf().autofmt_xdate()
plt.xlabel(u'景点名称')
plt.ylabel(u'月销量')
plt.title(u'拉钩景点月销售统计表')
plt.ylim(0.4000)
plt.savefig('去哪儿月销售量排行榜')
plt.show()

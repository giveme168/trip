#coding:utf-8

import logging
import datetime
import simplejson as json

import sys
from config import APP_PATH
from config import LOG_FILE
sys.path.append(APP_PATH) 

from django.core.management import setup_environ

import settings
setup_environ(settings)

from django.contrib.auth.models import User
from apps.product.models.product import Products,Product_Add_Service,Special_Tags,Product_Tags

PRODUCTS = [
    {
    'name':u'全新欧洲参与型冬季深度游8天',
    'date_count':8,
    'price_type':1,
    'price_by_one':6000,
    'total_price_by_one':6000,
    'price_by_two':4800,
    'total_price_by_two':4800,
    'price_by_three':4700,
    'total_price_by_three':4700,
    'price_by_four':4600,
    'total_price_by_four':4600,
    'price_by_five':4550,
    'total_price_by_five':4550,
    'price_by_six':4500,
    'total_price_by_six':4500,
    'price_by_serven':4450,
    'total_price_by_serven':4450,
    'price_by_eight':4400,
    'total_price_by_eight':4400,
    'order_time':'2014-05-31',
    'trip_start_time':'2014-06-01',
    'trip_end_time':'2014-09-01',
    'start_city':u'北京',
    'end_city':u'特罗姆瑟|斯沃崴岛',
    'end_country':u'挪威',
    'language':u'中文|英文',
    'tags':u'猎人式酒店|狗拉雪橇|极光探',
    'key_desc':u'* 极地郎伊尔城: 入住猎人式酒店, 狗拉雪翘<br/>* 在最北城市特罗姆瑟 : 极光探险, 萨米族糜鹿<br/>* 罗富敦群岛最大岛屿斯沃崴岛: 冬季出海钓鱼/海鹰探险/参与自做鱼餐和鱼籽酱<br/>* 全程原生野味食品<br/>* 全程 我公司资深导游带团, 精通挪, 英，中文和挪威社会<br/>* 一晚挪威海岸线油轮',
    'pics':'3c5bffc18e464440be34fb4d6e81794b.png|c20f375ca6aa4b78ac8b0de18c7d6c1d.png',
    'trips':[
        {
        'traffic':u'早上乘坐航班经挪威首都奥斯陆前往位于北极圈内的挪威自治岛斯瓦尔巴群岛，导游接机后前往芭瑟卡玛普塔普尔酒店',
        'hotel':u'芭瑟卡玛普塔普尔酒店,这是郎伊尔城最具特色的酒店（酒店位于郎伊尔城市中心，每个房间都有其独特的装饰配上捕猎风格与浮木，海豹皮等完美结合，酒店无线互联网无处不在）',
        'breakfast':u'酒店提供早餐',
        'lunch':u'午餐在酒店享受挪威特色简餐',
        'dinner':u'晚上特别安排帐篷篝火晚餐，享受和萨迷族人风味的晚餐稍候入住酒店休息',
        'project':u'下午安排体验贵族娱乐雪橇犬拉雪橇车，在北极大部分拉雪橇的都是纯种西伯利亚哈士奇、阿拉斯加雪橇犬等，体验专业的雪橇犬团队在雪地上的激情和动力！',
        'pics':u'12e0ae1942dd49e1b4c2d918e8e8709c.png|17c95337fc624da49b0974d765bb4089.png',
    	}
    ],
    'body':{
        'more_contact':u'是',
        'hotel_diff_price':500,
        'price_contain':u'岸全包价',
        'price_no_contain':u'私人消费',
        'cancel_detail':u'提前30天取消免费，提前7天取消扣20%，提前3天取消扣100%',
        'special_attention':u'保险理赔不包括超速'
    },
    'add_service':[
        {
    	'content':u'在卡普LINNE，朗伊爾城90公里，我們 歡迎我們的客人伊斯峽灣電台，於2007年開業。 這是朗伊爾城以外唯一的全規模的精品酒店，轉換電台在中間的顯著北極原野，面對巴倫支海。 一月份白天也能看到北极光！',
    	'price_type':1,
    	'price_by_one':100,
    	'total_price_by_one':100,
    	'body':{'pics':'7da81f26abe8462ab1ae2beb0f443fca.png'}
        }
    ]
    }
]

def run():

    for product in PRODUCTS:
        #导入产品详情
        pro = Products()
        pro.name = product['name']
        pro.price_type = product['price_type']
        pro.price_by_one = product['price_by_one']
        pro.total_price_by_one = product['total_price_by_one']
        pro.price_by_two = product['price_by_two']
        pro.total_price_by_two = product['total_price_by_two']
        pro.price_by_three = product['price_by_three']
        pro.total_price_by_three = product['total_price_by_three']
        pro.price_by_four = product['price_by_four']
        pro.total_price_by_four = product['total_price_by_four']
        pro.price_by_five = product['price_by_five']
        pro.total_price_by_five = product['total_price_by_five']
        pro.price_by_six = product['price_by_six']
        pro.total_price_by_six = product['total_price_by_six']
        pro.price_by_serven = product['price_by_serven']
        pro.total_price_by_serven = product['total_price_by_serven']
        pro.price_by_eight = product['price_by_eight']
        pro.total_price_by_eight = product['total_price_by_eight']
        pro.order_time = datetime.datetime.strptime(product['order_time'],'%Y-%m-%d')
        pro.trip_start_time = datetime.datetime.strptime(product['trip_start_time'],'%Y-%m-%d')
        pro.trip_end_time = datetime.datetime.strptime(product['trip_end_time'],'%Y-%m-%d')
        pro.key_desc = product['key_desc']
        pro.start_city = product['start_city']
        pro.end_country = product['end_country']
        pro.end_city = product['end_city']
        pro.language = product['language']
        pro.tags = product['tags']
        pro.pics = product['pics']
        pro.trips = json.dumps(product['trips'])
        pro.date_count = product['date_count']
        pro.user = User.objects.get(id=1)
        pro.body = json.dumps(product['body'])
        pro.status = 2
        pro.save()
        #导入增值服务
        for service in product['add_service']:
            pro_add_service = Product_Add_Service()
            pro_add_service.prodect = pro
            pro_add_service.content = service['content']
            pro_add_service.price_type = service['price_type']
            pro_add_service.price_by_one = service['price_by_one']
            pro_add_service.body = json.dumps(service['body'])
            pro_add_service.save()

        tags = product['tags'].split('|')
        for tag in tags:
            stag = Special_Tags()
            stag.name = tag
            stag.name_en = tag
            try:
                stag.save()
            except:
                try:
                    stag = Special_Tags.objects.get(name=tag)
                except:
                    stag = None
                    
            if stag:
                ptag = Product_Tags()
                ptag.prodect = pro
                ptag.tag = stag
                try:
                    ptag.save()
                except:
                    pass

    return

if __name__ == '__main__':
    run()
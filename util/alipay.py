#coding=utf-8

import uuid
from datetime import datetime
import StringIO
import urllib
import string
import hashlib

gateway	= "https://www.alipay.com/cooperate/gateway.do?"
partner = "2088701685055791" #合作身份者ID
security_code   = "qjlz6d9nfm9wh8hst0w1m2bpwsyoygq7" #安全检验码
seller_email    = "jkzx33@163.com" #签约支付宝账号或卖家支付宝帐户

_input_charset  = "utf-8"#字符编码格式 目前支持 GBK 或 utf-8
transport       = "http" #访问模式,根据自己的服务器是否支持ssl访问，若支持请选择https；若不支持请选择http

notify_url_default      = "http://112.124.100.205/alipay/notify" #交易过程中服务器通知的页面 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
return_url_default      = "http://112.124.100.205/alipay/redirect" #付完款后跳转的页面 要用 http://格式的完整路径，不允许加?id=123这类自定义参数

show_url        = "http://112.124.100.205/" #网站商品的展示地址，不允许加?id=123这类自定义参数

sign_type       = "MD5" #加密方式 不需修改
antiphishing    = "0" #防钓鱼功能开关，'0'表示该功能关闭，'1'表示该功能开启。默认为关闭

def make_sign(params):
	params_list = []
	for k in params:
		if type(k) == type(u''):
			kk = k.encode('utf-8')
		else:
			kk = k
		if type(params[k]) == type(u''):
			p = params[k].encode('utf-8')
		else:
			p = params[k]
		if (kk == 'sign') or (kk == 'sign_type') or (p == ''):
			continue
		params_list.append('%s=%s'%(kk, p))
	try:
		params_list.sort()
		param = string.join(params_list, '&')
		param = param + security_code
		m = hashlib.md5(param)
	except Exception, e:
		import logging
		logging.debug(str(e))
	return m.hexdigest()

def pay_req(pay_id, subject, body, total_fee, notify_url = notify_url_default, return_url = return_url_default):
	if type(subject) == type(u''):
		subject = subject.encode(_input_charset)
	if type(body) == type(u''):
		body = body.encode(_input_charset)
	if type(total_fee) != type(''):
		total_fee = str(total_fee)
	params = {'service':'create_direct_pay_by_user',
		'payment_type': 1,
		'partner': partner,
		'_input_charset': _input_charset,
		'seller_email': seller_email,
		'sign_type': sign_type,
		'notify_url': notify_url,
		'return_url': return_url,
		'show_url':show_url,
		'out_trade_no': pay_id, 
		'subject': subject,
		'body': body,
		'total_fee': total_fee}
	sign = make_sign(params)
	params['sign'] = sign
	uri = urllib.urlencode(params)
	url = gateway + uri
	return url

if __name__ == '__main__':
	print pay_req('id-xxx', u'海南五日游', u'费用', 1)

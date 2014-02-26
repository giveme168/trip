# -*- coding:utf8 -*-

def ip_check(ip):
	q = ip.split('.')
	return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, map(int, filter(lambda x: x.isdigit(), q)))) == 4
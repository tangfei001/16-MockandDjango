#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 10:42
# @Author  : Aries
# @Site    : 
# @File    : cilent.py
# @Software: PyCharm

import requests
import shutil

def send_request(url):
	r=requests.get(url)
	return r.status_code

def visit_ustack():
	'''自己写的测试函数'''
	r=send_request('http://www.ustack.com')

class Remove(object):
	def rmdir(self,path='c:/'):
		r=shutil.rmtree(path)
		if r==None:
			return 'succeed'
		else:
			return 'fail'

	def exsit_get_rmdir(self):
		'''自己写的测试函数'''
		return self.rmdir()

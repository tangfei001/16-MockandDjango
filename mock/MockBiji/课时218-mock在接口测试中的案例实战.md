**课时218-mock在接口测试中的案例实战**


步骤:

## 01:cilent.py ##

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

## 02:mockTest.py ##

from D16 import cilent
from unittest import mock
import unittest

class MockTest(unittest.TestCase):
	def test_fail_send(self):
        #client=mock.Mock(return_value='xxxxx')
		fail_send=mock.Mock(return_vlaue='404')
        #替换开发写的函数
		cilent.send_request=fail_send
        #断言-中使用自己写的函数
		self.assertEqual(cilent.visit_ustack(),fail_send())

	def test_succeed_send(self):
		succeed_send=mock.Mock(return_value='200')
		cilent.send_request=succeed_send
		self.assertEqual(cilent.visit_ustack(),succeed_send())

if __name__ == '__main__':
    unittest.main(verbosity=2)
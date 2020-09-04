#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 10:45
# @Author  : Aries
# @Site    : 
# @File    : mockTest.py
# @Software: PyCharm
from D16 import cilent
from unittest import mock
import unittest

class MockTest(unittest.TestCase):
	def test_fail_send(self):
		fail_send=mock.Mock(return_vlaue='404')
		cilent.send_request=fail_send
		self.assertEqual(cilent.visit_ustack(),fail_send())

	def test_succeed_send(self):
		succeed_send=mock.Mock(return_value='200')
		cilent.send_request=succeed_send
		self.assertEqual(cilent.visit_ustack(),succeed_send())

if __name__ == '__main__':
    unittest.main(verbosity=2)


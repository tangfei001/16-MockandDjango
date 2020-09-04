**课时217(重点)--mock的介绍和详解**

# 核心东西: #
01:使用mock的对象去模拟
cilent=mock.Mock(return_value='xxxxxx')

02:mock中使用patch或者patch.object的目的是为了控制mock的范围,模拟的类或者模拟的函数
，使用 with语句范围内nock一个对象。

## Pyhton3.3版本之后引入方式是： ##
from unittest import  mock 


## 案例说明:测试一个网站 ##

步骤:
*01:D16-client.py中编写 visit_ustack()*

   #自己写一个测试函数,来引用开发写的函数
   def visit_ustack():
	   r=send_request('http://www.ustack.com')

*02:D16-mockTest.py中编写*

from D16 import cilent
from unittest import mock
import unittest

class MockTest(unittest.TestCase):
	def test_fail_send(self):
		fail_send=mock.Mock(return_vlaue='404')
		cilent.send_request=fail_send
		self.assertEqual(cilent.visit_ustack(),'404')

	def test_succeed_send(self):
        #client=mock.Mock(return_value='xxxxxx')
		succeed_send=mock.Mock(return_value='200') 
        #替换函数
		cilent.send_request=succeed_send
        #替换函数
		self.assertEqual(cilent.visit_ustack(),'200')

if __name__ == '__main__':
    unittest.main(verbosity=2)


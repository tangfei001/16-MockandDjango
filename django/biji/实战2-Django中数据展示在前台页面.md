实战2-Django中数据展示在前台页面


01:在five-app-views.py中编写def douban(requests)

  001:import requests  import json
  002:def douBan()
      01:完善接口 r=requests.get()
      02:print(r.json) #拿到所有的返回信息后,注释print,用json在线工具处理
      03:循环的取数据,以列表的形式展示
           03:定义一个列表 movies=[]
		   for i in range(20):
                03:定义一个列表 movies=[]
			    01-完善接口信息
                02-拿到对应的数据
                04-movies.append({'xx':'xx'})
	  04:函数返回值
		   return render(request,'laGou.html',locals())
  003:douban()

02:定义模板文件
   templates-HTML File-douban
   完善html代码

03:在url.py中添加
	 path('douBan/',douBan,name='douBan')

04:启动Django服务
   run-manage.py

05:浏览器中访问地址

06:在官方网站下载bootstarp前端框架
   01:使用cdn方式-具体见 douban.html
   02:使用bootstarp中文官方文档,对表格进行修改

07:刷新页面查看结果

      
# coding:utf-8

'''
@version:3.8
@author:qiuzhi
'''
from rest_framework.views import Response

class APIResponse(Response):
    # 定义一个初始化函数，这个里面 参数借鉴了父类init需要的这些。能实例化出来一个异常的对象
    def __init__(self,code=1,msg='成功',result=None,data=None,
                  headers=None,status=None,
                  content_type=None,**kwargs):    # 同时加上了一个kwargs来装token
        dic={'code':code,
             'msg':msg}  # 默认字典里有这两个信息，响应码和信息
        if result:
            dic['result']=result   # 响应结果如果有的话传一个到字典
        dic.update(kwargs)  # 如果有传额外信息也添加进去
        #  调用父类的初始化，把我们自己组织的字典当成data传给父类的方法
        super().__init__(data=dic,status=status,
                 headers=headers,content_type=content_type)
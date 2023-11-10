# coding:utf-8

'''
@version:3.8
@author:qiuzhi
'''

# 为了更多更详细的异常，只需要重新rest_framework里一个异常处理函数，在rest的settings配置里面有个默认的配置。exception_handler
'''
    # Exception handling
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    '''
from rest_framework.views import exception_handler
from .response import APIResponse   # 用.代表当前路径下的文件夹，把response导过来用于返回我们自己处理的异常信息
from helloword_backend.utils import response # 也可以这样导
from .logger import log  # 把我们实例化出来的日志对象导入，直接在异常下添加日志


''''exc,异常对象，本次发生的异常对象
context,字典，本次发生异常时，python解析器提供的执行上下文
    所谓的执行上下文[context]，就是程序执行到当前一行代码时，
    能提供给开发者调用的环境信息异常发生时，代码所在的路径，时间，视图，客户端http请求等等...]
'''
def common_exception_handler(exc, context):  # 用它原本要的参数
    log.error('错误视图view：%s 错误类型type：%s 错误信息msg：%s'%((context['view']).__class__.__name__,exc.__class__.__name__,str(exc)))
    # context['view'])这是出错的视图类的对象.__class__.__name__可以取到他的类的名字，也就是出错视图类
    # exc.__class__.__name__这个就是报错里面的错误类keyerror什么的
    ret=exception_handler(exc,context)  # 先让他自己处理，处理完如果返回值为空，代表它处理不了，我们自己处理
    # ret如果有值，返回的会是一个response对象，里面有data属性，statu等等
    if not ret: # 其实可以用isinstance来判断很多种错误，颗粒度加细，也可以直接把response实例化出来最后都返回response对象
        return response.APIResponse(code=0,msg=exc.__class__.__name__,result=str(exc))
    else:
        return APIResponse(code=0,msg='error',result=ret.data)

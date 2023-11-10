from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware

# 这一个文件是为了解决跨域问题
class MyCORS():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 在视图执行之前的代码...

        response = self.get_response(request)
        # 在视图执行之后的代码...
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8001'
        if request.method=='OPTIONS':
            response['Access-Control-Allow-Methods'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type'

        return response

class MyCORS2(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8001'
        if request.method=='OPTIONS':
            response['Access-Control-Allow-Methods'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type'

        return response

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class M1(MiddlewareMixin):
    def process_request(self,request):
        #读取当前访问的用户信息
        info=request.session.get("info")
        # if request.path_info=='/load/'or request.path_info=='':
        #     return
        if request.path_info!='/locate/' and request.path_info!='/load/':
            return
        print(info)
        if info:
            print('登录了')
            return
        else:
            request.session["info"] = {'id': 'xxxx'};
            print('匿名登录')
            return

    def process_response(self,request,response):
        print('go了')
        return response




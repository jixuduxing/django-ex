import os
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib

class Weixin(View):
    token = 'jixuduxing'

    def validate(self, request):
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')

        tmp_str = hashlib.sha1(''.join(sorted([self.token, timestamp, nonce]))).hexdigest()
        assert False
        if tmp_str == signature:
            return True

        return False

    @csrf_exempt
    def get(self, request):
        if self.validate(request):
            return HttpResponse(request.GET.get('echostr', ''))
        return HttpResponse('2')

    @csrf_exempt
    def post(self,request):
        return HttpResponse('1')

        # raise PermissionDenied

def hello(request):
    # hostname = os.getenv('HOSTNAME', 'unknown')
    if request.method == 'GET':
        rsp = request.GET.get('echostr', 'error')
    else:
        # message = wechat.get_message()
        # rsp = wechat.response_text(u'��Ϣ����: {}'.format(message.type))
        return HttpResponse("Hello world ! ")
    return HttpResponse(rsp)
    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

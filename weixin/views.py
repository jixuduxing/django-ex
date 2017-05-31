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
        import logging
        signature = request.GET.get('signature', '')
        logging.debug('signature:'+signature)
        timestamp = request.GET.get('timestamp', '')
        logging.debug('timestamp:'+timestamp)
        nonce = request.GET.get('nonce', '')
        logging.debug('nonce:'+nonce)

        tmp_str = hashlib.sha1(''.join(sorted([self.token, timestamp, nonce]))).hexdigest()
        logging.debug('tmp_str:'+tmp_str)
        # assert False
        if tmp_str == signature:
            return True
        logging.debug('return False')
        return False

    @csrf_exempt
    def get(self, request):
        import logging
        logging.debug('request:'+str(request))
        if self.validate(request):
            logging.debug('echostr')
            return HttpResponse(request.GET.get('echostr', ''))
        logging.debug('2')
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
        # rsp = wechat.response_text(u'消息类型: {}'.format(message.type))
        return HttpResponse("Hello world ! ")
    return HttpResponse(rsp)
    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

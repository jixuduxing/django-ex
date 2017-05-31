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
        list = [self.token, timestamp, nonce]
        list.sort()
        sha2 = hashlib.sha1()
        map(sha2.update, list)
        hashcode = sha2.hexdigest()
        logging.debug('hashcode:' + hashcode)
        if hashcode == signature:
            return True
        logging.debug('return False')
        return False

    @csrf_exempt
    def get(self, request):
        import logging
        logging.debug('request:')
        if self.validate(request):
            logging.debug('echostr')
            return HttpResponse(request.GET.get('echostr', '2'))
        logging.debug('2')
        return HttpResponse(request.GET.get('echostr', '2'))

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
        return HttpResponse("Hello world ! ")
    return HttpResponse(rsp)
    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

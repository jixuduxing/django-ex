import os
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import View
from django.http import HttpResponse

def hello(request):
    # hostname = os.getenv('HOSTNAME', 'unknown')
    if request.method == 'GET':
        rsp = request.GET.get('echostr', 'error')
    else:
        # message = wechat.get_message()
        # rsp = wechat.response_text(u'消息类型: {}'.format(message.type))
        return HttpResponse("Hello world ! ")
    return HttpResponse(rsp)
    # return render(request, 'welcome/index.html', {
    #     'hostname': hostname,
    #     'database': database.info(),
    #     'count': PageView.objects.count()
    # })

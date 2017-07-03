import os
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.encoding import smart_str
import hashlib
import time
from .weimsg import WeiMsg
import xml.etree.ElementTree as ET
import traceback
import urllib2
import json
# TOKEN = "******"
API_KEY = 'bb0d3afc6f344cc1a5c177e73a9d3bea'

def paraseMsgXml(rootElem):
    msg = {}
    if rootElem.tag == 'xml':
        for child in rootElem:
            msg[child.tag] = smart_str(child.text)
    return msg

def getReplyXml(msg,replyContent):
    TextReply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>";
    TextReply = TextReply % (msg['FromUserName'],msg['ToUserName'],str(int(time.time())),'text',replyContent)
    return TextReply

def responseMsg(request):
    rawStr = smart_str(request.raw_post_data)
    msg = paraseMsgXml(ET.fromstring(rawStr))
    if msg['Content'] == 'Hello2BizUser':
        replyContent = 'thankyou!'
    else:
        replyContent = 'Hello'
    return getReplyXml(msg, replyContent)

TOKEN = "jixuduxing"

def checkSignature(request):
    global TOKEN
    signature = request.GET.get("signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echoStr = request.GET.get("echostr",None)

    token = TOKEN
    tmpList = [token,timestamp,nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echoStr
    else:
        return None

@csrf_exempt
def handleRequest(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request),content_type="text/plain")
        return response
    elif request.method == 'POST':
        response = HttpResponse(responseMsg(request),content_type="application/xml")
        return response
    else:
        return None


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
        import logging
        try:
            logging.debug('post')
            logging.debug(repr(request))
            logging.debug(request.body)
            recv_msg = WeiMsg(request.body)
            raw_tulingURL = "http://www.tuling123.com/openapi/api?key=%s&%s&info=" % (API_KEY,recv_msg.from_user_name)
            tulingURL = "%s%s" % (raw_tulingURL,urllib2.quote(recv_msg.content))
            req=urllib2.Request(tulingURL)
            raw_json=urllib2.urlopen(req).read()
            hjson=json.loads(raw_json)
            length=len(hjson.keys())
            content=hjson['text'].encode('utf-8')
            if length==3:
                replyContent= "%s%s"%(content,hjson['url'].encode('utf-8'))
            elif length==2:
                replyContent= content
            else:
                return "please input again."

            context = {
                'toUser': recv_msg.from_user_name,
                'fromUser': recv_msg.to_user_name,
                'createTime': int(time.time()),
                'type': recv_msg.msg_type,
                'content': replyContent,
            }
            # context = {
            #     'toUser': recv_msg.from_user_name,
            #     'fromUser': recv_msg.to_user_name,
            #     'createTime': int(time.time()),
            #     'type': recv_msg.msg_type,
            #     'content': recv_msg.content,
            # }
            logging.debug(str(context) )
            rendered = render_to_string('reply_text.xml', context)
            return HttpResponse(rendered)
        except Exception as ex:
            logging.debug('something wrong:')
            logging.debug(ex)


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

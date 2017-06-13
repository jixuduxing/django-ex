import hashlib
import os
import re

# basic info
re_msg_type = re.compile(r"<MsgType><!\[CDATA\[(.*?)\]\]></MsgType>")
re_msg_tuid = re.compile(r"<ToUserName><!\[CDATA\[(.*?)\]\]></ToUserName>")
re_msg_fuid = re.compile(r"<FromUserName><!\[CDATA\[(.*?)\]\]></FromUserName>")
re_msg_ctime = re.compile(r"<CreateTime>(.*?)</CreateTime>")
re_msg_id = re.compile(r"<MsgId>(.*?)</MsgId>")
re_media_id = re.compile(r"<MediaId><!\[CDATA\[(.*?)\]\]></MediaId>")
# text msg
re_text_content = re.compile(r"<Content><!\[CDATA\[(.*?)\]\]></Content>")


# img msg
re_img_url = re.compile(r"<PicUrl><!\[CDATA\[(.*?)\]\]></PicUrl>")
re_img_id = re.compile(r"")
# location msg
re_locx = re.compile(r"<Location_X>(.*?)</Location_X>")
re_locy = re.compile(r"<Location_Y>(.*?)</Location_Y>")
re_scale = re.compile(r"<Scale>(.*?)</Scale>")
re_label = re.compile(r"<Label><!\[CDATA\[(.*?)\]\]></Label>")

# link msg
re_title = re.compile(r"<Title><!\[CDATA\[(.*?)\]\]></Title>")
re_description = re.compile(r"<Description><!\[CDATA\[(.*?)\]\]></Description>")
re_url = re.compile(r"<Url><!\[CDATA\[(.*?)\]\]></Url>")

# event msg
re_event = re.compile(r"<Event><!\[CDATA\[(.*?)\]\]></Event>")
re_eventkey = re.compile(r"<EventKey><!\[CDATA\[(.*?)\]\]></EventKey>")


class WeiMsg(object):


    def get_info(self, regx, msg):
        result = re.findall(regx, msg)
        if result:
            return result[0]
        else:
            return ''

    def get_text_msg(self, msg):

        self.content = self.get_info(re_text_content, msg)

    def get_img_msg(self, msg):

        self.pic_url = self.get_info(re_img_url, msg)
        self.media_id = self.get_info(re_media_id, msg)

    def get_location_msg(self, msg):

        self.location_x = self.get_info(re_locx, msg)
        self.location_y = self.get_info(re_locy, msg)
        self.scale = self.get_info(re_scale, msg)
        self.label = self.get_info(re_label, msg)

    def get_link_msg(self, msg):

        self.title = self.get_info(re_title, msg)
        self.description = self.get_info(re_description, msg)
        self.url = self.get_info(re_url, msg)

    def get_event_msg(self, msg):
        self.event = self.get_info(re_event, msg)
        self.event_key = self.get_info(re_eventkey, msg)

    def __init__(self, msg):
        """genetate a message object
        """
        msg = msg.decode('utf-8')
        self.to_user_name = self.get_info(re_msg_tuid, msg)
        self.from_user_name = self.get_info(re_msg_fuid, msg)
        self.create_time = self.get_info(re_msg_ctime, msg)
        self.msg_type = self.get_info(re_msg_type, msg)
        self.msg_id = self.get_info(re_msg_id, msg)
        msgtype = self.msg_type
        if msgtype == 'text':
            self.get_text_msg(msg)
        elif msgtype == 'image':
            self.get_img_msg(msg)
        elif msgtype == 'location':
            self.get_location_msg(msg)
        elif msgtype == 'link':
            self.get_link_msg(msg)
        elif msgtype == 'event':
            self.get_event_msg(msg)

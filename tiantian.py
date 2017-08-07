# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
from time import sleep
import settings
from xiaozhushou_util import *
import re
reload(sys)  
sys.setdefaultencoding('utf8')

itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.get_chatrooms(update=True)
settings.init()

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(settings.vT, msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  CurUserName = msg['FromUserName']
  if(preventAbuseTalking(CurUserName)):
    return
  sendGroupInviteMsg(msg,CurUserName)

#send group invite msg according to digits
def sendGroupInviteMsg(msg,CurUserName):
  msgText = msg['Text']
  x = re.findall(r'\d+', msgText)
  if(len(x) >0):
    y= int(x[0])
    if(y>=0 and y<=10):
      pullMembersMore(msg, settings.chatGroups[y*2], CurUserName)
      sleep(0.5)
      pullMembersMore(msg, settings.chatGroups[y*2+1], CurUserName)
      sleep(0.5)
  itchat.send_msg(settings.vT, CurUserName)
  sleep(0.5)

#if group chat msg contains kick ads, start kicking logic
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    #print msg
    #if u'超然群主233' in msg['ActualNickName']:
    if u'@774514af2f79102d03828205cc9b3c77926b8643fa75749be3a5082cf6149917' in msg['ActualUserName']:
      content = msg['Content']
      if(content[0]=="@"):
        if u'广告' in content:
          delUser(msg['FromUserName'],content)

itchat.run() 





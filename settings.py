# -*- coding: UTF-8 -*-
import datetime
def init():
  global admins
  global chatGroups
  global vT
  global usersDict
  global ADMIN
  global previousDay

  chatGroups =[
  u'UIUC二手交易群',u'线上KTV',
  u'UIUC租房群2',u'UIUC内推找工作群2',
  u'UIUC二手车',u'UIUC宠物群',
  u'UIUC ECE大家庭',u'UIUC CS大家庭🌽',
  u'UIUC经济',u'北美信用卡',
  u'UIUC统计',u'玉米地小球',
  u'UIUC 心理系大家庭',u'UIUC 物理系大家庭',
  u'18春季香槟托儿',u'UI食神',
  u'北美表情分享','2018 UIUC往返芝加哥班车群',
  u'Chuck郭律师','北美CPA',
  u'2018 H1B 中中中',u'北美区块链技术交流总群',
  ]
  save = [
    u'北美妈妈母婴', u'北美CPA',
    u'UIUC CS刷题',u'17暑假',
    u'UIUC狼人杀',u'UIUC手机',
    u'找莹颖群',u'UIUCcarpool',
    u'UIUC行李',u'UIUC统计',
  ]

  v0= u"您好，😊 UIUC加群建群小助手😊 为您服务～\n"
  v00=u"每天只能加2个群哦;\n" 
  v1= u"回复 0 加UIUC二手交易群;线上KTV开嗓🎙️北美总群;\n"
  v2= u"回复 1 加UIUC租房群;UIUC内推找工作群;\n";
  v3= u"回复 2 加UIUC二手车群;UIUC宠物群🐱 🐶 🦆🐻  🐷 \n"
  v4= u"回复 3 加UIUC ECE大家庭；UIUC CS大家庭;\n"
  v5= u"回复 4 加UIUC经济系大家庭;北美信用卡爱好者;\n"
  v6= u"回复 5 加UIUC统计系大家庭;玉米地小球俱乐部; \n"
  v7= u"回复 6 加UIUC心理系大家庭;UIUC物理系大家庭\n"
  v8= u"回复 7 18春季香槟托儿所;加UI食神带飞群;\n"
  v9= u"回复 8 加北美表情分享总群;2018 UIUC往返芝加哥班车群;\n"
  v10= u"回复 9 加Chuck郭律师美帝绿卡讨论群;北美CPA,REG天天刷题群;\n"
  v11= u"回复 10 加H1B中中中讨论群;北美区块链技术交流总群\n\n"
  v12= u"回复 99 查看【北美加群小助手Jogchat.com】\n微信公众号二维码加纽约，硅谷，西雅图等群(无限次数)\n\n"
  v13= u"回复 100 加UIUC课程群小助手(无限次数)\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13
 
  
  vv0= u"回复 0 加北美母婴总群;北美CPA,REG天天刷题群\n"
  vv1= u'天天健身',u'UI食神',
  vv2= u"回复 2 加天天健身北美总群;加食神带飞群;\n"

  usersDict = {}
  admins =[]
  ADMIN = u'UIUC香槟加群小助手'
  previousDay = datetime.datetime.now().day

# -*- coding: UTF-8 -*-
def init():
  global admins
  global chatGroups
  global vT
  global usersDict
  chatGroups =[
  u'北美妈妈母婴', u'北美CPA',
  u'UIUC2017经济系',u'北美信用卡',
  u'天天健身',u'UI食神',
  u'UIUC ECE找队友',u'UIUC CS找队友2',
  u'UIUC CS刷题',u'17暑假',
  u'UIUC狼人杀',u'UIUC手机',
  u'UIUC租房天天',u'玉米地小球',
  u'找莹颖群',u'UIUCcarpool',
  u'UIUC行李',u'UIUC统计',
  u'UIUC二手车',u'UIUC宠物群',
  u'线上KTV',u'香槟二手交易群天天',
  u'UI食神',u'17秋季香槟托儿'
  u'北美表情分享'
  ]

  v0= u"您好，😊 UIUC加群建群小助手😊 为您服务～\n"
  v00=u"每天只能加3个群哦;\n" 
  vv0= u"回复 0 加北美母婴总群;北美CPA,REG天天刷题群\n"
  v1= u"回复 1 加UIUC会计、经济大家庭;北美信用卡爱好者;\n"
  v2= u"回复 2 加天天健身北美总群;加食神带飞群;\n"
  v3= u"回复 3 加UIUC ECE、CS找队友群;\n"
  v4= u"回复 4 加UIUC功能群:刷题面试;暑期留守儿童;\n"
  v5= u"回复 5 找朋友;UIUC手机family plan.\n";
  v6= u"回复 6 加UIUC租房群;玉米地小球俱乐部\n"
  v7= u"回复 7 加finding yingying群，大家一起帮助寻找~;UIUC天天carpool群\n"
  v8= u"回复 8 加UIUC行李保管中美互运群, UIUC统计群\n"
  v9= u"回复 9 加UIUC二手车群.UIUC宠物群🐱 🐶 🦆🐻  🐷 \n"
  v10= u"回复 10 加线上KTV开嗓🎙️北美总群;UIUC二手货群\n"
  v11= u"回复 11 加UI食神带飞群;17秋季香槟托儿所\n"
  v12= u"回复 12 加北美表情分享总群\n"
  vT =v0+v00+vv0+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12

  usersDict = {}
  admins =[]

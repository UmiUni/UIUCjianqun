# -*- coding: UTF-8 -*-
import datetime
def init():
  global admins
  global chatGroups
  global vT
  global v21
  global usersDict
  global ADMIN
  global previousDay

  chatGroups =[
  u'UIUC二手交易群',u'线上KTV',
  u'UIUC租房群3',u'UIUC内推找工作群2',
  u'UIUC二手车',u'UIUC宠物群',
  u'UIUC ECE大家庭',u'UIUC CS大家庭🌽',
  u'UIUC经济',u'北美信用卡',
  u'UIUC统计',u'玉米地小球',
  u'UIUC 心理系大家庭',u'UIUC 物理系大家庭',
  u'18春季香槟托儿',u'UI食神',
  u'北美表情分享','2018 UIUC往返芝加哥班车群',
  u'北美绿卡申请讨论总群','北美CPA',
  u'Pokemon Go北美交流总群',u'北美区块链技术交流总群',
  u'UIUC春假旅游出行2018',u'UIUC摄影爱好者',
  u'北美股市Trading技术交流总群1',u'UIUC面试算法找工作-九章算法群',
  u'UIUC暑期修学分交流群A',u'UIUC硕博新生必备干货群',
  u'UIUC本科新生必备干货群',
  u'小鹏汽车',
  u'UIUC 生活tips',
  u'UIUC2018留学就这样'
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
  v10= u"回复 9 加北美绿卡申请讨论总群;北美CPA,REG天天刷题群;\n"
  v11= u"回复 10 加Pokemon Go北美交流总群;北美区块链技术交流总群\n\n"
  v12= u"回复 11 加UIUC春假旅游出行自由组队群;UIUC摄影爱好者\n"
  v13= u"回复 12 加北美股市Trading技术交流总群1;加UIUC面试算法找工作-九章算法群\n"
  v14= u"回复 13 加UIUC暑期修学分交流群A; 加UIUC硕博新生必备干货群;\n"
  v15= u"回复 14 加UIUC本科新生必备干货群;\n"
  v16= u"回复 99 查看【北美加群小助手Jogchat.com】\n微信公众号二维码加纽约，硅谷，西雅图等群(无限次数)\n\n"
  v17= u"回复 100 加UIUC课程群小助手(无限次数)\n"
  v18= u"回复 101 加小鹏汽车5.6 UIUC校招群(无限次数)\n"
  v19= u"回复 102 加UIUC生活tips干货分享群(无限次数)\n"
  v20= u"回复 103 加 UIUC留学就这样 群(无限次数)\n"
  v21= u"微信自动加群群功能已关，请使用我们的网站【北美加群小助手joghcat.com】加入北美各地区Facebook群组。\n使用【umiuni.com】买卖香槟地区二手物品。谢谢😊\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17+v18+v19+v20
 
  
  vv0= u"回复 0 加北美母婴总群;北美CPA,REG天天刷题群\n"
  vv1= u'天天健身',u'UI食神',
  vv2= u"回复 2 加天天健身北美总群;加食神带飞群;\n"

  usersDict = {}
  admins =[]
  ADMIN = u'UIUC香槟加群小助手jogchat.com'
  previousDay = datetime.datetime.now().day

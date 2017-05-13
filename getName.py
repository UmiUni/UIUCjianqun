# -*- coding: UTF-8 -*-  
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
reload(sys)  
sys.setdefaultencoding('utf8')
freq = {}
usersDict = {}
itchat.auto_login(enableCmdQR=2,hotReload=True)
#UIUC CS大家庭  #@@07954b291e555b7ebcbc8a1c3110eadb7e77088935c0978ca14c9ee4db1829a4
#UIUC CS大家庭2 #@@e403e86ed7214a1d664ef7126dc430f36836ebcdbc4c9c32108b62c3b9ab86de 
#天天VIP @@6cdcfcb7dc00e7d546464ba702151143e1bf4aa9f72aa6e2559b86469e9a2481
#雷孙王 @@0515f86f31ec80ce4d4238a9ada8fdc0dd0900cc017f87c17df8ee49fb6d4663

#UIUC 万能总群2#@@d8b03e5ed3d34267d563c552a33af7b975e7375dd0a0499965292b2621fdee40
#UIUC 万能总群3#@@8bd479db2f43c6e2bf8ba14caf6cb2297dd0bf66235e88760457ef9d2d323dd2
#UIUC CS刷题小分队 @@6f46e7080085245f7a77f45fe3e1aced2aae89ce646be6fdacb5f21fc0497dcd
#天天刷题 @@b6a73f92b566e3c0c891ed90949b255db5ba52283d4c9376623c76b4e6cac7ac
def getName(chatroomName):
	itchat.get_chatrooms(update=True)
	cur_chatrooms = itchat.search_chatrooms(name=chatroomName)
	detailedChatroom = itchat.update_chatroom(cur_chatrooms[0]['UserName'], detailedMember=True)
	print(json.dumps(cur_chatrooms)+"\n")
	return cur_chatrooms[0]["UserName"]


if __name__ == "__main__":
	#getName(u'UIUC CS大家庭')
	#getName(u'UIUC CS刷题小分队')
	getName(u'天天刷题')


itchat.run() 

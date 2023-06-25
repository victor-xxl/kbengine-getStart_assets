
# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class FirstEntity(KBEngine.Entity):
	def __init__(self):
		#onEnter：在FirstEntity.def中自定义的函数，该函数用于告诉客户端，用户已进入服务器
		self.client.onEnter()
		pass 

	def say(self,id,content):
		#字符串格式化 ： %d:整数，%s：字符串
		INFO_MSG("Entity:[%d],Content:%s"%(id,content))
		#onSay函数在 FirstEntity.def中被定义
		self.allClients.onSay("Entity:[%d],Content:%s"%(id,content))
		pass	
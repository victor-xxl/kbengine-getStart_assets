# -*- coding: utf-8 -*-
from re import DEBUG
import KBEngine
from KBEDebug import *

class FirstEntity(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)

	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的cell部分。
		"""
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))
			
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		#self.destroy()
		self.destroyCellEntity()#销毁FirstEntity的cell部分
	
	#当cell被销毁后，kbe引擎层会调用base部分的onLoseCell函数
	def onLoseCell(self):
		DEBUG_MSG("Account[%i].onLoseCell:"%self.id)
		self.destroy()
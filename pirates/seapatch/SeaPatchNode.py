import math
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import directNotify

class SeaPatchNode(NodePath):
	notify = directNotify.newCategory('SeaPatchNode')
	
	def __init__(self, name, patchNode):
		NodePath.__init__(self, name)

	def setColorScale(self, colorScale):
		pass

	def setTwoSided(self, isTwoSided):
		pass

	def hide(self):
		pass

	def setBin(self, binStr, binVal):
		pass

	def setLightOff(self):
		pass

	def setLight(self, todMgrLights):
		pass

	def setWantReflect(self, wantReflect):
		pass

	def setWantColor(self, color):
		pass

	def collectGeometry(self):
		pass

	def resetProperties(self):
		pass
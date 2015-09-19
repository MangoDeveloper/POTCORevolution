from pandac.PandaModules import *
from pirates.world.WorldCreatorBase import WorldCreatorBase
from direct.directnotify.DirectNotifyGlobal import directNotify

class WorldManagerAI(WorldCreatorBase):
	notify = directNotify.newCategory('WorldManagerAI')

	def __init__(self, air, worldFile=None):
		WorldCreatorBase.__init__(self, air, worldFile)
		self.world = None

	def isObjectInCurrentGamePhase(self, obj):
		if not obj:
			return False

		return True

	def loadObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj = False, fileName = None, actualParentObj = None):
		WorldCreatorBase.loadObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj, fileName, actualParentObj)
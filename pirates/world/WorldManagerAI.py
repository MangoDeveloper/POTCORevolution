from pandac.PandaModules import *
from pirates.world.WorldCreatorBase import WorldCreatorBase
from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.world.DistributedIslandAI import DistributedIslandAI

class WorldManagerAI(WorldCreatorBase):
	notify = directNotify.newCategory('WorldManagerAI')

	def __init__(self, air, worldFile=None, gameZone=2000):
		WorldCreatorBase.__init__(self, air, worldFile)
		self.air = air

		self.world = None
		self.gameZone = gameZone

	def isObjectInCurrentGamePhase(self, obj):
		if not obj:
			return False

		return True

	def loadObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj = False, fileName = None, actualParentObj = None):
		objType = WorldCreatorBase.loadObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj, fileName, actualParentObj)

		if objType == 'Island':
			self.world = DistributedIslandAI(self.air, object['Visual']['Model'], object['Name'], objKey)
			self.world.generateWithRequired(zoneId=self.gameZone)

			if self.world:
				self.air.notify.info("Created island: %s" % (object['Name']))
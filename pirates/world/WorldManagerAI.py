from pandac.PandaModules import *
from pirates.world.WorldCreatorBase import WorldCreatorBase
from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.world.DistributedIslandAI import DistributedIslandAI
from pirates.world.DistributedOceanGridAI import DistributedOceanGridAI
from pirates.instance.DistributedInstanceWorldAI import DistributedInstanceWorldAI
import WorldGlobals

class WorldManagerAI(WorldCreatorBase):
	notify = directNotify.newCategory('WorldManagerAI')

	def __init__(self, air, worldFile=None, gameZone=WorldGlobals.ISLAND_GRID_STARTING_ZONE):
		WorldCreatorBase.__init__(self, air, worldFile)
		self.air = air

		self.world = None
		self.ocean = None
		self.gameZone = gameZone

	def isObjectInCurrentGamePhase(self, obj):
		if not obj:
			return False

		return True

	def loadObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj = False, fileName = None, actualParentObj = None):
		objType = WorldCreatorBase.loadObject(self, object, parent, parentUid, objKey, dynamic, parentIsObj, fileName, actualParentObj)

		if objType == 'Island':
			self.world = DistributedInstanceWorldAI(self.air)
			self.world.generateWithRequired(zoneId=self.gameZone)
			self.world.generateIslands(object['Visual']['Model'], object['Name'], objKey, object['Undockable'], self.gameZone)

			self.ocean = DistributedOceanGridAI(self.air)
			self.ocean.generateWithRequired(zoneId=self.gameZone)

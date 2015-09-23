from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI
from direct.directnotify import DirectNotifyGlobal
import WorldGlobals

class DistributedOceanGridAI(DistributedCartesianGridAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedOceanGridAI')

    def __init__(self, air):
        DistributedCartesianGridAI.__init__(self, air, WorldGlobals.OCEAN_GRID_STARTING_ZONE, WorldGlobals.OCEAN_GRID_SIZE, WorldGlobals.OCEAN_GRID_RADIUS, WorldGlobals.OCEAN_CELL_SIZE)
        self.parentingRules = ['ocean', '2000:10:20']

    def generate(self):
        DistributedCartesianGridAI.generate(self)

    def announceGenerate(self):
        DistributedCartesianGridAI.announceGenerate(self)

    def getParentingRules(self):
        return self.parentingRules

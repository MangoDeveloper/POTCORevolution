from pirates.world.DistributedGameAreaAI import DistributedGameAreaAI
from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI
from direct.directnotify import DirectNotifyGlobal

class DistributedGAInteriorAI(DistributedGameAreaAI, DistributedCartesianGridAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGAInteriorAI')

    def __init__(self, air, connectorId, modelPath, name):
        DistributedGameAreaAI.__init__(self, air, modelPath)
        DistributedCartesianGridAI.__init__(self, air, startingZone=self.air.allocateZone(), gridSize=10, gridRadius=10, cellWidth=20)
        self.connectorId = connectorId

    def generate(self):
        DistributedGameAreaAI.generate(self)
        
    def announceGenerate(self):
        DistributedGameAreaAI.announceGenerate(self)

    def getParentingRules(self):
        return ['', '']

    def getConnectorId(self):
        return self.connectorId
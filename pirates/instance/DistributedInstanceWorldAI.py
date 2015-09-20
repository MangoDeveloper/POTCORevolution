from direct.directnotify import DirectNotifyGlobal
from pirates.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from pirates.world.DistributedIslandAI import DistributedIslandAI

class DistributedInstanceWorldAI(DistributedInstanceBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInstanceWorldAI')

    def __init__(self, air, fileName=""):
        DistributedInstanceBaseAI.__init__(self, air, fileName)
        self.fileName = fileName

        self.activeIslands = set()

    def announceGenerate(self):
        DistributedInstanceBaseAI.announceGenerate(self)

    def generateIslands(self, islandModel, name, uid, isDockable, gameZone):
        self.island = DistributedIslandAI(self.air, islandModel, name, uid)
        self.island.generateWithRequired(zoneId=gameZone)
        self.island.d_setZoneSphereSize(rad0=1000, rad1=2000, rad2=3000)
        self.island.d_setIslandModel(islandModel=self.island.getIslandModel())
        self.island.d_setUndockable(undockable=isDockable)
        self.activeIslands.add(self.island)

        if self.island:
            self.air.notify.info("Created island: %s" % (name))
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from pirates.piratesbase import PiratesGlobals

class DistributedInstanceBaseAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInstanceBaseAI')

    def __init__(self, air, fileName, type=PiratesGlobals.INSTANCE_GENERIC):
        DistributedObjectAI.__init__(self, air)
        self.fileName = fileName
        self.type = type

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getParentingRules(self):
        return ['instance', '2000']

    def getFileName(self):
        return self.fileName

    def getType(self):
        return self.type

    def d_setSpawnInfo(self, xPos, yPos, zPos, h, spawnZone, parents):
        pass

    def requestSpawnLoc(self):
        pass

    def avatarDied(self):
        pass
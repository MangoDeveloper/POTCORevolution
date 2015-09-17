from direct.distributed.DistributedNodeAI import DistributedNodeAI
from direct.directnotify import DirectNotifyGlobal

class DistributedGameAreaAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGameAreaAI')

    def __init__(self, air, modelPath, name):
        DistributedNodeAI.__init__(self, air)
        self.modelPath = modelPath
        self.links = []
        self.uid = ''
        self.name = name

    def generate(self):
        DistributedNodeAI.generate(self)

    def announceGenerate(self):
        DistributedNodeAI.announceGenerate(self)

    def getModelPath(self):
        return self.modelPath

    def setLinks(self, links):
        self.links = links

    def getLinks(self):
        return self.links

    def setUniqueId(self, uid):
        self.uid = uid

    def d_setUniqueId(self, uid):
        self.sendUpdate('setUniqueId', [uid])

    def b_setUniqueId(self, uid):
        self.setUniqueId(uid)
        self.d_setUniqueId(uid)

    def getUniqueId(self):
        return self.uid

    def getName(self):
        return self.name

    def d_addSpawnTriggers(self, triggerSphere):
        pass

    def d_spawnNPC(self, spawnPtId, doId):
        pass

    def d_requestNPCRemoval(self, doId):
        pass
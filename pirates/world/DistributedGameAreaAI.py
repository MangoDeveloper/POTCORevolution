from direct.distributed.DistributedNodeAI import DistributedNodeAI
from direct.directnotify import DirectNotifyGlobal

class DistributedGameAreaAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGameAreaAI')
    
    def __init__(self, air, modelPath, name='', uid='', links=[]):
        DistributedNodeAI.__init__(self, air)
        self.modelPath = modelPath
        self.links = links
        self.uid = uid
        self.name = name

    def setUniqueId(self, uid):
        self.uid = uid

    def d_setUniqueId(self, uid):
        self.sendUpdate('setUniqueId', [uid])

    def b_setUniqueId(self, uid):
        self.setUniqueId(uid)
        self.d_setUniqueId(uid)

    def getUniqueId(self):
        return self.uid

    def setName(self, name):
        self.name = name

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def getName(self):
        return self.name

    def getModelPath(self):
        return self.modelPath

    def getLinks(self):
        return self.links

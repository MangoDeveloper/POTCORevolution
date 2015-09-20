from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI
from direct.directnotify import DirectNotifyGlobal

class DistributedOceanGridAI(DistributedCartesianGridAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedOceanGridAI')

    def __init__(self, air):
        DistributedCartesianGridAI.__init__(self, air, 2000, 1, 1, 1)
        self.parentingRules = ['ocean', '2000:10:20']

    def generate(self):
        DistributedCartesianGridAI.generate(self)

    def announceGenerate(self):
        DistributedCartesianGridAI.announceGenerate(self)

    def getParentingRules(self):
        return self.parentingRules
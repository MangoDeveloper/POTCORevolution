from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedPirateProfileMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPirateProfileMgrAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
    	DistributedObjectAI.generate(self)

    def announceGenerate(self):
    	DistributedObjectAI.announceGenerate(self)

    def requestAvatar(self, avId, doId):
    	pass #TODO: Get avatar info and send it!
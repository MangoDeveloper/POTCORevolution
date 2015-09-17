from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class PiratesTutorialManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('PiratesTutorialManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def requestTutorial(self): # Recv the client field and create a zone for it and send back as enterTutorial field.
    	self.sendUpdate('enterTutorial', [
    		self.air.allocateZone()])
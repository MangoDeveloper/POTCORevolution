from direct.directnotify import DirectNotifyGlobal
from pirates.distributed.DistributedInteractiveAI import *
from direct.distributed.DistributedObjectAI import *
from pirates.inventory import LootableAI
import FishingGlobals
from pandac.PandaModules import NodePath
from panda3d.core import *

class DistributedFishingSpotAI(DistributedInteractiveAI, LootableAI.LootableAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingSpotAI')
    
    def __init__(self, air):
        DistributedInteractiveAI.__init__(self, air)
    
    def handleInteract(self, avId, interactType, instant):
        #todo: Gotta add a check here to see if the player has any lures.
        pass

    def caughtFish(self, fishId, weight):
        pass

    def lostLure(self, lureId):
        pass
    
    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def setOceanOffset(self, offset):
        self.offset = offset

    def getOceanOffset(self):
        return self.offset

    def setOnABoat(self, isOnBoat):
        self.isOnBoat = isOnBoat

    def getOnABoat(self):
        return self.isOnBoat

    @classmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = DistributedInteractiveAI.makeFromObjectKey(cls, air, objKey, data)
        return obj
        
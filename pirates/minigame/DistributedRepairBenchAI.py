from direct.directnotify import DirectNotifyGlobal
from pirates.distributed.DistributedInteractiveAI import *
from DistributedRepairGameAI import DistributedRepairGameAI
from DistributedRepairGameBase import GAME_OPEN, GAME_ORDER, DIFFICULTY_MAX, ON_LAND

class DistributedRepairBenchAI(DistributedInteractiveAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedRepairBenchAI')
    
    def __init__(self, air):
        DistributedInteractiveAI.__init__(self, air)
        self.difficulty = 0
        
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty
        
    def getDifficulty(self):
        return self.difficulty
        
    def announceGenerate(self):
        DistributedInteractiveAI.announceGenerate(self)
        self.game = DistributedRepairGameAI(self.air)
        self.getParentObj().generateChild(self.game, self.zoneId)
    
    def handleInteract(self, avId, interactType, instant):
        self.game.sendUpdateToAvatarId(avId, 'start', [self.game.location])
        return ACCEPT | ACCEPT_SEND_UPDATE | ACCEPT_SET_AV
    
    @classmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = DistributedInteractiveAI.makeFromObjectKey(cls, air, objKey, data)
        obj.setDifficulty(int(data['difficulty']))
        return obj
    
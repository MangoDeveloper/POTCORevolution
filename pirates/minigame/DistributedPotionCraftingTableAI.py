from direct.directnotify.DirectNotifyGlobal import *

from pirates.distributed.DistributedInteractiveAI import *
from DistributedPotionGameAI import DistributedPotionGameAI

class DistributedPotionCraftingTableAI(DistributedInteractiveAI):
    notify = directNotify.newCategory('DistributedPotionCraftingTableAI')
    
    def __init__(self, air):
        DistributedInteractiveAI.__init__(self, air)
        self.games = {}
    
    def requestExit(self, avId=0):
        if not avId:
            avId = self.air.getAvatarIdFromSender()
            
        if avId in self.games:
            game = self.games.pop(avId)
            self.ignore(self.air.getAvatarExitEvent(avId))
            self.ignore(game.uniqueName('potiongame-exit'))
            self.sendUpdateToAvatarId(avId, 'rejectInteraction', [])
            game.requestDelete()
    
    def checkExit(self):
        self.requestExit()
    
    def handleInteract(self, avId, interactType, instant):
        if avId in self.games:
            return REJECT
            
        game = DistributedPotionGameAI(self.air, avId)
        game.generateWithRequiredAndId(self.air.allocateChannel(), self.doId, avId)
        self.games[avId] = game
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.requestExit, [avId])
        self.acceptOnce(game.uniqueName('potiongame-exit'), self.requestExit, [avId])
        return ACCEPT | ACCEPT_SEND_UPDATE
    
    @classmethod
    def makeFromObjectKey(cls, air, objKey, data):
        obj = DistributedInteractiveAI.makeFromObjectKey(cls, air, objKey, data)      
        return obj
        
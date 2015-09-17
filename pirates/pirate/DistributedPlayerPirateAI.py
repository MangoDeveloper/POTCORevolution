from direct.directnotify import DirectNotifyGlobal
from otp.avatar.DistributedPlayerAI import DistributedPlayerAI
from pirates.pirate.HumanDNA import HumanDNA
from pirates.battle.DistributedBattleAvatarAI import DistributedBattleAvatarAI
#from pirates.quest.DistributedQuestAvatar import DistributedQuestAvatar
from pandac.PandaModules import *

class DistributedPlayerPirateAI(DistributedPlayerAI, HumanDNA, DistributedBattleAvatarAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPlayerPirateAI')

    def __init__(self, air):
        DistributedPlayerAI.__init__(self, air)
        HumanDNA.__init__(self)
        DistributedBattleAvatarAI.__init__(self, air)
        self.avatarType = [0, 0, 0, 0]
        self.inInvasion = False
        self.skillEffects = []

    def generate(self):
        DistributedPlayerAI.generate(self)
        DistributedBattleAvatarAI.generate(self)

    def announceGenerate(self):
        DistributedPlayerAI.announceGenerate(self)
        DistributedBattleAvatarAI.announceGenerate(self)

    def setAvatarType(self, avatarType):
        self.avatarType = avatarType

    def getAvatarType(self):
        return self.avatarType

    def cueRegenerate(self):
    	self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'cueRegenerate', [])
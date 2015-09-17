from otp.distributed.DistributedDistrictAI import DistributedDistrictAI
from direct.directnotify import DirectNotifyGlobal

class PiratesDistrictAI(DistributedDistrictAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('PiratesDistrictAI')

    def __init__(self, air, mainWorld, shardType):
        DistributedDistrictAI.__init__(self, air)
        self.avatarCount = 0
        self.newAvatarCount = 0
        self.mainWorld = mainWorld
        self.shardType = shardType

    def generate(self):
    	DistributedDistrictAI.generate(self)
    	self.air.notify.info("Generated PiratesDistrictAI at %d" % (self.getDoId()))

    def announceGenerate(self):
        DistributedDistrictAI.announceGenerate(self)

    def setAvatarCount(self, avatarCount):
    	self.avatarCount = avatarCount

    def d_setAvatarCount(self, avatarCount):
    	self.sendUpdate('setAvatarCount', [
    		avatarCount])

    def b_setAvatarCount(self, avatarCount):
    	self.setAvatarCount(avatarCount)
    	self.d_setAvatarCount(avatarCount)

    def getAvatarCount(self):
    	return self.avatarCount

    def setNewAvatarCount(self, newAvatarCount):
    	self.newAvatarCount = newAvatarCount

    def d_setNewAvatarCount(self, newAvatarCount):
    	self.sendUpdate('setNewAvatarCount', [
    		newAvatarCount])

    def b_setNewAvatarCount(self, newAvatarCount):
    	self.setNewAvatarCount(newAvatarCount)
    	self.d_setNewAvatarCount(newAvatarCount)

    def getNewAvatarCount(self):
    	return self.newAvatarCount

    def setMainWorld(self, mainWorld):
    	self.mainWorld = mainWorld

    def getMainWorld(self):
    	return self.mainWorld

    def setShardType(self, shardType):
    	self.shardType = shardType

    def getShardType(self):
    	return self.shardType

    def d_setStats(self, avatarCount, newAvatarCount):
    	self.b_setAvatarCount(avatarCount)
    	self.b_setNewAvatarCount(newAvatarCount)

    def setPopulationLimits(self, popLow, popMax):
    	pass

from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from pirates.piratesbase import TODDefs
from pirates.piratesbase import TODGlobals
from direct.distributed.ClockDelta import *

class DistributedTimeOfDayManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTimeOfDayManagerAI')

    def __init__(self, air, isPaused, isJolly):
        DistributedObjectAI.__init__(self, air)
        self.isPaused = isPaused
        self.subList = []
        self.isJolly = isJolly
        self.tod = [0, 0, 0, 0]

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
    
    def setIsPaused(self, isPaused):
        self.isPaused = isPaused
	
    def getIsPaused(self):
        return self.isPaused
	
    def d_syncTOD(self, cycleType, cycleSpeed, startingNetTime, timeOffset):
        self.tod = [cycleType, cycleSpeed, startingNetTime, timeOffset]

        self.sendUpdate('syncTOD', [cycleType,
        	cycleSpeed,
        	startingNetTime,
        	timeOffset])
	
    def getSyncTOD(self):
        return self.tod
	
    def requestSync(self): #TODO: cycle type, check for halloween and jolly!
        self.d_syncTOD(cycleType=TODGlobals.TOD_REGULAR_CYCLE, cycleSpeed=1, startingNetTime=globalClockDelta.getRealNetworkTime(bits=32), timeOffset=0)
	
    def setEnvSubs(self, subList):
        self.subList = subList
	
    def getEnvSubs(self):
        return self.subList
	
    def setMoonPhaseChange(self, fromCurrent, startPhase, targetPhase, targetTime): #TODO!
        pass
	
    def getMoonPhaseChange(self):
        return [0, 0, 0, 0]
	
    def setMoonJolly(self, isJolly):
        self.isJolly = isJolly
	
    def d_setMoonJolly(self, isJolly):
        self.sendUpdate('setMoonJolly', [
            isJolly])
	
    def b_setMoonJolly(self, isJolly):
        self.setMoonJolly(isJolly)
        self.d_setMoonJolly(isJolly)
	
    def getMoonJolly(self):
        return self.isJolly

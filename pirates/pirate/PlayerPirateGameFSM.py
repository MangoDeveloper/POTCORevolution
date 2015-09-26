# File: P (Python 2.4)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from pirates.destructibles import ShatterableSkeleton
from pirates.pirate.BattleAvatarGameFSM import BattleAvatarGameFSM

class PlayerPirateGameFSM(BattleAvatarGameFSM):
    
    def __init__(self, av, fsmName = 'PlayerPirateGameFSM'):
        BattleAvatarGameFSM.__init__(self, av, fsmName)
    
    def enterDeath(self, extraArgs = []):
        BattleAvatarGameFSM.enterDeath(self, extraArgs)
    
    def exitDeath(self):
        BattleAvatarGameFSM.exitDeath(self)

    def enterOff(self, extraArgs = []):
        BattleAvatarGameFSM.enterOff(self, extraArgs)

    def enterLandRoam(self, extraArgs = []):
        BattleAvatarGameFSM.enterLandRoam(self, extraArgs)

    def exitLandRoam(self):
        BattleAvatarGameFSM.exitLandRoam(self)

    def enterSpawn(self, extraArgs = []):
        BattleAvatarGameFSM.enterSpawn(self, extraArgs)

    def exitSpawn(self):
        BattleAvatarGameFSM.exitSpawn(self)


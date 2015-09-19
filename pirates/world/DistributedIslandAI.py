from pirates.world.DistributedGameAreaAI import DistributedGameAreaAI
from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI
from pirates.battle.Teamable import Teamable
from direct.directnotify import DirectNotifyGlobal

class DistributedIslandAI(DistributedGameAreaAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedIslandAI')

    def __init__(self, air):
        DistributedGameAreaAI.__init__(self, air)
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal

class CentralLoggerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('CentralLoggerUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
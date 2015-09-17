# STUB
# NO BASE CLASS WAS FOUND!
# IT MEANS THAT THIS FILE HAD NO DEF
# IN PIRATES.DC WHEN AI-GEN WAS RUN!

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class LootableAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('LootableAI')
        
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    # startLooting(PlunderListItem [], int8, uint8, bool)

    # stopLooting()

    # doneTaking() airecv clsend

    # requestItem(PlunderItemLocationInfo) airecv clsend

    # requestItems(PlunderItemInfo []) airecv clsend



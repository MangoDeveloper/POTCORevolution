from direct.distributed.DistributedObjectAI import DistributedObjectAI
from DistributedRepairGameBase import *

'''
dclass DistributedRepairGame : DistributedObject {
  start(uint8(0-5));
  stop();
  requestMincroGame(uint8(0-5)) airecv clsend;
  requestMincroGameResponse(bool, uint8);
  reportMincroGameProgress(uint8(0-5), int8, uint8) clsend airecv;
  setMincroGameProgress(uint8(0-5), int8);
  setAllMincroGameProgress(int8 []);
  setAvIds2CurrentGameList(uint8(0-5) [0-5], uint32 [0-5]);
  reportMincroGameScore(uint8(0-5), uint32) clsend airecv;
  cycleComplete(uint8, uint32 [0-5], uint16 [0-5], uint32);
  shipDamaged(bool, uint8);
  setGoldBonus(uint32) broadcast;
};
'''

class DistributedRepairGameAI(DistributedObjectAI, DistributedRepairGameBase):
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        DistributedRepairGameBase.__init__(self)
        
    def requestMincroGame(self, game):
        print 'requestMincroGame', game
        
    def reportMincroGameProgress(self, a, b, c):
        print 'reportMincroGameProgress', a, b, c

    def reportMincroGameScore(self, a, b):
        print 'reportMincroGameScore', a, b

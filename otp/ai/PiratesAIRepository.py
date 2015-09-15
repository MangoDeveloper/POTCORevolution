from pirates.distributed.PiratesInternalRepository import PiratesInternalRepository
from direct.distributed.PyDatagram import *
from otp.distributed.OtpDoGlobals import *
from pandac.PandaModules import *

class PiratesAIRepository(PiratesInternalRepository):
    
    def __init__(self, baseChannel, stateServerChannel, districtName):
        PiratesInternalRepository.__init__(
            self, baseChannel, stateServerChannel, dcSuffix='AI')

        self.notify.setInfo(True)
        self.districtName = districtName
        self.zoneAllocator = UniqueIdAllocator(ToontownGlobals.DynamicZonesBegin,
                                                ToontownGlobals.DynamicZonesEnd)
        self.zoneDataStore = AIZoneDataStore()

    def createManagers(self):
        pass

    def handleConnected(self):
        self.districtId = self.allocateChannel()
        #self.notify.info('Creating ToontownDistrictAI(%d)...' % self.districtId)
        #self.distributedDistrict = ToontownDistrictAI(self)
        #self.distributedDistrict.setName(self.districtName)
        #self.distributedDistrict.generateWithRequiredAndId(
        #    self.districtId, self.getGameDoId(), 2)
        #self.notify.info('Claiming ownership of channel ID: %d...' % self.districtId)
        #self.claimOwnership(self.districtId)

        self.notify.info('Creating managers...')
        self.createManagers()

        self.notify.info('Making district available...')
        self.distributedDistrict.b_setAvailable(1)
        self.notify.info('Done.')

    def claimOwnership(self, channelId):
        datagram = PyDatagram()
        datagram.addServerHeader(channelId, self.ourChannel, STATESERVER_OBJECT_SET_AI)
        datagram.addChannel(self.ourChannel)
        self.send(datagram)

    def incrementPopulation(self):
        pass
        #self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() + 1)

    def decrementPopulation(self):
        pass
        #self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() - 1)

    def allocateZone(self):
        return self.zoneAllocator.allocate()

    def deallocateZone(self, zone):
        self.zoneAllocator.free(zone)

    def getZoneDataStore(self):
        return self.zoneDataStore

    def getTrackClsends(self):
        return self.wantTrackClsends

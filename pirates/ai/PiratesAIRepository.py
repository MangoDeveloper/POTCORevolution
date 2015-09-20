from pirates.distributed.PiratesInternalRepository import PiratesInternalRepository
from pirates.distributed.PiratesDistrictAI import PiratesDistrictAI
from pirates.distributed.DistributedPopulationTrackerAI import DistributedPopulationTrackerAI
from pirates.piratesbase.DistributedTimeOfDayManagerAI import DistributedTimeOfDayManagerAI
from pirates.tutorial.DistributedPiratesTutorialAI import DistributedPiratesTutorialAI
from pirates.world.DistributedJailInteriorAI import DistributedJailInteriorAI
from pirates.piratesgui.DistributedPirateProfileMgrAI import DistributedPirateProfileMgrAI
from pirates.world.WorldManagerAI import WorldManagerAI
from pirates.piratesbase import PiratesGlobals
from direct.distributed.PyDatagram import *
from otp.distributed.OtpDoGlobals import *
from pandac.PandaModules import *

class PiratesAIRepository(PiratesInternalRepository):
    
    def __init__(self, baseChannel, stateServerChannel, districtName):
        PiratesInternalRepository.__init__(
            self, baseChannel, stateServerChannel, dcSuffix='AI')

        self.notify.setInfo(True)
        self.districtName = districtName
        self.zoneAllocator = UniqueIdAllocator(PiratesGlobals.DynamicZonesBegin,
                                                PiratesGlobals.DynamicZonesEnd)

    def createManagers(self):
        self.districtStats = DistributedPopulationTrackerAI(self, populationMin=100, populationMax=700)
        self.districtStats.generateWithRequiredAndId(
            self.allocateChannel(), self.getGameDoId(), 3)
        self.districtStats.b_setShardId(self.distributedDistrict.getDoId())

        self.DistributedTimeOfDayManager = DistributedTimeOfDayManagerAI(self, isPaused=False, isJolly=0)
        self.DistributedTimeOfDayManager.generateWithRequired(2)

        self.DistributedPirateProfileMgr = DistributedPirateProfileMgrAI(self)
        self.DistributedPirateProfileMgr.generateWithRequired(2)

        self.worldManager = WorldManagerAI(self) #TODO: Generate the rest of the islands!
        self.portRoyal = self.worldManager.loadObjectsFromFile(filename="PortRoyalWorld.py")
        self.tortuga = self.worldManager.loadObjectsFromFile(filename="TortugaWorld.py")
        self.islaCangrejos = self.worldManager.loadObjectsFromFile(filename="CangrejosIsland.py")
        self.kingsHead = self.worldManager.loadObjectsFromFile(filename="KingsheadWorld.py")
        self.cuba = self.worldManager.loadObjectsFromFile(filename="CubaWorld.py")
        self.islaRumrunner = self.worldManager.loadObjectsFromFile(filename="RumrunnerWorld.py")
        self.anvilIsland = self.worldManager.loadObjectsFromFile(filename="AnvilIsland.py")
        self.islaTormenta = self.worldManager.loadObjectsFromFile(filename="TormentaIsland.py")

        # Tutorial:
        self.rambleShackIsland = self.worldManager.loadObjectsFromFile(filename="RambleshackWorld.py")

        self.tutorialObject = DistributedPiratesTutorialAI(self)
        self.tutorialObject.generateWithRequired(2)

    def handleConnected(self):
        self.districtId = self.allocateChannel()
        self.distributedDistrict = PiratesDistrictAI(self, mainWorld="PortRoyalWorld.py", shardType=PiratesGlobals.SHARD_MAIN)
        self.distributedDistrict.setName(self.districtName)
        self.distributedDistrict.generateWithRequiredAndId(
            self.districtId, self.getGameDoId(), 2)
        self.notify.info('Claiming ownership of channel ID: %d...' % self.districtId)
        self.claimOwnership(self.districtId)

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
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() + 1)

    def decrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() - 1)

    def allocateZone(self):
        return self.zoneAllocator.allocate()

    def deallocateZone(self, zone):
        self.zoneAllocator.free(zone)
from direct.distributed.DistributedCartesianGridAI import DistributedCartesianGridAI
from pirates.world.DistributedGameAreaAI import DistributedGameAreaAI
from direct.directnotify import DirectNotifyGlobal
from pirates.battle.Teamable import Teamable
import WorldGlobals

class DistributedIslandAI(DistributedCartesianGridAI, DistributedGameAreaAI, Teamable):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedIslandAI')
    
    def __init__(self, air, islandModel, name, uid):
        DistributedGameAreaAI.__init__(self, air, islandModel, name, uid)
        DistributedCartesianGridAI.__init__(self, air, WorldGlobals.ISLAND_GRID_STARTING_ZONE, WorldGlobals.ISLAND_GRID_SIZE, WorldGlobals.ISLAND_GRID_RADIUS, WorldGlobals.ISLAND_CELL_SIZE)
        Teamable.__init__(self)

        self.parentingRules = ['island', '2000:10:20']
        self.islandTransform = [1, 1, 1, 1]
        self.zoneSphereSize = [1, 1, 1]
        self.zoneSphereCenter = [1, 1]

        self.islandModel = islandModel

        self.undockable = True
        self.portCollisionSpheres = []
        self.feastFireEnabled = False
        self.fireworkShowEnabled = [False, 0]

    def generate(self):
        DistributedGameAreaAI.generate(self)
        DistributedCartesianGridAI.generate(self)

    def announceGenerate(self):
        DistributedGameAreaAI.announceGenerate(self)
        DistributedCartesianGridAI.announceGenerate(self)

    def setParentingRules(self, rule1, rule2):
        self.parentingRules = [rule1, rule2]

    def d_setParentingRules(self, rule1, rule2):
        self.sendUpdate('setParentingRules', [
            rule1,
            rule2])

    def b_setParentingRules(self, rule1, rule2):
        self.setParentingRules(rule1, rule2)
        self.d_setParentingRules(rule1, rule2)

    def getParentingRules(self):
        return self.parentingRules

    def setIslandTransform(self, x, y, z, h):
        self.islandTransform = [x, y, z, h]

    def d_setIslandTransform(self, x, y, z, h):
        self.sendUpdate('setIslandTransform', [
            x,
            y,
            z,
            h])

    def b_setIslandTransform(self, x, y, z, h):
        self.setIslandTransform(x, y, z, h)
        self.d_setIslandTransform(x, y, z, h)

    def getIslandTransform(self):
        return self.islandTransform

    def setZoneSphereSize(self, rad0, rad1, rad2):
        self.zoneSphereSize = [rad0, rad1, rad2]

    def d_setZoneSphereSize(self, rad0, rad1, rad2):
        self.sendUpdate('setZoneSphereSize', [
            rad0,
            rad1,
            rad2])

    def b_setZoneSphereSize(self, rad0, rad1, rad2):
        self.setZoneSphereSize(rad0, rad1, rad2)
        self.b_setZoneSphereSize(rad0, rad1, rad2)

    def getZoneSphereSize(self):
        return self.zoneSphereSize

    def setZoneSphereCenter(self, todo0, todo1):
        pass

    def d_setZoneSphereCenter(self, todo0, todo1):
        pass

    def b_setZoneSphereCenter(self, todo0, todo1):
        pass

    def getZoneSphereCenter(self):
        return self.zoneSphereCenter

    def setIslandModel(self, islandModel):
        self.islandModel = islandModel

    def d_setIslandModel(self, islandModel):
        self.sendUpdate('setIslandModel', [
            islandModel])

    def b_setIslandModel(self, islandModel):
        self.setIslandModel(islandModel)
        self.d_setIslandModel(islandModel)

    def getIslandModel(self):
        return self.islandModel

    def setUndockable(self, undockable):
        self.undockable = undockable

    def d_setUndockable(self, undockable):
        self.sendUpdate('setUndockable', [
            undockable])

    def b_setUndockable(self, undockable):
        self.setUndockable(undockable)
        self.d_setUndockable(undockable)

    def getUndockable(self):
        return self.undockable

    def setPortCollisionSpheres(self, todo0):
        pass

    def d_setPortCollisionSpheres(self, todo0):
        pass

    def b_setPortCollisionSpheres(self, todo0):
        pass

    def getPortCollisionSpheres(self):
        return self.portCollisionSpheres

    def makeLavaErupt(self):
        self.sendUpdate('makeLavaErupt', [])

    def requestEntryToIsland(self):
        pass

    def deniedEntryToIsland(self):
        self.sendUpdate('deniedEntryToIsland', [])

    def setFeastFireEnabled(self, todo0):
        pass

    def d_setFeastFireEnabled(self, todo0):
        pass

    def b_setFeastFireEnabled(self, todo0):
        pass

    def getFeastFireEnabled(self):
        return self.feastFireEnabled

    def setFireworkShowEnabled(self, todo0, todo1):
        pass

    def d_setFireworkShowEnabled(self, todo0, todo1):
        pass

    def b_setFireworkShowEnabled(self, todo0, todo1):
        pass

    def getFireworkShowEnabled(self):
        return self.fireworkShowEnabled

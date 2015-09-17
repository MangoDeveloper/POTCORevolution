from pirates.world.DistributedGAInteriorAI import DistributedGAInteriorAI
from direct.directnotify import DirectNotifyGlobal

class DistributedJailInteriorAI(DistributedGAInteriorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedJailInteriorAI')

    def __init__(self, air):
        DistributedGAInteriorAI.__init__(self, air, connectorId=0, modelPath="pirates/leveleditor/worldData/make_a_pirate_jail.py", name="MakeAPirate_Jail")

    def generate(self):
        DistributedGAInteriorAI.generate(self)

    def announceGenerate(self):
        DistributedGAInteriorAI.announceGenerate(self)
    
    def avatarAlreadyInJail(self):
        pass
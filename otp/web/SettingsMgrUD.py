from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal
import SettingsMgrBase

class SettingsMgrUD(DistributedObjectGlobalUD, SettingsMgrBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('SettingsMgrUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def announceGenerate(self):
    	DistributedObjectGlobalUD.announceGenerate(self)
    	SettingsMgrBase.SettingsMgrBase.announceGenerate(self)

    def requestAllChangedSettings(self):
    	pass #Overidden by subclass.

    def d_settingChange(self, settingName, valueStr):
    	self.sendUpdate('settingChange', [
    		settingName,
    		valueStr])
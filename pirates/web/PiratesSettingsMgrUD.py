from otp.web.SettingsMgrUD import SettingsMgrUD
from direct.directnotify import DirectNotifyGlobal
from PiratesSettingsMgrBase import PiratesSettingsMgrBase

class PiratesSettingsMgrUD(SettingsMgrUD, PiratesSettingsMgrBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('PiratesSettingsMgrUD')

    def __init__(self, air):
        SettingsMgrUD.__init__(self, air)

    def announceGenerate(self):
    	SettingsMgrUD.announceGenerate(self)

    def requestAllChangedSettings(self):
    	PiratesSettingsMgrBase._initSettings()
    	# TODO: SettingsMgrUD.d_settingChange()!
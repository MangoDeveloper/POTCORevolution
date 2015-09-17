from direct.directnotify import DirectNotifyGlobal
from otp.friends.PlayerFriendsManagerUD import PlayerFriendsManagerUD

class PCPlayerFriendsManagerUD(PlayerFriendsManagerUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("PCPlayerFriendsManagerUD")

    def updatePlayerFriend(self, todo0, todo1, todo2):
        pass

    def removePlayerFriend(self, todo0):
        pass

    def setShipState(self, todo0):
        pass

    def getShipState(self, todo0):
        pass

    def getShipId2State(self, todo0):
        pass

    def getShipId(self, todo0):
        pass

    def setBandId(self, todo0, todo1, todo2):
        pass

    def getBandId(self, todo0):
        pass

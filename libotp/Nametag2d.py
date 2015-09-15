from Nametag import *
from MarginPopup import *
from pandac.PandaModules import *
import math

class Nametag2d(Nametag, MarginPopup):
    SCALE_2D = 0.25
    CHAT_ALPHA = 0.5
    ARROW_OFFSET = -1.0
    ARROW_SCALE = 1.5

    def __init__(self):
        Nametag.__init__(self)
        MarginPopup.__init__(self)
        self.contents = self.CName | self.CSpeech
        self.chatWordWrap = 7.5
        self.arrow = None
        self.innerNP.setScale(self.SCALE_2D)
        return

    def showBalloon(self, balloon, text):
        text = '%s: %s' % (self.displayName, text)
        Nametag.showBalloon(self, balloon, text)
        balloon = NodePath.anyPath(self).find('*/balloon')
        text = balloon.find('**/+TextNode')
        t = text.node()
        left, right, bottom, top = t.getFrameActual()
        center = self.innerNP.getRelativePoint(text, ((left + right) / 2.0, 0, (bottom + top) / 2.0))
        balloon.setPos(balloon, -center)
        self.setPriority(1)
        if self.arrow is not None:
            self.arrow.removeNode()
        self.arrow = None
        return

    def showName(self):
        Nametag.showName(self)
        self.setPriority(0)
        t = self.innerNP.find('**/+TextNode')
        arrowZ = self.ARROW_OFFSET + t.node().getBottom()
        self.arrow = NametagGlobals.arrowModel.copyTo(self.innerNP)
        self.arrow.setZ(arrowZ)
        self.arrow.setScale(self.ARROW_SCALE)
        if self.colorCode == CCSuit:
            self.arrow.setColor(0.8, 0.4, 0.0, 1.0)
        else:
            self.arrow.setColor(self.nameFg)

    def update(self):
        Nametag.update(self)
        self.considerUpdateClickRegion()

    def marginVisibilityChanged(self):
        self.considerUpdateClickRegion()

    def considerUpdateClickRegion(self):
        if self.isDisplayed():
            self.updateClickRegion(-1, 1, -1, 1)

    def tick(self):
        if not self.isDisplayed() or self.arrow is None:
            return
        elif self.avatar is None:
            return
        else:
            cam = NametagGlobals.camera or base.cam
            toon = NametagGlobals.toon or cam
            location = self.avatar.getPos(toon)
            rotation = toon.getQuat(cam)
            camSpacePos = rotation.xform(location)
            arrowRadians = math.atan2(camSpacePos[0], camSpacePos[1])
            arrowDegrees = arrowRadians / math.pi * 180
            self.arrow.setR(arrowDegrees - 90)
            return

    def getSpeechBalloon(self):
        return NametagGlobals.speechBalloon2d

    def getThoughtBalloon(self):
        return NametagGlobals.thoughtBalloon2d
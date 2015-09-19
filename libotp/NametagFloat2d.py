from Nametag3d import *

class NametagFloat2d(Nametag3d):
    WANT_DYNAMIC_SCALING = False
    SCALING_FACTOR = 1.0
    SHOULD_BILLBOARD = False
    
    def __init__(self):
		Nametag3d.__init__(self)

    def upcastToPandaNode(self):
    	return self.icon

    def setActive(self, active):
    	self.active = active
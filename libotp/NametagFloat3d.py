from Nametag3d import *

class NametagFloat3d(Nametag3d):
    WANT_DYNAMIC_SCALING = False
    SCALING_FACTOR = 1.0
    SHOULD_BILLBOARD = True

    def __init__(self):
    	Nametag3d.__init__(self)

    def upcastToPandaNode(self):
    	return self.icon
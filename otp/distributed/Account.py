# File: o (Python 2.4)

from direct.distributed import DistributedObject

class Account(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)



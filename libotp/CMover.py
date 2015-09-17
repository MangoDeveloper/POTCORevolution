from otp.movement.PyVec3 import PyVec3

class CMover:
	def __init__(self, objNodePath, fwdSpeed, rotSpeed):
		self.rotSpeed = rotSpeed
		self.fwdSpeed = fwdSpeed
		self.impulses = [None]
		self.activeImpluses = set()
	
	def setFwdSpeed(self, rotSpeed):
		self.fwdSpeed = fwdSpeed
	
	def setRotSpeed(self, rotSpeed):
		self.rotSpeed = rotSpeed
	
	def getFwdSpeed(self):
		return self.fwdSpeed
	
	def getRotSpeed(self):
		return self.rotSpeed
	
	def indexImpulses(self):
		return self.impulses.index(None)
	
	def addCImpulse(self, name, impulse):
		self.indexImpulses()
		self.impulses[name] = impulse
	
	def removeCImpulse(self, name):
		self.impulses[name] = None
		for impulse in self.impulses:
			del impulse
	
	def processCImpulses(self, dt):
		pass #TODO!
	
	def integrate(self):
		for impulse in self.impulses:
			self.activeImpluses.add(impulse)
			

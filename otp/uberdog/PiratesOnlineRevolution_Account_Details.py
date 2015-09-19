from pandac.PandaModules import *

class PiratesOnlineRevolution_Account_Details:

	def __init__(self, accountName, accountAccess):
		self.accountName = accountName
		self.accountAccess = accountAccess

	def getAccountName(self):
		return self.accountName

	def getAccountAccess(self):
		return self.accountAccess

	def canOpenChatAndNotGetBooted(self):
		return base.config.GetBool('can-open-chat-and-not-get-booted', True)

	def WLChatEnabled(self):
		return base.config.GetBool('wl-chat-enabled', True)
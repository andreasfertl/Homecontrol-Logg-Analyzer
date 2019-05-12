import enum 

class LogMessageType(enum.Enum):
	NotToHandle = 0
	BTDevice = 1
	Temperature = 2
	Humidity = 3


class Entrie:
	def __init__(self, type, date, value):
		self.type = type
		self.date = date
		self.value = value


class LoggEntries:
	def __init__(self):
		self.entries = []

	def addEntry(self, entrie):
		self.entries.append(entrie)

#TCPManager.cpp Line: 225 2019-05-13 16:33:44:643 Sending a MANDOLYN_SENSOR MESSAGE ID: 12 Temp: 22.2 Humidity: 14

class TemperatureHumidity:
	def __init__(self, name:int, temperature:float, humidity:int):
		self.name = name
		self.temperature = temperature
		self.humidity = humidity

	def __init__(self, fromString:str):
		self.name = readValue('ID:', fromString)
		self.temperature = readValue('Temp:', fromString)
		self.humidity = readValue('Humidity:', fromString)

	def ToString(self):
		return "ID: {}, Temperature: {}, Humidity: {}".format(self.name, self.temperature, self.humidity)

def findPostion(line, string):
    resultNo = line.find(string)
    if resultNo > 0:
        resultNo = resultNo -1 #skip ' ' 
    return resultNo

def readValue(identifier, line):
    position = line.find(identifier)
    skip = position + len(identifier) + 1

    if position > 0:
        lengthOfLine = len(line)
        if lengthOfLine > 1 and skip < lengthOfLine:
            partofString = line[skip:lengthOfLine-1] 
            value = partofString.partition(" ")[0]
            return value
    return ''



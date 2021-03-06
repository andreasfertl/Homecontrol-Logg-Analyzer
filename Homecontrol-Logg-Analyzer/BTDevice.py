class BTDevice:
	def __init__(self, name, inRange):
		self.name = name
		self.inRange = inRange

	def ToString(self):
		return "Name: {}, In Range: {}".format(self.inRange, self.name)

def readInRange(line) -> bool:
	result = line.find('Yes in Range') 
	return result != -1

def findPostion(line, string):
    resultNo = line.find(string)
    if resultNo > 0:
        resultNo = resultNo -1 #skip ' ' 
    return resultNo

def readName(line):
	#BTDevice Watch von Andreas Yes in Range
	#BTDevice Apple Watch von Andreas No Not in Range

    btDeviceIdentifier = 'BTDevice'
    btDeviceIdentifierLength = len(btDeviceIdentifier)

    resultBTDevicePostion = line.find(btDeviceIdentifier)
    skipBTDevice = resultBTDevicePostion + btDeviceIdentifierLength + 1
    resultYes = findPostion(line, 'Yes in Range')
    resultNo = findPostion(line, 'No Not in Range')

    if resultBTDevicePostion > 0:
        if resultYes > skipBTDevice:
            return line[skipBTDevice:resultYes]
        elif resultNo > skipBTDevice:
            return line[skipBTDevice:resultNo]
    return ''

def readBTDevice(line) -> BTDevice:
	return BTDevice(readName(line), readInRange(line))


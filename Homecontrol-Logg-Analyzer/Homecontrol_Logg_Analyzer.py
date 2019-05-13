import sys  
import re
import datetime
from BTDevice import *
from LoggEntries import *
from PlotLoggEntries import *

def filterLines(line):
	if line.find('in Range') != -1:
		return LogMessageType.BTDevice
	#elif line.find('MANDOLYN_SENSOR') != -1:
	#	return True
	else:
		return LogMessageType.NotToHandle

def findDateAndTimeFrom(line) -> datetime.datetime:
	match = re.search(r'(\d+-\d+-\d+ \d+:\d+:\d+)',line)
	if match.endpos >= 1:
		try:
			dateAndTime = match.group(1)
			dt = datetime.datetime.strptime(dateAndTime, "%Y-%m-%d %H:%M:%S")
			return dt
		except:
			return datetime.datetime.now()
	else:
		return datetime.datetime.now()

def handleType(type, date, line) -> Entrie:
	if type == LogMessageType.BTDevice:
		return Entrie(type, date, readBTDevice(line))
	else:
		return None



def readFileTo(filename, loggEntries):
	with open(filename, mode='r') as fp:  
		line = fp.readline()
		cnt = 1

		while line:
			typeOfEntry = filterLines(line)
			if  typeOfEntry != LogMessageType.NotToHandle:
				entrie = handleType(typeOfEntry, findDateAndTimeFrom(line), line)
				if entrie != None:
					loggEntries.addEntry(entrie)
			else:
				pass
			line = fp.readline()
			cnt = cnt + 1 


def main():
	#filename = sys.argv[1]
    loggEntries = LoggEntries()
    readFileTo('c:\LinuxClientLog.txt', loggEntries)

    plotLoggEntries(loggEntries)

    for element in loggEntries.entries:
        print("Type: {}, Timestamp: {}, {}".format(element.type, element.date, element.value.ToString()))


if __name__ == '__main__':
    main()



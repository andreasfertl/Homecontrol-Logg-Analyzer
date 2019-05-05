import sys  
import re
import datetime
import enum 
  
# creating enumerations using class 
class LogMessageType(enum.Enum):
	NotToHandle = 0
	BTDevice = 1
	Temperature = 2
	Humidity = 3


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



def readFile(filename):
	with open(filename, mode='r') as fp:  
		line = fp.readline()
		cnt = 1

		while line:
			if filterLines(line) != LogMessageType.NotToHandle:
				dt = findDateAndTimeFrom(line)
				print("Line {}: {}".format(cnt, line.strip()))
				print(dt.year)
			else:
				pass
			line = fp.readline()
			cnt = cnt + 1 



def main():
	#filename = sys.argv[1]
	readFile('c:\LinuxClientLog.txt')


if __name__ == '__main__':
    main()



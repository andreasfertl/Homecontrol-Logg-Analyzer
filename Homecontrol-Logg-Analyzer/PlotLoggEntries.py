import matplotlib.pyplot as plt
from LoggEntries import*

class plotElement:

    def __init__(self):
        self.date: str = []
        self.value: int  = []
        self.value2: int  = []

    def appendElement(self, date, value, value2 = None):
        self.date.append(date)
        self.value.append(value)
        if value2 is not None:
            self.value2.append(value2)


class plotElements:

    def __init__(self, name, date, value, value2 = None):
        self.name = name
        self.elements = plotElement()
        self.elements.appendElement(date, value, value2)

    
def findName(plotElements, name):
    for index, element in enumerate(plotElements):
        if element.name == name:
            return index
    return -1

def plotLoggEntries(loggEntries):
    toPlot: plotElements() = []

    for element in loggEntries.entries:
        if element.type == LogMessageType.BTDevice:
            index = findName(toPlot, element.value.name)
            if index != -1: #do we have it from before? No need to add
                toPlot[index].elements.appendElement(element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.inRange)
            else:
                toPlot.append(plotElements(element.value.name, element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.inRange))
        elif element.type == LogMessageType.TemperatureAndHumidity:
            index = findName(toPlot, element.value.name)
            if index != -1: #do we have it from before? No need to add
                toPlot[index].elements.appendElement(element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.temperature, element.value.humidity)
            else:
                toPlot.append(plotElements(element.value.name, element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.temperature, element.value.humidity))

    for element in toPlot:
        plt.plot(element.elements.date, element.elements.value)
        plt.xlabel('Date')
        plt.ylabel(element.name)
        plt.show()
        #show potential second value
        if len(element.elements.value2) > 0:
            plt.plot(element.elements.date, element.elements.value2)
            plt.xlabel('Date')
            plt.ylabel(element.name)
            plt.show()



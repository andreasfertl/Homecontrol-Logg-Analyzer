import matplotlib.pyplot as plt

class plotElement:

    def __init__(self):
        self.date: str = []
        self.value: bool  = []

    def appendElement(self, date, value):
        self.date.append(date)
        self.value.append(value)


class plotElements:

    def __init__(self, name, date, value):
        self.name = name
        self.elements = plotElement()
        self.elements.appendElement(date, value)

    
def findName(plotElements, name):
    for index, element in enumerate(plotElements):
        if element.name == name:
            return index
    return -1

def plotLoggEntries(loggEntries):
    toPlot: plotElements() = []

    for element in loggEntries.entries:
        index = findName(toPlot, element.value.name)
        if index != -1: #do we have it from before? No need to add
            toPlot[index].elements.appendElement(element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.inRange)
        else:
            toPlot.append(plotElements(element.value.name, element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.inRange))

    for element in toPlot:
        plt.plot(element.elements.date, element.elements.value)
        plt.xlabel('Date')
        plt.ylabel('AtHome: ' + element.name)
        plt.show()

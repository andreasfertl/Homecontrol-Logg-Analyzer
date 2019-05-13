import matplotlib.pyplot as plt

class plotElement:
    date: str = []
    value: bool  = []

    def appendElement(self, date, value):
        self.date.append(date)
        self.value.append(value)


class plotElements:
    name: str
    elements: plotElement

    def __init__(self, name):
        self.name = name
        self.elements = plotElement()

    
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
            toPlot.append(plotElements(element.value.name))
            #index of last element is accessable by -1
            toPlot[-1].elements.appendElement(element.date.strftime("%Y-%m-%d %H:%M:%S"), element.value.inRange)

    for element in toPlot:
        plt.plot(element.elements.date, element.elements.value)
        plt.xlabel('Date')
        plt.ylabel('AtHome: ' + element.name)
        plt.show()

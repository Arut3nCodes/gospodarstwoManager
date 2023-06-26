from Entry import Entry
from operator import attrgetter
import datetime as dt

class EntryList:
    def __init__(self, entryList=[]):
        self.entryList : list[Entry] = entryList
        self.autonum = max(entryList, key=attrgetter('id')).id + 1 if entryList else 1

    def addExistingEntry(self, entry):
            self.entryList.append(entry)

    def addNewEntry(self, name, date, category, cost, description):
        self.entryList.append(Entry(self.autonum, name, date, category, cost, description))
        print(self.autonum)
        self.autonum += 1

    def setInsideEntryList(self, listOfEntries):
        self.entryList = listOfEntries
        self.autonum = max(listOfEntries, key=attrgetter('id')).id+1 if listOfEntries else 1
        print(self.autonum)
    def getInsideEntryList(self) -> list[Entry]:
        return self.entryList

    def clear(self):
        self.entryList=[]

    def addReccuringFees(self, howManyTimes, span, name, startingDate, category, cost, description=""):
        for it in range(0,howManyTimes):
            self.addEntry(self.autonum, name, startingDate, category, cost, description)
            self.autonum+=1
            startingDate = startingDate + dt.timedelta(days=span)

    def updateId(self):
        self.autonum = max(self.entryList, key=attrgetter('id')).id+1 if self.entryList else 1

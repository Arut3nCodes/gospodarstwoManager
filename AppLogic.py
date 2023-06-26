import datetime
from EntryList import EntryList
class AppLogic:
    def __init__(self):
        self.entryList : EntryList = EntryList([])
        self.calendarEntryList : EntryList = EntryList([])
        self.daySummaryEntryList : EntryList = EntryList([])
        self.allPaymentsEntryList : EntryList = EntryList([])

    def getEntryList(self):
        return self.entryList

    def setEntryList(self, list):
        self.entryList = list

    def getCalendarEntryList(self):
        return self.calendarEntryList

    def setCalendarEntryList(self, list):
        self.calendarEntryList = list

    def getDaySummaryEntryList(self):
        return self.daySummaryEntryList

    def setDaySummaryEntryList(self, list):
        self.daySummaryEntryList = list

    def getAllPaymentsEntryList(self):
        return self.allPaymentsEntryList

    def setAllPaymentsEntryList(self, list):
        self.allPaymentsEntryList = list

    def sumAllForEveryDay(self, startDate, endDate, AppLogIns):
        sumsForEveryDayOfTheWeek = []
        if(AppLogIns.getEntryList().getInsideEntryList()):
            listOfAllInBetweenTheDates = list(filter(lambda object: startDate <= object.date <= endDate,
                                                AppLogIns.getEntryList().getInsideEntryList()))
            while startDate <= endDate:
                tempList = list(filter(lambda object: startDate == object.date, listOfAllInBetweenTheDates))
                sumsForEveryDayOfTheWeek.append(sum(obj.cost for obj in tempList))
                startDate = startDate + datetime.timedelta(days=1)
        else:
            sumsForEveryDayOfTheWeek=[0.0]*7
        return sumsForEveryDayOfTheWeek

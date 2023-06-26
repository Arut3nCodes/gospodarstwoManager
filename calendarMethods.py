from PyQt6 import QtWidgets
import time


def calendarTabUpdate(ui):
    ui.calendarRecordsList.clear()
    if len(ui.appLogicInstance.getEntryList().getInsideEntryList()):
        forceStop = 0
        for entry in ui.appLogicInstance.getEntryList().getInsideEntryList():
            if (entry.date == ui.calendar.selectedDate().toPyDate()):
                ui.appLogicInstance.getCalendarEntryList().addExistingEntry(entry)
                ui.calendarRecordsList.addItem(QtWidgets.QListWidgetItem(str(entry)))
            if forceStop == 10:
                time.sleep(5)
            forceStop+=1


def calendarActivated(calendar, appLogIns, calendarListWidget):
    calendarListWidget.clear()
    if len(appLogIns.getEntryList().getInnerEntryList()):
        for entry in appLogIns.getEntryList().getInnerEntryList():
            if (entry.date == calendar.selectedDate().toPyDate()):
                appLogIns.getCalendarEntryList().addExistingEntry(entry)
                calendarListWidget.addItem(QtWidgets.QListWidgetItem(str(entry)))
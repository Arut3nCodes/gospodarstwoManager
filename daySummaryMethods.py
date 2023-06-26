from PyQt6 import QtWidgets
import sorters as sts

def daySummaryTabUpdate(ui):
    if (ui.daySumSortComboBox.currentIndex() != 0):
        ui.daySumSortComboBox.setCurrentIndex(0)
    ui.dayRecordsList.clear()
    ui.appLogicInstance.getDaySummaryEntryList().setInsideEntryList(
         ui.appLogicInstance.getEntryList().getInsideEntryList().copy())
    list = ui.appLogicInstance.getDaySummaryEntryList().getInsideEntryList()
    for entry in list:
        ui.dayRecordsList.addItem(QtWidgets.QListWidgetItem(str(entry)))
def dateEditDateChanged(dateEdit, appLogIns, daySummaryEntryListWidget, daySummaryComboBox):
    daySummaryEntryListWidget.clear()
    appLogIns.getDaySummaryEntryList().setInsideEntryList([])

    if(appLogIns.getEntryList().getInsideEntryList()):
        for entry in appLogIns.getEntryList().getInsideEntryList():
            if dateEdit.date().toPyDate() == entry.date:
                appLogIns.getDaySummaryEntryList().addExistingEntry(entry)
                daySummaryEntryListWidget.addItem(QtWidgets.QListWidgetItem(str(entry)))
    daySummaryComboBox.setCurrentIndex(0)

def daySummarySortComboBoxChanged(daySumSortComboBox, appLogIns, daySummaryEntryListWidget):
    daySummaryEntryListWidget.clear()
    list = appLogIns.getDaySummaryEntryList().getInsideEntryList()
    if(appLogIns.getDaySummaryEntryList().getInsideEntryList()):
        match daySumSortComboBox.currentIndex():
            case 0:
                sts.sortById(list)
            case 1:
                sts.sortByName(list)
            case 2:
                sts.sortByCategory(list)
            case 3:
                sts.sortByCost(list)
        for entry in list:
            daySummaryEntryListWidget.addItem(QtWidgets.QListWidgetItem(str(entry)))
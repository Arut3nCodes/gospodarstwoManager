from EntryList import EntryList
import loadAndSave as las
from addDialog import *


def loadAction(appLogIns, allPaymentsList):
    appLogIns.setEntryList(EntryList(las.loadEntries()[0]))
    appLogIns.setAllPaymentsEntryList(EntryList(las.loadEntries()[0]))
    allPaymentsList.clear()
    for entry in appLogIns.getEntryList().getInsideEntryList():
        allPaymentsList.addItem(QtWidgets.QListWidgetItem(str(entry)))

def saveAction(appLogIns):
    las.saveEntries(appLogIns.getEntryList().getInsideEntryList())
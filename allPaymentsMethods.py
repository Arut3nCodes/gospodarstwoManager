from PyQt6 import QtWidgets
import sorters as sts
import addDialog


def readDetailsPayments(mainWindow, ui):
        addDialog.runReadOnly(mainWindow, ui)
def allPaymentsTabUpdate(ui):
    if(ui.allPaymentsSortCombo.currentIndex() != 0):
        ui.allPaymentsSortCombo.setCurrentIndex(0)

    else:
        ui.allPaymentsList.clear()
        ui.appLogicInstance.getAllPaymentsEntryList().setInsideEntryList(ui.appLogicInstance.getEntryList().getInsideEntryList().copy())
        list = ui.appLogicInstance.getAllPaymentsEntryList().getInsideEntryList()
        for entry in list:
           ui.allPaymentsList.addItem(QtWidgets.QListWidgetItem(str(entry)))

def addItem(appLogicInstance, listWidget, mainWindow, ui):
    data = addDialog.runAndReturnAddWindow(mainWindow)
    if data is not None:
        name, date, category, price, description = data
        appLogicInstance.getEntryList().addNewEntry(name, date, category, price, description)
        ui.updateAllTabs()
def deleteItem(ui):
    if ui.allPaymentsList.count() and ui.allPaymentsList.currentItem() is not None:
        ourObject = ui.appLogicInstance.getAllPaymentsEntryList().getInsideEntryList()[ui.allPaymentsList.row(ui.allPaymentsList.currentItem())]
        ui.appLogicInstance.getEntryList().getInsideEntryList().remove(ourObject)
        ui.updateAllTabs()
        ui.appLogicInstance.getEntryList().updateId()

def editItem(mainWindow, ui):
    if ui.allPaymentsList.count() and ui.allPaymentsList.currentItem() is not None:
        addDialog.runAndReturnEditWindow(mainWindow, ui)

def allPaymentsSortComboBoxChanged(allPaymentsSortComboBox, appLogIns, allPaymentsEntryListWidget):
    allPaymentsEntryListWidget.clear()
    appLogIns.getAllPaymentsEntryList().setInsideEntryList(appLogIns.getEntryList().getInsideEntryList().copy())
    list = appLogIns.getAllPaymentsEntryList().getInsideEntryList()
    if(appLogIns.getAllPaymentsEntryList().getInsideEntryList()):
        match allPaymentsSortComboBox.currentIndex():
            case 0:
                sts.sortById(list)
            case 1:
                sts.sortByName(list)
            case 2:
                sts.sortByDate(list)
            case 3:
                sts.sortByCategory(list)
            case 4:
                sts.sortByCost(list)
        for entry in list:
            allPaymentsEntryListWidget.addItem(QtWidgets.QListWidgetItem(str(entry)))

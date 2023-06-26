import datetime as dt
import dateManip

def updateWeekTab(ui):
    listOfQEditLines = [ui.mondayLine, ui.tuesdayLine, ui.wednesdayLine, ui.thursdayLine, ui.fridayLine,
                        ui.saturdayLine, ui.sundayLine, ui.dateLineLabel, ui.dateLineLabel2, ui.weekLineEdit,
                        ui.yearLineEdit]

    ui.weekLineEdit.setText(str(dt.date.today().isocalendar().week))
    ui.yearLineEdit.setText(str(dt.date.today().year))
    ui.dateLineLabel.setText(
        str(dateManip.getFirstAndLastDayOfTheWeek(dt.date.today().year, dt.date.today().isocalendar().week)[
                0]))
    ui.dateLineLabel2.setText(
        str(dateManip.getFirstAndLastDayOfTheWeek(dt.date.today().year, dt.date.today().isocalendar().week)[
                1]))
    changeQEditLinesBasedOnDates(listOfQEditLines, ui.appLogicInstance, )


def leftButtonAction(listOfQEditLines, appLogIns):
    listOfQEditLines[9].setText(str(int(listOfQEditLines[9].text())-1))
    listOfQEditLines[10].setText(str(max(int(listOfQEditLines[10].text()), 1900)))
    if(int(listOfQEditLines[9].text()) < 1):
        listOfQEditLines[9].setText(str(dt.date.fromisoformat(f'{int(listOfQEditLines[10].text()) - 1}-12-31').isocalendar().week))
        listOfQEditLines[10].setText(str(max(int(listOfQEditLines[10].text()) - 1, 1900)))
    listOfQEditLines[7].setText(
        str(dateManip.getFirstAndLastDayOfTheWeek(int(listOfQEditLines[10].text()), int(listOfQEditLines[9].text()))[
                0]))
    listOfQEditLines[8].setText(
        str(dateManip.getFirstAndLastDayOfTheWeek(int(listOfQEditLines[10].text()), int(listOfQEditLines[9].text()))[
                1]))
    changeQEditLinesBasedOnDates(listOfQEditLines, appLogIns)
def rightButtonAction(listOfQEditLines, appLogIns):
    listOfQEditLines[9].setText(str(int(listOfQEditLines[9].text())+1))
    listOfQEditLines[10].setText(str(max(int(listOfQEditLines[10].text()), 1900)))
    try:
        listOfQEditLines[7].setText(
        str(dateManip.getFirstAndLastDayOfTheWeek(int(listOfQEditLines[10].text()), int(listOfQEditLines[9].text()))[
                0]))
        listOfQEditLines[8].setText(
        str(dateManip.getFirstAndLastDayOfTheWeek(int(listOfQEditLines[10].text()), int(listOfQEditLines[9].text()))[
                1]))
    except Exception:
        listOfQEditLines[9].setText(str(1))
        listOfQEditLines[10].setText(str(max(int(listOfQEditLines[10].text()) + 1, 1900)))
        listOfQEditLines[7].setText(
            str(dateManip.getFirstAndLastDayOfTheWeek(int(listOfQEditLines[10].text()),
                                                      int(listOfQEditLines[9].text()))[0]))
        listOfQEditLines[8].setText(
            str(dateManip.getFirstAndLastDayOfTheWeek(int(listOfQEditLines[10].text()),
                                                      int(listOfQEditLines[9].text()))[1]))
    changeQEditLinesBasedOnDates(listOfQEditLines, appLogIns)

def changeQEditLinesBasedOnDates(listOfQEditLines, appLogIns):
    listOfSums = appLogIns.sumAllForEveryDay(dt.datetime.strptime(listOfQEditLines[7].text(), '%Y-%m-%d').date(),
                                             dt.datetime.strptime(listOfQEditLines[8].text(), '%Y-%m-%d').date(), appLogIns)
    for i in range(0,7):
        listOfQEditLines[i].setText(f'{listOfSums[i]:.2f} zl')
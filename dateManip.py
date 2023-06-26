import datetime as dt

def getFirstAndLastDayOfTheWeek(year, week):
    return dt.date.fromisocalendar(year, week, 1), dt.date.fromisocalendar(year, week, 7)
import csv
import Entry
import datetime as dt
import sorters as sts
def loadEntries(listOfCategories=[]):
    try:
        with open('entries.csv', mode='r') as file:
            csvreader = csv.reader(file, delimiter=';', quotechar='|')
            listOfEntries = []
            for row in csvreader:
                try:
                    (id, name, date, category, cost, description) = tuple(row)
                    date = date.split('-')
                    entry = Entry.Entry(id, name, dt.date(int(date[0]), int(date[1]), int(date[2])), category, cost, description)
                    if(entry.selfCheck()):
                        if(category not in listOfCategories):
                            listOfCategories.append(category)
                        listOfEntries.append(entry)
                except Exception:
                    print('line is incorrect, proceeding further...')
            sts.sortById(listOfEntries)
            return listOfEntries, listOfCategories
    except FileNotFoundError:
        return "ABORTED"
def saveEntries(listOfEntries : list[Entry.Entry]):
    try:
        with open('entries.csv', mode='w', newline='') as file:
            csvwriter = csv.writer(file, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for entry in listOfEntries:
                csvwriter.writerow(entry.toList())
    except FileNotFoundError:
        print('ABORTED')



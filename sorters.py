from Entry import Entry
from operator import attrgetter


def sortById(listOfEntries):
    listOfEntries.sort(key=attrgetter('id'))

def sortByName(listOfEntries):
    listOfEntries.sort(key=attrgetter('name', 'id'))


def sortByDate(listOfEntries):
    listOfEntries.sort(key=attrgetter('date', 'id'))


def sortByCategory(listOfEntries):
    listOfEntries.sort(key=attrgetter('category', 'id'))


def sortByCost(listOfEntries):
    listOfEntries.sort(key=attrgetter('cost', 'id'))


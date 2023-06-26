import datetime

class Entry:
    def __init__(self, id, name, date, category, cost, description=""):
        self.id : int = int(id)
        self.name: str = name
        self.date : datetime.date = date
        self.category : str = category
        self.cost : float = float(cost)
        self.description : str = description


    def __str__(self):
        return f"ID[{self.id}]:\t{self.name}\t{self.date}\t{self.category}\t{self.cost:.2f}zl"


    def __repr__(self):
        return f"ID[{self.id}]:\t{self.name}\t{self.date}\t{self.category}\t{self.cost:.2f}zl"

    def selfCheck(self):
        if not 6 <= self.name.len <= 30 or not self.name.isalnum():
            return False
        elif not 4 <= self.category.len <= 20 or not self.category.isalnum():
            return False
        elif not 0 < self.cost <= 100000000:
            return False
        return True
    def toList(self):
        return [self.id, self.name, self.date, self.category, self.cost, self.description]

    def __eq__(self, other):
        if(self.id == other.id):
            return True
        return False
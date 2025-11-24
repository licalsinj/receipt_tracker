import datetime as dt
class Transactions:
    date: dt.date
    payee: str
    category: str
    amount: float
    description: str
    project: str
    notes: str
    link: str

    def __init__(self, date, payee, category, amount, description, project, notes, link):
        self.date = date
        self.payee = payee
        self.category = category
        self.amount = amount
        self.description = description
        self.project = project
        self.notes = notes
        self.link = link
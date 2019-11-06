import datetime

class Person:
    def __init__(self, first_name: str, last_name: str, DOB: DateTime, email = None):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.email = email

def set_first_name

def get_age(self) -> int:
    now = datetime.datetime.now()
    return now.year - self._DOB.year
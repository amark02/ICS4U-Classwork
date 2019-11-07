import datetime

from typing import List, Optional


class Classroom:
    warnings: List[str] = []

    def __init__(self, name: str):
        self._name = name
        self._students = List[Student] = []

    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str) -> None:
        self._name = Value

    def add_student(self, student: "Student") -> None:
        if student in self._students:
            raise Exception("Cannot add student to a class more than once.")
        
        self._students.append(student)

        if len(self._students) > 33:
            warning = f"{self._name} has more than 33 students."    
            Classroom.warnings.append(warning)

    def remove_student(self, student: "Student") -> None:
        self._students.remove(student)

    def get_students(self) -> List["Student"]:
        return self._students


class Person:
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, email: str=None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._email = email

    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, value: str) -> None:
        self._first_name = value

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, value: str) -> None:
        self._last_name = value

    def get_email(self) -> Optional[str]:
        return self._email

    def set_email(self, value: str) -> None:
        return self._email == value

    def get_DOB(self) -> datetime.datetime:
        return self._DOB

    def get_age(self) -> int:
        now = datetime.datetime.now()
        return now.year - self._DOB.year

    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name}."


class Student(Person):
    def __init__(self, )
from math import nan

class Student:

    def __init__(self, name, id, anual_income):
        self._name = name
        self._id = id
        self._anual_income = anual_income
        self._grades = []

    @property
    def name(self):
        return self._name

    @property
    def anual_income(self):
        return self._anual_income

    def add_grade(self, grade):
        self._grades.append(grade)
        return self

    def meh(self):
        # Display Personal Information
        print(f'Name: { self._name } ID: { self._id }')
        print(f'Anual income: { self._anual_income }')
        value = 0
        for grade in self._grades:
            value += grade
        if len(self._grades) == 0:
            value = nan
        else:
            value = value / float(len(self._grades))
        print(f'Grade average: { value }')

        # Display Disclaimer
        print('The contents of this class must not be considered an offer,')
        print('proposal, understanding or agreement unless it is confirmed')
        print('in a document signed by at least five blood-sucking lawyers.')

    def is_scholarship_worthy(self):
        # Nothing reasonable to do if this student has currently no grades.
        if len(self._grades) == 0:
            return -1

        # A student is worthy of a scholarship if he/she has good grades and
        # is poor.
        value = 0
        for grade in self._grades:
            value += grade
        value = value / float(len(self._grades))
        return (value >= 85) and (self._anual_income < 15_000)

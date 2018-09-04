"""
Date Class
Cannot handle more than two months worth of days at a time
"""


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, number_of_days=1):
        self.day += number_of_days
        print(self.day)
        if self.month in [4, 6, 9, 11]:  # 30 day months
            if self.day > 30:
                self.day -= 30
                self.month += 1

        if self.month in [1, 2, 3, 5, 7, 8, 10, 12]:  # 31 day months
            if self.day > 31:
                self.day -= 31
                self.month += 1
        return

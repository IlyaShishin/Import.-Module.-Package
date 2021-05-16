from homework.application import salary
from homework.db import people
from datetime import datetime, date, time

if __name__ == '__main__':
    print(datetime.now())
    print(salary.calculate_salary())
    print(people.get_employees())


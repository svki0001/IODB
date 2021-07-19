from dbQuerys import dbQuerys
from faker import Faker
from random import randrange
from datetime import timedelta
from dbQuerys import dbQuerys

class Log_Users_Faker:
    faker = None

    def __init__(self) -> None:
        self.faker = Faker()

    def get_cardID(self):
        return dbQuerys.get_random_cardID()

    def get_checkIn(self):
        return self.faker.date_time_between(start_date="-1y", end_date="-1d")

    def get_checkOut(self, check_in):
        sessionTimeMinutes = randrange(180) + 1
        return check_in + timedelta(minutes=sessionTimeMinutes)
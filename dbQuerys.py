import time
from datetime import datetime, timedelta

from DB import db

class dbQuerys:
    @classmethod
    def addUser(self, cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor()

        sql = """INSERT INTO Users (cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city)
                 VALUES ('{cardID}', '{username}', '{email}', '{prename}', '{surname}', '{birthDate}', '{sex}', '{validityDate}', '{state}', '{note}', '{rights}', '{street}', {postcode}, '{city}')""".format(cardID=cardID, username=username, email=email, prename=prename, surname=surname, birthDate=birthDate, sex=sex, validityDate=validityDate, state=state, note=note, rights=rights, street=street, postcode=postcode, city=city)

        cursor.execute(sql)
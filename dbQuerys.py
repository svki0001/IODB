from DB import db

class dbQuerys:
    @classmethod
    def add_user(self, cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor()

        sql = """INSERT INTO Users (cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city)
                 VALUES ('{cardID}', '{username}', '{email}', '{prename}', '{surname}', '{birthDate}', '{sex}', '{validityDate}', '{state}', '{note}', '{rights}', '{street}', {postcode}, '{city}')""".format(cardID=cardID, username=username, email=email, prename=prename, surname=surname, birthDate=birthDate, sex=sex, validityDate=validityDate, state=state, note=note, rights=rights, street=street, postcode=postcode, city=city)

        cursor.execute(sql)

    @classmethod
    def get_random_cardID(self):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor(dictionary = True, buffered = True)

        sql = """SELECT cardID FROM Users
                 ORDER BY RAND()
                 LIMIT 1;"""

        cursor.execute(sql)

        data = cursor.fetchone()

        return data["cardID"]